import tkinter as tk
from tkinter import ttk, messagebox
from servicios.garaje_servicio import GarajeServicio
from modelos.vehiculo import Vehiculo


class GarajeApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Gestión de Garaje")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.servicio = GarajeServicio()

        self._crear_interfaz()

    def _crear_interfaz(self):
        # Título
        tk.Label(self.root, text="Gestión de Vehículos - Garaje", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Frame del formulario
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10, padx=20, fill="x")

        # Campos de entrada
        labels = ["Placa:", "Marca:", "Propietario:"]
        self.entries = {}

        for i, texto in enumerate(labels):
            tk.Label(frame_form, text=texto).grid(row=i, column=0, padx=10, pady=8, sticky="e")
            entry = tk.Entry(frame_form, width=35, font=("Arial", 11))
            entry.grid(row=i, column=1, padx=10, pady=8, sticky="w")
            self.entries[texto.lower().replace(":", "")] = entry

        # Botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=15)

        tk.Button(frame_botones, text="Agregar Vehículo", command=self.agregar_vehiculo,
                  width=18, font=("Arial", 11), bg="#4CAF50", fg="white").pack(side="left", padx=10)

        tk.Button(frame_botones, text="Limpiar Formulario", command=self.limpiar_formulario,
                  width=18, font=("Arial", 11)).pack(side="left", padx=10)

        tk.Button(frame_botones, text="Limpiar Todo", command=self.limpiar_todo,
                  width=18, font=("Arial", 11), bg="#f44336", fg="white").pack(side="left", padx=10)

        # Tabla
        self._crear_tabla()

    def _crear_tabla(self):
        columns = ("placa", "marca", "propietario")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=12)

        self.tree.heading("placa", text="Placa")
        self.tree.heading("marca", text="Marca")
        self.tree.heading("propietario", text="Propietario")

        self.tree.column("placa", width=120, anchor="center")
        self.tree.column("marca", width=180)
        self.tree.column("propietario", width=280)

        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

    def agregar_vehiculo(self):
        placa = self.entries["placa"].get()
        marca = self.entries["marca"].get()
        propietario = self.entries["propietario"].get()

        exito, mensaje = self.servicio.agregar_vehiculo(placa, marca, propietario)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_tabla()
            self.limpiar_formulario()
        else:
            messagebox.showwarning("Atención", mensaje)

    def actualizar_tabla(self):
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Llenar tabla
        for vehiculo in self.servicio.obtener_todos():
            self.tree.insert("", "end", values=(vehiculo.placa, vehiculo.marca, vehiculo.propietario))

    def limpiar_formulario(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def limpiar_todo(self):
        if messagebox.askyesno("Confirmar", "¿Realmente desea eliminar TODOS los vehículos registrados?"):
            self.servicio.limpiar()
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "Lista de vehículos limpiada")