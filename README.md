# Sistema de Gestión de Clientes – Documentación de Funcionamiento

## Descripción general

Este proyecto consiste en un sistema básico de gestión de clientes desarrollado en Python, utilizando Programación Orientada a Objetos (POO).
Su finalidad es permitir el registro, almacenamiento, edición y eliminación de clientes, además de aplicar validaciones y manejo de archivos.

El sistema funciona desde consola y simula la administración simple de clientes dentro de una aplicación.

---

## ¿Cómo funciona el sistema?

El programa está dividido en módulos para mantener el código ordenado y facilitar su mantenimiento:

### 1. Clase Cliente

Representa a cada cliente individual.
Incluye información como:

* ID del cliente
* Nombre
* Email
* Teléfono
* País (según implementación)

También contiene métodos para mostrar la información del cliente de forma clara.

---

### 2. Validación de datos

Se incorporan validaciones básicas, principalmente en el email:

* Verifica formato correcto
* Si el email no es válido, el sistema muestra un mensaje de error
* Permite controlar la calidad de los datos ingresados

Esto ayuda a evitar registros incorrectos.

---

### 3. Gestor de clientes

Esta parte administra todos los clientes registrados.
Permite realizar las operaciones principales:

#### ➜ Agregar cliente

* Se crea un objeto cliente
* Se valida la información
* Se guarda en memoria y en archivo TXT

#### ➜ Mostrar clientes

* Lista los clientes almacenados
* Puede mostrar clientes en memoria o desde archivo

#### ➜ Editar cliente

* Permite modificar datos existentes (ejemplo: email o teléfono)
* Actualiza la información guardada

#### ➜ Eliminar cliente

* Busca al cliente por ID
* Lo elimina de memoria y archivo

---

### 4. Persistencia de datos (archivo TXT)

El sistema guarda automáticamente los clientes en un archivo de texto.
Esto permite:

* Mantener la información aunque se cierre el programa
* Recuperar clientes previamente registrados
* Simular una base de datos simple

---

## Ejecución del programa

Para ejecutar el sistema, se debe abrir la terminal en la carpeta del proyecto y ejecutar:

```bash
python -m src.main
```

El archivo principal (`main.py`) contiene ejemplos de uso del sistema y pruebas de funcionamiento.

---

##  funcionamiento esperados

Al ejecutar el programa se pueden observar:

* Creación de cliente correctamente
* Mensaje de error si el email es inválido
* Visualización de clientes guardados
* Edición de datos existentes
* Eliminación de registros
* Guardado automático en archivo TXT

