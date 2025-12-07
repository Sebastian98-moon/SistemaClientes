Sistema de Gestión de Clientes (Python + SQLite)

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar clientes utilizando una base de datos SQLite.

Funcionalidades:

✔ Agregar clientes
✔ Listar todos los clientes
✔ Buscar un cliente por nombre
✔ Eliminar clientes por ID
✔ Validaciones de datos (nombre, apellido, correo)
✔ Conexión persistente con base de datos SQLite

=====================================

Estructura del proyecto

SistemaClientes/
│── src/
│    └── clientes.py           # Código principal
│
│── database/
│    └── Clientes.db           # Base de datos SQLite
│
│── .gitignore
│── README.md

====================================

Tecnologías utilizadas:

-Python 3

-SQLite3

-Manejo de excepciones (try / except)

-Estructuras de control y funciones

=====================================

Funcionamiento del menú principal
1️⃣ Agregar clientes

Pide nombre, apellido y correo.
Valida que:

No estén vacíos

El correo tenga un solo "@"

2️⃣ Ver clientes

Muestra toda la tabla Clientes.

3️⃣ Buscar cliente por nombre

Busca coincidencias exactas en la base de datos.

4️⃣ Eliminar cliente por ID

El usuario elige un ID existente y lo elimina de la DB.

=====================================

Autor

Sebastián Luna

GitHub:
🔗 https://github.com/Sebastian98-moon