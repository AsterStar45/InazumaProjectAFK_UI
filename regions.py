REGIONES = [
    {
        "nombre": "Empezar Partido",
        "region": (790, 950, 350, 80),
        "palabras": ["EMP", "PART", "PULSA", "BOTON"],
        "min_match": 1,        
        "tecla": "enter",
        "cooldown": 1.0,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Confirmar Si",
        "region": (480, 600, 300, 80),
        "palabras": ["SI"],
        "tecla": "enter",
        "cooldown": 1.0,
        "psm": 7,
        "lang": "eng"
    },
    
    {
        "nombre": "Comenzar 2da Parte",
        "region": (1568, 960, 300, 80),
        "palabras": ["COM", "PART", "SIG"],
        "repetir_texto": True,
        "min_match": 1,            
        "tecla": "enter",
        "cooldown": 1.0,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Siguiente / Finalizar",
        "region": (1570, 900, 320, 80),
        "palabras": ["SIGUIENTE", "FINALIZAR", "PARTIDO"],
        "repetir_texto": True,
        "tecla": "enter",
        "cooldown": 1.0,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Modo Manual",
        "region": (380, 730, 280, 90),
        "palabras": ["MAN"],
        "tecla": "u",
        "min_match": 1,          
        "cooldown": 1.0,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Terminar edicion",
        "region": (230, 960, 400, 90),
        "palabras": ["TERMINAR", "EDICION"],
        "click": True,
        "click_pos": "center",
        "click_tipo": "left",
        "click_delay": 0.1,
        "cooldown": 1.0,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Saque de Centro",
        "region": (810, 890, 300, 80),
        "palabras": ["SAQUE", "CENTRO","REA"],
        "min_match": 1,    
        "click": True,
        "click_pos": "center",
        "click_tipo": "left",
        "click_delay": 0.1,
        "cooldown": 1.0,
        "psm": 7,
        "lang": "eng"
    },

    {
        "nombre": "Luz eterna",
        "region": (890, 340, 160, 40),
        "palabras": ["LUZ", "ETER"],
        "min_match": 1,          
        "tecla": "enter",
        "cooldown": 1.0,
        "psm": 7,
        "lang": "eng"
    },    

    {
        "nombre": "Batalla heroica",
        "region": (250, 480, 120, 60),
        "palabras": ["PLAN"],     
        "min_match": 1,             
        "repetir_texto": True,
        "click": True,
        "click_pos": (415, 780),
        "click_tipo": "left",
        "click_delay": 0.1,
        "cooldown": 1.0,
        "psm": 7,
        "lang": "eng"
    },        
]
