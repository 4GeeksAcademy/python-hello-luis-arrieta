import os
import unittest
import app


class TestTodoListCLI(unittest.TestCase):

    def setUp(self):
        """Prepara un entorno de pruebas limpio antes de cada test."""
        app.todos.clear()
        self.test_filename = "test_todos.csv"
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def tearDown(self):
        """Limpia archivos temporales creados por las pruebas."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_one_task(self):
        """Verifica que add_one_task agrega tareas correctamente a la lista en memoria."""
        result = app.add_one_task("Comprar leche")
        self.assertTrue(result)
        self.assertEqual(len(app.todos), 1)
        self.assertEqual(app.todos[0], "Comprar leche")

    def test_add_multiple_tasks(self):
        """Verifica que se pueden agregar múltiples tareas conservando el orden."""
        app.add_one_task("Tarea 1")
        app.add_one_task("Tarea 2")
        app.add_one_task("Tarea 3")
        self.assertEqual(app.todos, ["Tarea 1", "Tarea 2", "Tarea 3"])

    def test_add_empty_task(self):
        """Verifica que no se agreguen tareas vacías."""
        result = app.add_one_task("   ")
        self.assertFalse(result)
        self.assertEqual(len(app.todos), 0)

    def test_delete_task_valid_position(self):
        """Verifica la eliminación de una tarea por posición (1-based index)."""
        app.add_one_task("Primera")
        app.add_one_task("Segunda")
        deleted = app.delete_task(1)
        self.assertEqual(deleted, "Primera")
        self.assertEqual(app.todos, ["Segunda"])

    def test_delete_task_invalid_position(self):
        """Verifica el comportamiento al intentar eliminar un índice fuera de rango."""
        app.add_one_task("Única")
        deleted = app.delete_task(99)
        self.assertIsNone(deleted)
        self.assertEqual(len(app.todos), 1)

    def test_save_and_load_todos(self):
        """Verifica la persistencia guardando y cargando desde CSV."""
        app.add_one_task("Tarea Guardada 1")
        app.add_one_task("Tarea Guardada 2")
        
        save_success = app.save_todos(self.test_filename)
        self.assertTrue(save_success)
        self.assertTrue(os.path.exists(self.test_filename))

        # Limpiar memoria e intentar cargar desde el archivo guardado
        app.todos.clear()
        self.assertEqual(len(app.todos), 0)

        load_success = app.load_todos(self.test_filename)
        self.assertTrue(load_success)
        self.assertEqual(app.todos, ["Tarea Guardada 1", "Tarea Guardada 2"])

    def test_load_non_existent_file(self):
        """Verifica que al cargar un archivo inexistente la aplicación no falle."""
        load_success = app.load_todos("archivo_inexistente_999.csv")
        self.assertFalse(load_success)
        self.assertEqual(len(app.todos), 0)


if __name__ == "__main__":
    unittest.main()
