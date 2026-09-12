"""Pruebas de la bitacora de seguimiento academico."""

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


def cargar_modulo(ruta_relativa, nombre):
    """Carga un script cuyo nombre comienza con un numero."""
    ruta = ROOT / ruta_relativa
    especificacion = importlib.util.spec_from_file_location(nombre, ruta)
    modulo = importlib.util.module_from_spec(especificacion)
    especificacion.loader.exec_module(modulo)
    return modulo


clasificacion_edad = cargar_modulo(
    "src/condicionales/01_clasificar_edad.py", "clasificacion_edad"
)
sesiones = cargar_modulo(
    "src/condicionales/02_numero_mayor.py", "sesiones"
)
avance = cargar_modulo(
    "src/condicionales/03_calificacion.py", "avance"
)
registro = cargar_modulo("src/iterativas/01_contador_while.py", "registro")
plan = cargar_modulo("src/iterativas/02_tabla_multiplicar.py", "plan")
puntos = cargar_modulo("src/iterativas/03_suma_pares.py", "puntos")
bienvenida = cargar_modulo("src/funciones/01_saludar.py", "bienvenida")
mesa = cargar_modulo("src/funciones/02_area_rectangulo.py", "mesa")
actividades = cargar_modulo("src/funciones/03_es_par.py", "actividades")


class TestBitacoraAcademica(unittest.TestCase):
    """Comprueba la logica principal de cada bloque de ejercicios."""

    def test_condicionales(self):
        self.assertEqual(
            clasificacion_edad.clasificar_participante(17),
            "Participante menor de edad",
        )
        self.assertIn("sesion 1", sesiones.comparar_sesiones(90, 45))
        self.assertEqual(avance.interpretar_resultado(85), "Avance esperado")
        self.assertEqual(avance.interpretar_resultado(120), "El porcentaje debe estar entre 0 y 100.")

    def test_iterativas(self):
        self.assertEqual(registro.registrar_sesiones(3), [1, 2, 3])
        self.assertEqual(len(plan.generar_plan_puntos(10)), 5)
        self.assertEqual(puntos.sumar_puntos_pares(2, 10), ([2, 4, 6, 8, 10], 30))

    def test_funciones(self):
        self.assertIn("Ana", bienvenida.preparar_bienvenida("Ana"))
        self.assertEqual(mesa.calcular_area_mesa(120, 60), 7200)
        self.assertTrue(actividades.es_actividad_par(12))
        self.assertFalse(actividades.es_actividad_par(13))


if __name__ == "__main__":
    unittest.main()
