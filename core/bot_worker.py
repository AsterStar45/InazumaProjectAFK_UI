from PySide6.QtCore import QThread, Signal
import pyautogui
import pytesseract
import cv2
import numpy as np
import time
import keyboard
import re

from core.regions import REGIONES

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class BotWorker(QThread):
    log = Signal(str)

    def __init__(self):
        super().__init__()
        self.running = True

        self.ultimo_texto = {}

        # Estado Saque de Centro
        self.saque_estado_activo = False
        self.saque_detectado_en = None
        self.saque_click_hecho = False
        self.saque_tecla_hecha = False

    def stop(self):
        self.running = False

    def obtener_pos_click(self, region, click_pos):
        x, y, w, h = self.region_px(region)

        if click_pos == "center":
            return x + w // 2, y + h // 2

        if isinstance(click_pos, tuple):
            return self.punto_px(click_pos)

        return None

    def puede_procesar_region(self, nombre, texto, repetir):
        if repetir:
            return True
        return texto != self.ultimo_texto.get(nombre)

    def region_px(self, region):
        sw, sh = pyautogui.size()
        x, y, w, h = region
        return (
            int(x * sw),
            int(y * sh),
            int(w * sw),
            int(h * sh),
        )


    def punto_px(self, punto):
        sw, sh = pyautogui.size()
        x, y = punto
        return int(x * sw), int(y * sh)

    def run(self):
        self.log.emit("BOT INICIADO")

        while self.running:
            for r in REGIONES:
                x, y, w, h = self.region_px(r["region"])
                screenshot = pyautogui.screenshot(region=(x, y, w, h))

                frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (5, 5), 0)
                gray = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)[1]

                texto = pytesseract.image_to_string(
                    gray,
                    config=f"--psm {r.get('psm',7)}",
                    lang=r.get("lang", "eng")
                )

                texto = texto.upper()
                texto = re.sub(r"[^A-Z0-9 ]", " ", texto)
                texto = re.sub(r"\s+", " ", texto).strip()

                # =========================
                # SAQUE DE CENTRO
                # =========================
                if r["nombre"] == "Saque de Centro":
                    ahora = time.time()
                    detecta_saque = ("SAQUE" in texto) or ("CENTRO" in texto)
                    detecta_reanudar = "REANUDAR" in texto

                    if detecta_reanudar:
                        pos = self.obtener_pos_click(r["region"], r.get("click_pos"))
                        if pos:
                            pyautogui.click(*pos)
                            self.log.emit("CLICK REANUDAR")
                        continue

                    if detecta_saque and not self.saque_estado_activo:
                        self.saque_estado_activo = True
                        self.saque_detectado_en = ahora
                        self.log.emit("SAQUE DETECTADO")

                    if self.saque_estado_activo:
                        if not self.saque_click_hecho:
                            pos = self.obtener_pos_click(r["region"], r.get("click_pos"))
                            if pos:
                                pyautogui.click(*pos)
                                self.log.emit("CLICK SAQUE")
                            self.saque_click_hecho = True

                        if not self.saque_tecla_hecha:
                            if ahora - self.saque_detectado_en >= 1:
                                pyautogui.press("u")
                                self.log.emit("TECLA U")
                                self.saque_tecla_hecha = True

                        if self.saque_click_hecho and self.saque_tecla_hecha:
                            self.saque_estado_activo = False
                            self.saque_click_hecho = False
                            self.saque_tecla_hecha = False
                            self.saque_detectado_en = None
                    continue

                # =========================
                # LOGICA NORMAL
                # =========================

                repetir = r.get("repetir_texto", False)

                if not self.puede_procesar_region(r["nombre"], texto, repetir):
                    continue

                self.ultimo_texto[r["nombre"]] = texto

                coincidencias = sum(1 for p in r["palabras"] if p in texto)
                min_match = r.get("min_match", 1)

                if coincidencias >= min_match:
                    self.log.emit(f"ACCION: {r['nombre']}")

                    if r.get("click"):
                        pos = self.obtener_pos_click(r["region"], r.get("click_pos"))
                        if pos:
                            pyautogui.click(*pos)

                    if r.get("tecla"):
                        pyautogui.press(r["tecla"])

            time.sleep(0.1)

        self.log.emit("BOT DETENIDO")
