import re
from src.excepciones import ExcepcionCliente

class Cliente:

    def __init__(self, id, nombre, email, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion

        # atributos encapsulados
        self._email = None
        self._telefono = None

        # setters para validar desde el inicio
        self.set_email(email)
        self.set_telefono(telefono)

    # ===== VALIDACIÓN EMAIL =====
    def set_email(self, email):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(patron, email):
            self._email = email
        else:
            raise ExcepcionCliente("Email inválido")

    def get_email(self):
        return self._email

    # ===== VALIDACIÓN TELÉFONO =====
    def set_telefono(self, telefono):
        if telefono.isdigit() and len(telefono) >= 8:
            self._telefono = telefono
        else:
            raise ExcepcionCliente("Teléfono inválido")

    def get_telefono(self):
        return self._telefono

    # ===== MOSTRAR INFO =====
    def mostrar_info(self):
        return f"Cliente: {self.nombre} | Email: {self._email} | Teléfono: {self._telefono}"

class ClienteRegular(Cliente):
    def __init__(self, id, nombre, email, telefono, direccion, puntos):
        super().__init__(id, nombre, email, telefono, direccion)
        self.puntos = puntos

    def calcular_descuento(self):
        return self.puntos * 0.01
