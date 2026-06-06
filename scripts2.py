# ============================================================
# ACTIVIDAD 2 - DICCIONARIO JURÍDICO Y CLASIFICADOR BÁSICO
# Proyecto: JustIA
# ============================================================

import json
import re
import unicodedata

diccionario_juridico = {
    "familia": [
        "custodia", "alimentos", "divorcio", "matrimonio",
        "hijo", "menor", "patria potestad", "paternidad",
        "adopcion", "familia", "sociedad conyugal"
    ],
    "laboral": [
        "contrato laboral", "empleado", "empleador", "salario",
        "despido", "prestaciones", "liquidacion", "horas extras",
        "acoso laboral", "accidente laboral", "trabajador"
    ],
    "penal": [
        "delito", "hurto", "fiscalia", "captura", "prision",
        "pena", "acusado", "lesiones", "amenazas", "estafa",
        "violencia intrafamiliar"
    ],
    "civil": [
        "contrato", "obligacion", "indemnizacion", "responsabilidad",
        "arrendamiento", "propiedad", "perjuicio", "compraventa",
        "sucesion", "bien inmueble", "demanda civil"
    ],
    "constitucional": [
        "tutela", "derecho fundamental", "igualdad", "salud",
        "educacion", "debido proceso", "constitucion",
        "accion popular", "accion de grupo"
    ],
    "administrativo": [
        "acto administrativo", "resolucion", "alcaldia",
        "sancion", "licencia", "entidad publica", "recurso",
        "revocatoria directa", "servidor publico"
    ],
    "migratorio": [
        "migrante", "visa", "asilo", "refugio", "regularizacion",
        "permiso", "deportacion", "frontera", "extranjero"
    ],
    "victimas_conflicto": [
        "victima", "conflicto armado", "desplazado", "reparacion",
        "restitucion de tierras", "lider social", "comunidad rural",
        "proteccion", "violencia"
    ]
}

def eliminar_tildes(texto):
    texto_normalizado = unicodedata.normalize("NFD", texto)
    return "".join(
        caracter for caracter in texto_normalizado
        if unicodedata.category(caracter) != "Mn"
    )

def limpiar_texto(texto):
    texto = texto.lower()
    texto = eliminar_tildes(texto)
    texto = re.sub(r"[^a-zñ\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

def guardar_diccionario():
    with open("diccionario_juridico.json", "w", encoding="utf-8") as archivo:
        json.dump(diccionario_juridico, archivo, ensure_ascii=False, indent=4)

def clasificar_texto(texto):
    texto_limpio = limpiar_texto(texto)

    puntajes = {}

    for categoria, palabras_clave in diccionario_juridico.items():
        puntaje = 0

        for palabra in palabras_clave:
            palabra_limpia = limpiar_texto(palabra)

            if palabra_limpia in texto_limpio:
                puntaje += 1

        puntajes[categoria] = puntaje

    categoria_probable = max(puntajes, key=puntajes.get)

    if puntajes[categoria_probable] == 0:
        return "sin clasificar", puntajes

    return categoria_probable, puntajes

if __name__ == "__main__":
    guardar_diccionario()

    print("Diccionario jurídico guardado como diccionario_juridico.json\n")

    texto = input("Ingrese el texto jurídico a clasificar: ")

    categoria, puntajes = clasificar_texto(texto)

    print("\nResultado de clasificación")
    print("--------------------------")
    print(f"Categoría más probable: {categoria}")
    print("\nPuntajes por categoría:")

    for categoria_nombre, puntaje in puntajes.items():
        print(f"- {categoria_nombre}: {puntaje}")