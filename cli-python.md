# Todo List CLI con Python — Instrucciones auditadas

> Documento de trabajo preparado a partir del README oficial del proyecto de 4Geeks Academy **Todo List CLI con Python**.
>
> **Repositorio oficial de la plantilla:** https://github.com/breatheco-de/exercise-todo-list-cli-python
>
> **README auditado:** https://github.com/breatheco-de/exercise-todo-list-cli-python/blob/master/README.es.md
>
> **Asset del catálogo 4Geeks:** `todo-list-cli-python-es` — proyecto `Todo List CLI con Python` — nivel principiante — ID `293`.

## 1. Contexto del proyecto

Te has unido al equipo de herramientas internas de una pequeña empresa de logística. Los coordinadores operativos anotan tareas pendientes entre mensajes de chat y notas sueltas, lo que provoca que se pierdan seguimientos importantes entre turnos.

El objetivo es construir una herramienta ligera de terminal que permita gestionar tareas desde la línea de comandos y conservarlas entre ejecuciones mediante un archivo local.

## 2. Brief funcional

La primera versión debe permitir:

- Agregar una nueva tarea mediante su título.
- Mostrar todas las tareas pendientes con una posición numérica.
- Eliminar una tarea indicando su posición en la lista.
- Guardar las tareas en un archivo local llamado `todos.csv`.
- Cargar nuevamente las tareas desde `todos.csv`.
- Mantener las tareas disponibles aunque se cierre y vuelva a abrir la terminal.

La edición de tareas no forma parte de esta versión. Si una tarea necesita cambiarse, el flujo esperado es eliminarla y crearla de nuevo.

## 3. Cómo iniciar el proyecto

Puedes trabajar con GitHub Codespaces o en local.

### Opción recomendada: Codespaces

Abrir:

```text
https://github.com/codespaces/new/?repo=4GeeksAcademy/python-hello
```

### Opción local

Clonar la plantilla:

```bash
git clone https://github.com/4GeeksAcademy/python-hello
cd python-hello
```

Comprobar que Python está disponible y ejecutar la aplicación inicial:

```bash
python3 app.py
```

Ejecutar las pruebas disponibles:

```bash
python3 test.py
```

Para entregar, crear un repositorio propio en GitHub y actualizar el remoto:

```bash
git remote set-url origin <tu-nueva-url>
```

## 4. Qué debes hacer

### 4.1 Funciones obligatorias

Implementa las siguientes funciones respetando sus responsabilidades:

- [ ] `add_one_task(title)`
  - Agrega una nueva tarea a la lista activa en memoria.
  - Debe utilizar el título recibido.
  - Debe permitir agregar varias tareas durante la misma ejecución.

- [ ] `print_list()`
  - Muestra todas las tareas pendientes.
  - Debe conservar el orden de la lista.
  - Debe mostrar posiciones numéricas claras para que el usuario pueda seleccionar una tarea.

- [ ] `delete_task(number_to_delete)`
  - Elimina la tarea indicada por su posición.
  - Debe actualizar correctamente la lista después de eliminarla.
  - La posición mostrada al usuario debe corresponder con la posición utilizada por la función.

- [ ] `save_todos()`
  - Persiste las tareas actuales en `todos.csv`.
  - El formato guardado debe poder reutilizarse posteriormente.

- [ ] `load_todos()`
  - Lee `todos.csv`.
  - Reconstruye en memoria las tareas guardadas.
  - Debe permitir continuar trabajando con las tareas después de cargar el archivo.

### 4.2 Flujo de línea de comandos

La experiencia completa debe funcionar desde la terminal e incluir, como mínimo, un flujo coherente para:

1. Crear o agregar tareas.
2. Listar las tareas con sus posiciones.
3. Eliminar una tarea usando su posición.
4. Guardar las tareas en `todos.csv`.
5. Cargar las tareas desde `todos.csv`.
6. Repetir la operación de agregar tantas veces como sea necesario en una misma ejecución.

