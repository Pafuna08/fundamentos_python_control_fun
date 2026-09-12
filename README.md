# Fundamentos de Python: estructuras de control y funciones

Proyecto individual para la evidencia **GA1-220501093-04-AA1-EV02**. El objetivo es practicar variables, literales, operadores aritmeticos, comparaciones, cadenas, estructuras condicionales, ciclos y funciones mediante ejercicios pequenos y faciles de verificar.

Cada archivo fue organizado para poder ejecutarse directamente o importarse como modulo. Las funciones separan la logica del programa de la entrada y salida de datos, lo que facilita las pruebas.

El contexto elegido para esta version es una bitacora de seguimiento academico. Los ejercicios representan situaciones de estudio: clasificacion de participantes, comparacion de sesiones, porcentaje de avance, registro de sesiones, puntos acumulados y actividades pares.

## Estructura

```text
fundamentos_python_control_fun/
|-- README.md
|-- src/
    |-- condicionales/
    |   |-- 01_clasificar_edad.py
    |   |-- 02_numero_mayor.py
    |   `-- 03_calificacion.py
    |-- iterativas/
    |   |-- 01_contador_while.py
    |   |-- 02_tabla_multiplicar.py
    |   `-- 03_suma_pares.py
    `-- funciones/
        |-- 01_saludar.py
        |-- 02_area_rectangulo.py
        `-- 03_es_par.py
`-- tests/
    `-- test_ejercicios.py
```

## Como ejecutar los ejercicios

1. Instala Python 3.
2. Abre una terminal en la carpeta del repositorio.
3. Ejecuta el archivo que quieras practicar.

Ejemplos en Windows:

```powershell
python src\condicionales\01_clasificar_edad.py
python src\iterativas\02_tabla_multiplicar.py
python src\funciones\03_es_par.py
```

Tambien puedes usar `py` en lugar de `python`.

## Ejercicios incluidos

### Condicionales

- `01_clasificar_edad.py`: clasifica la etapa de un participante.
- `02_numero_mayor.py`: compara la duracion de dos sesiones de estudio.
- `03_calificacion.py`: interpreta el porcentaje de avance de una actividad.

### Iterativas

- `01_contador_while.py`: registra sesiones hasta completar una meta con `while`.
- `02_tabla_multiplicar.py`: calcula puntos acumulados con `for`.
- `03_suma_pares.py`: suma los puntos de actividades con numero par.

### Funciones

- `01_saludar.py`: prepara una bienvenida personalizada para el aprendiz.
- `02_area_rectangulo.py`: calcula el espacio de una mesa de estudio.
- `03_es_par.py`: identifica si el numero de una actividad es par.

## Conceptos aplicados

- Condiciones `if`, `elif` y `else`.
- Operadores de comparacion y operador modulo (`%`).
- Ciclos `while` y `for`.
- Funciones con parametros, valores de retorno y llamadas.
- Entrada de datos con `input()` y conversion con `int()` y `float()`.

## Pruebas realizadas

Se verifico cada programa desde la terminal. Como minimo, se usaron estos casos:

| Archivo                               | Entrada de ejemplo | Resultado esperado             |
| ------------------------------------- | ------------------ | ------------------------------ |
| `condicionales/01_clasificar_edad.py` | `20`               | Participante mayor de edad     |
| `condicionales/02_numero_mayor.py`    | `90` y `45`        | La sesion 1 tuvo mas tiempo    |
| `condicionales/03_calificacion.py`    | `85`               | Avance esperado                |
| `iterativas/01_contador_while.py`     | No requiere        | Registra la sesion 5           |
| `iterativas/02_tabla_multiplicar.py`  | `10`               | Sesion 5: 50 puntos acumulados |
| `iterativas/03_suma_pares.py`         | No requiere        | Puntos acumulados: 30          |
| `funciones/01_saludar.py`             | `Ana`              | Bienvenida personalizada       |
| `funciones/02_area_rectangulo.py`     | `120` y `60`       | Area igual a 7200 cm2          |
| `funciones/03_es_par.py`              | `12`               | Actividad con numero par       |

Tambien conviene repetir las pruebas con valores limite: edad negativa, sesiones con la misma duracion, porcentajes `0`, `60`, `70`, `90`, `100` y `120`, y una meta de cero sesiones.

Las pruebas de la logica se pueden ejecutar sin introducir datos manualmente:

```powershell
python -m unittest discover -s tests -v
```

## Proceso de elaboracion

1. Elegi un contexto cercano a la actividad: organizar mi avance en el curso mediante una bitacora de estudio.
2. Relacione cada concepto de la leccion con una situacion del contexto: `if` para clasificar, `while` para registrar sesiones, `for` para acumular puntos y funciones para reutilizar calculos.
3. Separe cada ejercicio en una funcion y un `main`, de modo que la logica pueda probarse sin depender de `input()`.
4. Defini casos normales y limites, y los converti en pruebas automatizadas dentro de `tests/test_ejercicios.py`.
5. Ejecute los scripts, revise los resultados y registre los cambios en Git con mensajes descriptivos.

Esta bitacora explica las decisiones de esta entrega y permite distinguirla de una copia de ejercicios genericos.

## Versionamiento con Git

Desde la carpeta del proyecto:

```powershell
git init
git add .
git commit -m "Desarrolla ejercicios de control y funciones"
git branch -M main
git remote add origin https://github.com/Pafuna08/fundamentos_python_control_fun.git
git push -u origin main
```

El repositorio publico de esta entrega es https://github.com/Pafuna08/fundamentos_python_control_fun. Para evidenciar el proceso, conserva los commits y comparte ese enlace junto con esta estructura.

## Lista de entrega

- [x] La carpeta `src` contiene `condicionales`, `iterativas` y `funciones`.
- [x] Los nueve scripts se ejecutan con Python 3.
- [x] Cada ejercicio tiene docstring y codigo organizado.
- [x] Se probaron casos normales y casos limite.
- [x] El README explica la ejecucion y el versionamiento.
- [x] El proyecto esta publicado en un repositorio publico.
