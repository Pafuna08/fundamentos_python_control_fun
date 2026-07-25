# Fundamentos de Python: control y funciones

Proyecto individual para la evidencia **GA1-220501093-04-AA1-EV02**.

Este repositorio reune ejercicios sobre estructuras condicionales, estructuras iterativas y funciones en Python. Todos los programas se ejecutan con Python 3.

## Estructura

```text
fundamentos_python_control_fun/
|-- README.md
`-- src/
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

- `01_clasificar_edad.py`: clasifica una edad como menor o mayor de edad.
- `02_numero_mayor.py`: compara dos numeros y determina cual es mayor o si son iguales.
- `03_calificacion.py`: asigna un desempeno segun un valor entre 0 y 100.

### Iterativas

- `01_contador_while.py`: cuenta del 1 al 5 con un ciclo `while`.
- `02_tabla_multiplicar.py`: genera una tabla de multiplicar con `for`.
- `03_suma_pares.py`: suma los numeros pares del 2 al 10.

### Funciones

- `01_saludar.py`: define y llama una funcion que recibe un nombre.
- `02_area_rectangulo.py`: calcula y devuelve el area de un rectangulo.
- `03_es_par.py`: devuelve `True` o `False` para indicar si un numero es par.

## Conceptos aplicados

- Condiciones `if`, `elif` y `else`.
- Operadores de comparacion y operador modulo (`%`).
- Ciclos `while` y `for`.
- Funciones con parametros, valores de retorno y llamadas.
- Entrada de datos con `input()` y conversion con `int()` y `float()`.
