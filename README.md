# JustIA - Inteligencia Artificial para Apoyo Jurídico

## Descripción del Proyecto

Este repositorio contiene el desarrollo de las actividades prácticas propuestas para el caso de estudio **JustIA**, una iniciativa orientada a fortalecer los servicios del Consultorio Virtual de la Corporación Universitaria de Asturias mediante el uso responsable de Inteligencia Artificial (IA) y Procesamiento de Lenguaje Natural (NLP).

El objetivo del proyecto es construir componentes básicos que permitan:

- Preparar datos jurídicos para entrenamiento de modelos de IA.
- Clasificar automáticamente textos jurídicos según su temática.
- Simular una primera capa de interacción con usuarios mediante consola.
- Aplicar principios de trazabilidad, transparencia y ética en sistemas jurídicos asistidos por IA.

---

# Objetivos

## Objetivo General

Diseñar e implementar componentes básicos de Inteligencia Artificial que sirvan como base para el sistema JustIA, garantizando buenas prácticas técnicas y éticas en el tratamiento de información jurídica.

## Objetivos Específicos

- Construir un corpus jurídico limpio y estructurado.
- Aplicar técnicas de preprocesamiento de texto para NLP.
- Crear un diccionario jurídico temático.
- Implementar un clasificador básico basado en palabras clave.
- Simular la interacción de usuarios con el sistema JustIA.
- Garantizar la trazabilidad de las decisiones tomadas por el sistema.

---

# Estructura del Proyecto

```text
Scripts-Entregable-Asturias/
│
├── scripts1.py
├── scripts2.py
├── scripts3.py
│
├── corpus_juridico_original.csv
├── corpus_juridico_limpio.csv
├── corpus_juridico_limpio.json
│
├── diccionario_juridico.json
│
├── README.md
└── requirements.txt
```

---

# Actividad 1 - Preprocesamiento del Corpus Jurídico

## Objetivo

Preparar un conjunto de datos jurídicos limpios y estructurados que puedan utilizarse posteriormente en modelos de Procesamiento de Lenguaje Natural (NLP).

## Funcionalidades implementadas

### Construcción de Corpus Jurídico

Se generó un corpus compuesto por 50 fragmentos jurídicos simulados relacionados con:

- Derecho laboral
- Derecho penal
- Derecho civil
- Derecho constitucional
- Derecho administrativo
- Derecho de familia
- Derecho migratorio
- Víctimas del conflicto armado

### Limpieza de Texto

Se aplicaron las siguientes transformaciones:

- Conversión a minúsculas.
- Eliminación de tildes.
- Eliminación de símbolos especiales.
- Eliminación de espacios redundantes.

### Tokenización

Se dividieron los textos en palabras individuales para facilitar su procesamiento.

### Eliminación de Stopwords

Se eliminaron palabras frecuentes que no aportan significado jurídico relevante.

Ejemplos:

```text
de
la
para
con
el
una
```

### Lematización

Se implementó una lematización básica para reducir variaciones lingüísticas.

Ejemplo:

```text
trabajadores → trabajador
demandas → demanda
obligaciones → obligacion
```

### Exportación

El corpus procesado se exporta automáticamente en:

- CSV
- JSON

Archivos generados:

```text
corpus_juridico_original.csv
corpus_juridico_limpio.csv
corpus_juridico_limpio.json
```

---

# Actividad 2 - Diccionario Jurídico y Clasificación

## Objetivo

Construir una base de conocimiento jurídica capaz de identificar la temática principal de un texto.

## Categorías Implementadas

### Familia

```text
custodia
alimentos
divorcio
matrimonio
hijo
adopcion
```

### Laboral

```text
salario
despido
prestaciones
empleado
empleador
```

### Penal

```text
delito
hurto
captura
prision
fiscalia
```

### Civil

```text
contrato
propiedad
indemnizacion
arrendamiento
```

### Constitucional

```text
tutela
derecho fundamental
igualdad
constitucion
```

### Administrativo

```text
acto administrativo
resolucion
licencia
sancion
```

### Migratorio

```text
visa
migrante
asilo
refugio
```

### Víctimas del Conflicto

```text
victima
reparacion
conflicto armado
restitucion de tierras
```

---

