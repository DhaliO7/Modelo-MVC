import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox

class BibliotecaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Biblioteca")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        # Tabla para mostrar usuarios
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3)  # ID, Nombre, Email
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Email"])
        layout.addWidget(self.tabla)

        # Campos de entrada
        self.input_nombre = QLineEdit(self)
        self.input_nombre.setPlaceholderText("Nombre")
        layout.addWidget(self.input_nombre)

        self.input_email = QLineEdit(self)
        self.input_email.setPlaceholderText("Email")
        layout.addWidget(self.input_email)

        # Botones
        self.btn_cargar = QPushButton("Cargar Usuarios")
        self.btn_cargar.clicked.connect(self.cargar_usuarios)
        layout.addWidget(self.btn_cargar)

        self.btn_agregar = QPushButton("Agregar Usuario")
        self.btn_agregar.clicked.connect(self.agregar_usuario)
        layout.addWidget(self.btn_agregar)

        self.btn_eliminar = QPushButton("Eliminar Usuario Seleccionado")
        self.btn_eliminar.clicked.connect(self.eliminar_usuario)
        layout.addWidget(self.btn_eliminar)

        self.setLayout(layout)
        self.cargar_usuarios()  # Cargar usuarios al abrir la app

    def cargar_usuarios(self):
        """Obtiene la lista de usuarios desde Flask y la muestra en la tabla."""
        try:
            respuesta = requests.get("http://127.0.0.1:5001/usuarios")
            if respuesta.status_code == 200:
                usuarios = respuesta.json()
                self.tabla.setRowCount(len(usuarios))

                for fila, usuario in enumerate(usuarios):
                    self.tabla.setItem(fila, 0, QTableWidgetItem(str(usuario["id"])))
                    self.tabla.setItem(fila, 1, QTableWidgetItem(usuario["nombre"]))
                    self.tabla.setItem(fila, 2, QTableWidgetItem(usuario["email"]))
            else:
                QMessageBox.critical(self, "Error", "No se pudieron cargar los usuarios.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def agregar_usuario(self):
        """Agrega un nuevo usuario enviando un POST a Flask y muestra la respuesta."""
        nombre = self.input_nombre.text()
        email = self.input_email.text()

        if not nombre or not email:
            QMessageBox.warning(self, "Error", "Ingresa nombre y email.")
            return

        datos = {"nombre": nombre, "email": email}
        respuesta = requests.post("http://127.0.0.1:5001/usuarios", json=datos)

        if respuesta.status_code == 201:  # Código 201 indica éxito
            QMessageBox.information(self, "Éxito", "Usuario agregado correctamente.")
            self.input_nombre.clear()
            self.input_email.clear()
            self.cargar_usuarios()
        else:
            QMessageBox.critical(self, "Error", f"No se pudo agregar el usuario. Respuesta del servidor: {respuesta.text}")

    def eliminar_usuario(self):
        """Elimina un usuario seleccionado de la tabla y la BD."""
        fila = self.tabla.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Selecciona un usuario para eliminar.")
            return

        id_usuario = self.tabla.item(fila, 0).text()
        respuesta = requests.delete(f"http://127.0.0.1:5001/usuarios/{id_usuario}")

        if respuesta.status_code == 200:
            QMessageBox.information(self, "Éxito", "Usuario eliminado correctamente.")
            self.cargar_usuarios()
        else:
            QMessageBox.critical(self, "Error", "No se pudo eliminar el usuario.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = BibliotecaApp()
    ventana.show()
    sys.exit(app.exec_())
