# ============================================================
# ACTIVIDAD 1 - PREPROCESAMIENTO DE CORPUS JURÍDICO JUSTIA
# Autor: David Manuel Carrasco Conde
# Objetivo:
# Preparar un conjunto de datos jurídicos limpios y estructurados
# para ser usado como insumo en modelos de NLP.
# ============================================================

import pandas as pd
import re
import unicodedata

# ------------------------------------------------------------
# 1. Simulación del corpus jurídico original
# ------------------------------------------------------------
# Se construye un corpus con 50 fragmentos jurídicos simulados.
# Estos textos representan posibles consultas, sentencias,
# resoluciones o descripciones de casos del consultorio jurídico.

corpus = [
    "Acción de tutela por vulneración del derecho fundamental a la salud.",
    "Demanda laboral por despido sin justa causa y falta de pago de prestaciones sociales.",
    "Proceso penal por hurto agravado cometido en establecimiento comercial.",
    "Solicitud de custodia compartida de menor de edad por parte del padre.",
    "Incumplimiento de contrato de arrendamiento de vivienda urbana.",
    "Proceso de alimentos a favor de hijo menor de edad.",
    "Demanda civil por responsabilidad contractual e indemnización de perjuicios.",
    "Acción popular por afectación al medio ambiente en comunidad rural.",
    "Solicitud de reconocimiento de pensión de vejez ante entidad pública.",
    "Proceso penal por violencia intrafamiliar contra mujer víctima.",
    "Reclamación laboral por no pago de horas extras.",
    "Tutela presentada por migrante para acceder a servicios de salud.",
    "Demanda de divorcio y liquidación de sociedad conyugal.",
    "Proceso administrativo sancionatorio contra establecimiento comercial.",
    "Recurso de reposición contra acto administrativo de una alcaldía.",
    "Solicitud de protección a víctima del conflicto armado.",
    "Proceso de sucesión intestada entre herederos.",
    "Demanda por incumplimiento de contrato de compraventa.",
    "Investigación penal por lesiones personales.",
    "Solicitud de restablecimiento de derechos de menor de edad.",
    "Tutela por vulneración del derecho a la educación.",
    "Reclamación por accidente laboral y riesgos profesionales.",
    "Proceso penal por acceso carnal violento.",
    "Demanda civil por daño moral y perjuicios materiales.",
    "Solicitud de visa y regularización migratoria.",
    "Acción de grupo por daños causados a comunidad indígena.",
    "Proceso de filiación y reconocimiento de paternidad.",
    "Demanda laboral por acoso en el lugar de trabajo.",
    "Proceso penal por estafa y abuso de confianza.",
    "Solicitud de nulidad de acto administrativo.",
    "Tutela contra EPS por negación de medicamento.",
    "Proceso ejecutivo por incumplimiento de obligación dineraria.",
    "Demanda de alimentos contra progenitor ausente.",
    "Solicitud de reparación integral para víctima del conflicto armado.",
    "Proceso disciplinario contra servidor público.",
    "Demanda por terminación unilateral de contrato laboral.",
    "Solicitud de protección por violencia económica en el hogar.",
    "Proceso de restitución de tierras para población desplazada.",
    "Demanda civil por incumplimiento de contrato de prestación de servicios.",
    "Acción constitucional por vulneración del derecho a la igualdad.",
    "Proceso penal por amenazas contra líder social.",
    "Solicitud de medidas de protección para mujer víctima de violencia.",
    "Reclamación laboral por liquidación incorrecta.",
    "Proceso administrativo por revocatoria directa de resolución.",
    "Demanda de pertenencia sobre bien inmueble.",
    "Tutela por falta de atención médica urgente.",
    "Proceso penal por violencia patrimonial en contexto familiar.",
    "Solicitud de asilo por persecución política.",
    "Demanda comercial por incumplimiento de obligaciones mercantiles.",
    "Proceso de adopción de menor de edad."
]

# ------------------------------------------------------------
# 2. Creación del DataFrame original
# ------------------------------------------------------------
# Se estructura el corpus en una tabla con un identificador
# y el texto original.

df = pd.DataFrame({
    "id": range(1, len(corpus) + 1),
    "texto_original": corpus
})

# ------------------------------------------------------------
# 3. Función para eliminar tildes
# ------------------------------------------------------------
# Se eliminan tildes para normalizar el texto.
# Esta decisión ayuda a reducir errores en documentos escaneados
# o textos con problemas de codificación.

