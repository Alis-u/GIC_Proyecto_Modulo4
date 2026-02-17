def guardar_cliente(cliente):
    with open("clientes.txt", "a", encoding="utf-8") as f:
        f.write(cliente.mostrar_info() + "\n")
def cargar_clientes():
    clientes = []

    try:
        with open("clientes.txt", "r", encoding="utf-8") as f:
            for linea in f:
                clientes.append(linea.strip())

    except FileNotFoundError:
        print("No existe archivo de clientes todavía.")

    return clientes