La interfaz debe comportarse de forma consistente y coincidir con la referencia visual proporcionada por el proyecto.

### 4.3 Restricción técnica

En esta versión utiliza únicamente herramientas de la biblioteca estándar de Python para:

- Entrada y salida de archivos.
- Lectura y escritura de `todos.csv`.
- Manejo de la interfaz de línea de comandos.

No añadas dependencias externas para resolver funciones que Python estándar ya permite implementar.

## 5. Qué vamos a evaluar

### 5.1 Gestión en memoria

- [ ] `add_one_task(title)` agrega correctamente nuevas tareas a la lista activa.
- [ ] Se pueden agregar múltiples tareas sin reiniciar la aplicación.
- [ ] `print_list()` muestra las tareas en el orden correcto.
- [ ] Cada tarea tiene una posición numérica clara y utilizable.
- [ ] `delete_task(number_to_delete)` elimina exactamente la tarea seleccionada.
- [ ] La lista queda actualizada después de una eliminación.

### 5.2 Persistencia

- [ ] `save_todos()` guarda las tareas actuales en `todos.csv`.
- [ ] El contenido de `todos.csv` utiliza un formato reutilizable.
- [ ] `load_todos()` lee correctamente el archivo.
- [ ] Las tareas cargadas reconstruyen el estado de la lista en memoria.
- [ ] El estado se conserva al cerrar y volver a abrir la aplicación.

### 5.3 Flujo CLI

- [ ] El flujo de crear, listar, eliminar, guardar y cargar funciona de forma consistente.
- [ ] La aplicación se puede utilizar completamente desde la terminal.
- [ ] La salida muestra información suficiente para que el usuario sepa qué hacer.
- [ ] Las posiciones que se muestran al usuario son las que espera `delete_task()`.
- [ ] El comportamiento coincide con la referencia visual del ejercicio.

### 5.4 Alcance y simplicidad

- [ ] Se respeta el alcance de esta primera versión.
- [ ] No se implementa edición de tareas en sitio, porque está fuera del alcance.
- [ ] No se introducen frameworks ni librerías externas innecesarias.
- [ ] La solución mantiene una estructura comprensible para un proyecto principiante.

## 6. Casos que conviene verificar manualmente

Antes de entregar, comprueba al menos estos escenarios:

1. Iniciar la aplicación sin tareas.
2. Agregar una tarea.
3. Agregar varias tareas consecutivas.
4. Listar las tareas y verificar sus posiciones.
5. Eliminar la primera tarea.
6. Eliminar una tarea intermedia.
7. Eliminar la última tarea.
8. Guardar una lista con varias tareas.
9. Cerrar y volver a iniciar la aplicación.
10. Cargar las tareas guardadas.
11. Listar después de cargar y comprobar el orden.
12. Guardar de nuevo después de agregar o eliminar tareas.
13. Intentar cargar cuando todavía no existe `todos.csv` y comprobar que el fallo se maneja de forma comprensible, si el diseño del proyecto contempla ese caso.

## 7. Entrega

Sube la solución a un repositorio propio de GitHub y comparte la URL según las instrucciones del instructor.

Antes de entregar, verifica:

```bash
python3 test.py
```

También conviene comprobar el flujo completo ejecutando:

```bash
python3 app.py
```

## 8. Fuentes y auditoría

- README oficial en español: `README.es.md` del repositorio `breatheco-de/exercise-todo-list-cli-python`.
- Asset público del catálogo 4Geeks: `todo-list-cli-python-es`, ID `293`.
- Se priorizaron las secciones **Qué debes hacer** y **Qué vamos a evaluar**.
- El acceso autenticado a la cuenta de 4Geeks no pudo validarse durante la auditoría porque el token local respondió `401 Invalid or Inactive Token`. Por tanto, el contenido de este documento se contrastó con el README oficial público y el registro público del catálogo, no con el detalle privado de la cuenta.
