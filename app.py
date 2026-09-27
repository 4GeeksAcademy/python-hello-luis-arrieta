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


def save_todos():
    """
    Persiste las tareas actuales en el archivo todos.csv.
    """
    pass


def load_todos():
    """
    Lee todos.csv y reconstruye la lista de tareas en memoria.
    """
    pass


def main():
    """
    Punto de entrada principal para ejecutar la aplicación CLI.
    """
    print("Todo List CLI iniciada.")


if __name__ == "__main__":
    main()