## Método de Clasificación

El sistema realiza:

1. Limpieza del texto.
2. Comparación con palabras clave.
3. Conteo de coincidencias.
4. Asignación de la categoría más probable.

### Ejemplo

Entrada:

```text
La víctima solicita reparación integral por hechos ocurridos durante el conflicto armado.
```

Salida:

```text
Categoría más probable:
victimas_conflicto
```

---

# Actividad 3 - Simulación de Interfaz JustIA

## Objetivo

Simular la interacción básica entre un usuario y el sistema JustIA.

## Funcionalidades

### Menú Principal

```text
1. Ingresar una pregunta legal
2. Seleccionar documento de entrada
3. Ejecutar clasificación simulada
4. Salir
```

### Consulta Jurídica

Permite ingresar preguntas en lenguaje natural.

Ejemplo:

```text
¿Puedo reclamar prestaciones después de un despido injustificado?
```

### Selección de Documento

Simula la carga de:

- PDF
- TXT

### Clasificación de Casos

Permite identificar automáticamente el área jurídica relacionada.

---

# Decisiones Técnicas Adoptadas

## ¿Por qué Python?

Python es actualmente el lenguaje más utilizado en Inteligencia Artificial y Procesamiento de Lenguaje Natural debido a:

- Facilidad de aprendizaje.
- Amplio ecosistema de librerías.
- Integración con modelos de Machine Learning.

## ¿Por qué utilizar un diccionario jurídico?

Se optó inicialmente por un enfoque basado en reglas debido a:

- Mayor transparencia.
- Fácil auditoría.
- Menor complejidad técnica.
- Mejor interpretabilidad para el equipo jurídico.

## ¿Por qué no usar directamente una red neuronal?

Aunque las redes neuronales ofrecen mejores resultados en muchos escenarios, presentan desafíos importantes:

- Menor interpretabilidad.
- Mayor complejidad de entrenamiento.
- Riesgo de sesgos ocultos.

Por ello se plantea una implementación progresiva iniciando con modelos explicables.

---

# Consideraciones Éticas

El proyecto JustIA se desarrolla bajo los siguientes principios:

## Transparencia

Todas las decisiones del sistema deben poder explicarse.

## Trazabilidad

Las respuestas generadas deben registrar:

- Fuente utilizada.
- Fecha.
- Categoría identificada.

## Supervisión Humana

La IA actúa únicamente como herramienta de apoyo.

No reemplaza:

- Estudiantes de derecho.
- Docentes.
- Profesionales jurídicos.

## No Discriminación

Se evita el uso de:

- Reconocimiento facial.
- Perfilamiento automatizado.
- Clasificación de usuarios por características sensibles.

---

# Requisitos

## Verificar Python

```bash
python --version
```

## Instalar dependencias

```bash
pip install pandas
```

o

```bash
pip install -r requirements.txt
```

---

# Ejecución

## Actividad 1

```bash
python scripts1.py
```

## Actividad 2

```bash
python scripts2.py
```

## Actividad 3

```bash
python scripts3.py
```

---

# Resultados Esperados

Al ejecutar correctamente el proyecto se generarán:

```text
corpus_juridico_original.csv
corpus_juridico_limpio.csv
corpus_juridico_limpio.json
diccionario_juridico.json
```

Además, la consola permitirá realizar pruebas de clasificación jurídica de manera interactiva.

---

# Conclusiones

La implementación desarrollada demuestra la viabilidad de utilizar técnicas básicas de Inteligencia Artificial y Procesamiento de Lenguaje Natural para apoyar procesos jurídicos. El enfoque adoptado prioriza la transparencia, la trazabilidad y la supervisión humana, elementos fundamentales cuando se trabaja con poblaciones vulnerables y contextos relacionados con el acceso a la justicia.

Este proyecto constituye una base sólida para futuras extensiones que incorporen modelos avanzados de NLP, extracción automática de entidades jurídicas y asistentes virtuales especializados.

---

# Autor

**David Carrasco**

Especialización en Desarrollo de Software  
Corporación Universitaria de Asturias

---

# Licencia

Proyecto desarrollado con fines académicos para la asignatura de Inteligencia Artificial y Procesamiento de Lenguaje Natural.
