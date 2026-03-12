# Gestión de Garaje con Tkinter

Aplicación de escritorio sencilla para registrar y visualizar vehículos en un garaje.  
Desarrollada como proyecto académico utilizando arquitectura básica MVC-ish con Python y Tkinter.

## Características principales

- Registro de vehículos con placa, marca y propietario
- Validación básica de datos (campos obligatorios + duplicados de placa)
- Visualización en tabla (Treeview)
- Botón para limpiar el formulario
- Botón para limpiar toda la lista (con confirmación)
- Interfaz limpia y responsive dentro de ventana fija

## Tecnologías utilizadas

- **Tkinter** (biblioteca estándar de interfaces gráficas)
- Arquitectura modular:
  - Modelos (clase Vehículo)
  - Servicios (lógica de negocio)
  - UI (interfaz gráfica)

## Estructura del proyecto

garaje_app/
├── main.py                 # Punto de entrada de la aplicación
│
├── modelos/
│   └── vehiculo.py         # Clase Vehiculo
│
├── servicios/
│   └── garaje_servicio.py  # Lógica de gestión de vehículos
│
└── ui/
└── app_tkinter.py      # Interfaz gráfica con Tkinter

