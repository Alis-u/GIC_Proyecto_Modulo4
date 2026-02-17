from src.cliente import Cliente, ClienteRegular
from src.excepciones import ExcepcionCliente
from src.logger import LoggerSistema
from src.gestor_clientes import GestorClientes


logger = LoggerSistema()

try:
    # Cliente normal
    cliente1 = Cliente(1, "Ana", "ana@email.com", "123456789", "Chile")
    print(cliente1.mostrar_info())
    logger.registrar_evento("Cliente creado correctamente")

    # Cliente con error
    cliente2 = Cliente(2, "Pedro", "correo_malo", "123", "Chile")

except ExcepcionCliente as e:
    print("Error detectado:", e)
    logger.registrar_error(str(e))


# Cliente con herencia
cliente_regular = ClienteRegular(
    3, "Lucía", "lucia@email.com", "987654321", "Chile", 150
)

print(cliente_regular.mostrar_info())
print("Descuento:", cliente_regular.calcular_descuento())


# GestorClientes
gestor = GestorClientes()

gestor.agregar_cliente(cliente1)

print("\n--- Editando cliente ---")
gestor.editar_cliente(1, nuevo_email="nuevo@email.com")

print("\nClientes después de editar:")
gestor.mostrar_clientes()

print("\n--- Eliminando cliente ---")
gestor.eliminar_cliente(1)

print("\nClientes después de eliminar:")
gestor.mostrar_clientes()
