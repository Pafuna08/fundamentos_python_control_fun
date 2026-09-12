# Fundamentos de Python: estructuras de control y funciones

Proyecto individual para la evidencia **GA1-220501093-04-AA1-EV02**. El objetivo es practicar variables, literales, operadores aritmeticos, comparaciones, cadenas, estructuras condicionales, ciclos y funciones mediante ejercicios pequenos y faciles de verificar.

Cada archivo fue organizado para poder ejecutarse directamente o importarse como modulo. Las funciones separan la logica del programa de la entrada y salida de datos, lo que facilita las pruebas.

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

## Pruebas realizadas

Se debe comprobar cada programa desde la terminal. Como minimo, usa estos casos:

| Archivo                               | Entrada de ejemplo | Resultado esperado          |
| ------------------------------------- | ------------------ | --------------------------- |
| `condicionales/01_clasificar_edad.py` | `20`               | Mayor de edad               |
| `condicionales/02_numero_mayor.py`    | `8` y `3`          | El mayor es 8               |
| `condicionales/03_calificacion.py`    | `85`               | Desempeno alto              |
| `iterativas/01_contador_while.py`     | No requiere        | Cuenta del 1 al 5           |
| `iterativas/02_tabla_multiplicar.py`  | `7`                | Tabla del 7 del 1 al 10     |
| `iterativas/03_suma_pares.py`         | No requiere        | Pares del 2 al 10 y suma 30 |
| `funciones/01_saludar.py`             | `Ana`              | Saludo personalizado        |
| `funciones/02_area_rectangulo.py`     | `5` y `3`          | Area igual a 15             |
| `funciones/03_es_par.py`              | `12`               | Indica que es par           |

Tambien conviene repetir las pruebas de condicionales con valores limite: edad `0`, calificacion `0`, `60`, `70`, `90` y `100`, y dos numeros iguales.

## Versionamiento con Git

Desde la carpeta del proyecto:

```powershell
git init
git add .
git commit -m "Desarrolla ejercicios de control y funciones"
git branch -M main
git remote add origin https://github.com/USUARIO/fundamentos_python_control_fun.git
git push -u origin main
```

Reemplaza `USUARIO` por tu cuenta y crea previamente el repositorio publico en GitHub o GitLab. Para evidenciar el proceso, conserva los commits y comparte el enlace del repositorio junto con esta estructura.

## Lista de entrega

- [ ] La carpeta `src` contiene `condicionales`, `iterativas` y `funciones`.
- [ ] Los nueve scripts se ejecutan con Python 3.
- [ ] Cada ejercicio tiene docstring y codigo organizado.
- [ ] Se probaron casos normales y casos limite.
- [ ] El README explica la ejecucion y el versionamiento.
- [ ] El proyecto esta publicado en un repositorio publico.
