from src.persistencia import guardar_cliente, cargar_clientes


class GestorClientes:

    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        guardar_cliente(cliente)
        print("Cliente agregado y guardado correctamente")

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente.mostrar_info())

    def cargar_clientes_desde_txt(self):
        datos = cargar_clientes()
        print("\nClientes cargados desde archivo:")
        for d in datos:
            print(d)

    def eliminar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                self.clientes.remove(cliente)
                print("Cliente eliminado correctamente")
                return
        print("Cliente no encontrado")

    def editar_cliente(self, id_cliente, nuevo_email=None, nuevo_telefono=None):
        for cliente in self.clientes:
            if cliente.id == id_cliente:

                if nuevo_email:
                    cliente.email = nuevo_email

                if nuevo_telefono:
                    cliente.telefono = nuevo_telefono

                print("Cliente actualizado correctamente")
                return

        print("Cliente no encontrado")
