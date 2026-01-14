import pyautogui
import pytesseract
import cv2
import numpy as np
import time
import keyboard
import re

from regions import REGIONES

# AJUSTA ESTA RUTA SI ES NECESARIO
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# =========================
# FUNCIONES
# =========================

def obtener_pos_click(region, click_pos):
    x, y, w, h = region

    if click_pos == "center":
        return x + w // 2, y + h // 2

    if isinstance(click_pos, tuple):
        return click_pos

    return None


# =========================
# VARIABLES
# =========================

ultimo_disparo = {}
ultimo_texto = {}

print("BOT OCR INICIADO")
print("Presiona ESC para salir")

time.sleep(2)

# =========================
# LOOP PRINCIPAL
# =========================

while True:
    if keyboard.is_pressed("esc"):
        print("Saliendo...")
        break

    for r in REGIONES:
        x, y, w, h = r["region"]

        screenshot = pyautogui.screenshot(region=(x, y, w, h))
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Preprocesado
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        gray = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)[1]

        # OCR
        config = f"--psm {r.get('psm', 7)}"
        texto = pytesseract.image_to_string(
            gray,
            config=config,
            lang=r.get("lang", "spa")
        )

        texto = texto.upper()
        texto = re.sub(r"[^A-Z0-9 ]", " ", texto)
        texto = re.sub(r"\s+", " ", texto).strip()

        # Debug visual
        cv2.imshow(r["nombre"], gray)
        cv2.waitKey(1)
        print(f"[{r['nombre']}] OCR -> '{texto}'")

        # Repetir region
        def puede_procesar_region(region, texto, ultimo_texto):
            if r.get("repetir_texto", False):
                return True
            return texto != ultimo_texto.get(region)

        # Evitar repetir mismo texto
        if not puede_procesar_region(r["nombre"], texto, ultimo_texto):
            continue

        ultimo_texto[r["nombre"]] = texto

        # Buscar palabras clave (todas deben estar)
        coincidencias = sum(1 for p in r["palabras"] if p in texto)
        min_match = r.get("min_match", 1)

        if coincidencias >= min_match:
            ahora = time.time()
            ultimo = ultimo_disparo.get(r["nombre"], 0)

            if ahora - ultimo >= r["cooldown"]:
                print(f">>> ACCION DETECTADA: {r['nombre']}")

                # TECLA
                if r.get("tecla"):
                    print("   -> presionando tecla:", r["tecla"])
                    pyautogui.press(r["tecla"])

                # CLICK
                if r.get("click"):
                    time.sleep(r.get("click_delay", 0))
                    pos = obtener_pos_click(r["region"], r.get("click_pos", "center"))
                    if pos:
                        print("   -> click en:", pos)
                        pyautogui.click(
                            x=pos[0],
                            y=pos[1],
                            button=r.get("click_tipo", "left")
                        )

                ultimo_disparo[r["nombre"]] = ahora

    time.sleep(0.1)

cv2.destroyAllWindows()