def eliminar_tildes(texto):
    texto_normalizado = unicodedata.normalize("NFD", texto)
    texto_sin_tildes = ""

    for caracter in texto_normalizado:
        if unicodedata.category(caracter) != "Mn":
            texto_sin_tildes += caracter

    return texto_sin_tildes

# ------------------------------------------------------------
# 4. Función de limpieza básica
# ------------------------------------------------------------
# Se aplican las siguientes decisiones:
# - Convertir a minúsculas.
# - Eliminar tildes.
# - Eliminar signos y símbolos.
# - Eliminar espacios repetidos.

def limpiar_texto(texto):
    texto = texto.lower()
    texto = eliminar_tildes(texto)
    texto = re.sub(r"[^a-zñ\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()

    return texto

# ------------------------------------------------------------
# 5. Stopwords en español
# ------------------------------------------------------------
# Se definen palabras frecuentes que no aportan mucho valor
# para la clasificación jurídica.

stopwords = {
    "a", "ante", "bajo", "con", "contra", "de", "desde", "durante",
    "en", "entre", "hacia", "hasta", "para", "por", "segun", "sin",
    "sobre", "tras", "el", "la", "los", "las", "un", "una", "unos",
    "unas", "y", "o", "u", "que", "del", "al", "su", "sus", "se",
    "es", "son", "fue", "como", "parte", "favor"
}

# ------------------------------------------------------------
# 6. Función de tokenización y eliminación de stopwords
# ------------------------------------------------------------
# La tokenización divide el texto en palabras individuales.
# Luego se eliminan palabras comunes para conservar términos
# jurídicamente relevantes.

def tokenizar_y_filtrar(texto):
    tokens = texto.split()

    tokens_filtrados = []

    for token in tokens:
        if token not in stopwords:
            tokens_filtrados.append(token)

    return tokens_filtrados

# ------------------------------------------------------------
# 7. Lematización básica simulada
# ------------------------------------------------------------
# Para evitar dependencias externas, se implementa una lematización
# sencilla basada en un diccionario manual.
# En un proyecto real podría usarse spaCy con el modelo es_core_news_sm.

lemmas = {
    "demandas": "demanda",
    "derechos": "derecho",
    "victimas": "victima",
    "procesos": "proceso",
    "contratos": "contrato",
    "obligaciones": "obligacion",
    "prestaciones": "prestacion",
    "herederos": "heredero",
    "menores": "menor",
    "migrantes": "migrante",
    "comunidades": "comunidad",
    "sentencias": "sentencia",
    "resoluciones": "resolucion",
    "trabajadores": "trabajador",
    "empleados": "empleado"
}

def lematizar_tokens(tokens):
    tokens_lematizados = []

    for token in tokens:
        if token in lemmas:
            tokens_lematizados.append(lemmas[token])
        else:
            tokens_lematizados.append(token)

    return tokens_lematizados

# ------------------------------------------------------------
# 8. Función completa de preprocesamiento
# ------------------------------------------------------------
# Esta función integra:
# - Limpieza
# - Tokenización
# - Eliminación de stopwords
# - Lematización
# - Reconstrucción del texto limpio

def preprocesar_texto(texto):
    texto_limpio = limpiar_texto(texto)

    tokens = tokenizar_y_filtrar(texto_limpio)

    tokens_lematizados = lematizar_tokens(tokens)

    texto_final = " ".join(tokens_lematizados)

    return texto_final

# ------------------------------------------------------------
# 9. Aplicación del preprocesamiento
# ------------------------------------------------------------

df["texto_limpio"] = df["texto_original"].apply(preprocesar_texto)

# ------------------------------------------------------------
# 10. Guardado de archivos
# ------------------------------------------------------------
# Se guardan dos archivos:
# - corpus_juridico_original.csv
# - corpus_juridico_limpio.csv

df[["id", "texto_original"]].to_csv(
    "corpus_juridico_original.csv",
    index=False,
    encoding="utf-8"
)

df.to_csv(
    "corpus_juridico_limpio.csv",
    index=False,
    encoding="utf-8"
)

# También se guarda en formato JSON para interoperabilidad.

df.to_json(
    "corpus_juridico_limpio.json",
    orient="records",
    force_ascii=False,
    indent=4
)

# ------------------------------------------------------------
# 11. Visualización de resultados
# ------------------------------------------------------------

print("Proceso completado correctamente.\n")
print("Archivos generados:")
print("- corpus_juridico_original.csv")
print("- corpus_juridico_limpio.csv")
print("- corpus_juridico_limpio.json\n")

print("Vista previa del corpus procesado:\n")
print(df.head(10))