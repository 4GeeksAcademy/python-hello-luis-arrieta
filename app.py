import csv
import os

# Lista activa de tareas en memoria
todos = []


def add_one_task(title):
    """
    Agrega una nueva tarea a la lista activa en memoria.
    """
    clean_title = str(title).strip()
    if clean_title:
        todos.append(clean_title)
        return True
    return False


def print_list():
    """
    Muestra todas las tareas pendientes con sus posiciones numéricas.
    """
    if not todos:
        print("No hay tareas pendientes.")
        return

    for index, task in enumerate(todos, start=1):
        print(f"{index}. {task}")


def delete_task(number_to_delete):
    """
    Elimina la tarea indicada por su posición en la lista (1-based index).
    """
    try:
        index = int(number_to_delete)
        if 1 <= index <= len(todos):
            deleted_task = todos.pop(index - 1)
            return deleted_task
        else:
            print(f"Error: La posición {number_to_delete} no existe en la lista.")
            return None
    except (ValueError, TypeError):
        print("Error: Debes ingresar un número entero válido.")
        return None


FILENAME = "todos.csv"


def save_todos(filename=FILENAME):
    """
    Persiste las tareas actuales en el archivo todos.csv.
    """
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for task in todos:
                writer.writerow([task])
        print(f"Tareas guardadas exitosamente en '{filename}'.")
        return True
    except Exception as e:
        print(f"Error al guardar las tareas: {e}")
        return False


def load_todos(filename=FILENAME):
    """
    Lee todos.csv y reconstruye la lista de tareas en memoria.
    """
    if not os.path.exists(filename):
        print(f"El archivo '{filename}' no existe todavía. Se iniciará con una lista vacía.")
        return False

    try:
        todos.clear()
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Ignorar filas vacías
                    todos.append(row[0])
        print(f"Tareas cargadas exitosamente desde '{filename}'.")
        return True
    except Exception as e:
        print(f"Error al cargar las tareas: {e}")
        return False


def main():
    """
    Punto de entrada principal para ejecutar la aplicación CLI.
    """
    print("Todo List CLI iniciada.")


if __name__ == "__main__":
    main()
