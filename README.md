📌 README.md - Sistema de Gestión de Biblioteca
(Ejemplo de cómo documentarlo)

📌 Descripción del Proyecto
Este es un Sistema de Gestión de Biblioteca implementado con el patrón de diseño MVC (Modelo-Vista-Controlador).
Permite gestionar usuarios y realizar operaciones en una base de datos a través de una interfaz gráfica (PyQt5) conectada con un servidor Flask.

📌 Tecnologías utilizadas
El proyecto sigue la arquitectura MVC, separando la lógica de negocio, la interfaz gráfica y el control de flujo:

Capa	Tecnología Usada	Descripción
Modelo (M)	Flask-SQLAlchemy	Se encarga de la gestión de la base de datos (SQLite), definiendo las clases Usuario, Libro, etc.
Vista (V)	PyQt5	Interfaz gráfica que muestra y gestiona los datos en tiempo real.
Controlador (C)	Flask (Blueprints)	API REST que maneja las peticiones de la interfaz gráfica hacia la base de datos.
📌 Estructura del Proyecto
bash
Copiar
Editar
/biblioteca_mvc
│── /modelo                 # 📌 MODELO (Base de datos con SQLAlchemy)
│    ├── base_datos.py      # Conexión a la BD
│    ├── usuario.py         # Modelo Usuario
│    ├── libro.py           # Modelo Libro
│── /controlador            # 📌 CONTROLADOR (API Flask)
│    ├── controlador_usuarios.py   # Endpoints para gestionar usuarios
│── /vista                  # 📌 VISTA (Interfaz gráfica PyQt5)
│    ├── interfaz.py        # Ventana principal con PyQt5
│── app.py                  # Punto de entrada del servidor Flask
│── README.md               # Documentación del proyecto
│── requirements.txt        # Librerías necesarias
📌 Instalación y Ejecución
1️⃣ Clonar el repositorio
bash
Copiar
Editar
git clone https://github.com/TU-USUARIO/biblioteca_mvc.git
cd biblioteca_mvc
2️⃣ Crear un entorno virtual e instalar dependencias
bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
3️⃣ Iniciar el servidor Flask
bash
Copiar
Editar
python app.py
💡 Si todo está bien, Flask correrá en http://127.0.0.1:5001/.

4️⃣ Ejecutar la interfaz gráfica
En otra terminal, ejecuta:

bash
Copiar
Editar
python interfaz.py
✅ Esto abrirá la aplicación de escritorio para gestionar usuarios.

📌 Funcionalidades
✔ Listar usuarios registrados en la base de datos.
✔ Agregar usuarios desde la interfaz gráfica.
✔ Eliminar usuarios desde la tabla en la interfaz.
✔ Actualizar usuarios en la base de datos.
