# ==========================================================
# Tema: Creación de una Aplicación de Agenda Personal
# ==========================================================

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import calendar

# ==================== Funciones ====================

def abrir_datepicker(entry):
    """
    Crea un calendario emergente para seleccionar una fecha
    y ponerla en el Entry correspondiente.
    """
    def seleccionar_fecha():
        fecha_seleccionada = f"{year_var.get()}-{month_var.get():02d}-{day_var.get():02d}"
        entry.delete(0, tk.END)
        entry.insert(0, fecha_seleccionada)
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Seleccionar Fecha")
    top.geometry("250x200")

    # Variables para año, mes, día
    year_var = tk.IntVar(value=datetime.now().year)
    month_var = tk.IntVar(value=datetime.now().month)
    day_var = tk.IntVar(value=datetime.now().day)

    # Año
    tk.Label(top, text="Año:").pack()
    tk.Spinbox(top, from_=2000, to=2100, textvariable=year_var, width=5).pack()

    # Mes
    tk.Label(top, text="Mes:").pack()
    tk.Spinbox(top, from_=1, to=12, textvariable=month_var, width=3).pack()

    # Día
    tk.Label(top, text="Día:").pack()
    tk.Spinbox(top, from_=1, to=31, textvariable=day_var, width=3).pack()

    tk.Button(top, text="Seleccionar", command=seleccionar_fecha).pack(pady=10)

def agregar_evento():
    """
    Agrega un evento a la lista (TreeView) utilizando
    los valores ingresados en los campos de fecha, hora y descripción.
    """
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha == "" or hora == "" or descripcion == "":
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
        return

    tree.insert("", tk.END, values=(fecha, hora, descripcion))
    # Limpiar campos después de agregar
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

def eliminar_evento():
    """
    Elimina el evento seleccionado del TreeView.
    Muestra un diálogo de confirmación antes de eliminar.
    """
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Seleccionar evento", "Por favor, seleccione un evento para eliminar.")
        return
    confirm = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar este evento?")
    if confirm:
        tree.delete(selected_item)

def salir():
    """
    Cierra la aplicación.
    """
    root.destroy()

# ==================== Ventana Principal ====================

root = tk.Tk()
root.title("Agenda de Eventos")
root.geometry("600x500")

# ==================== Frames ====================

frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# ==================== TreeView ====================

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.column("Fecha", width=100)
tree.column("Hora", width=80)
tree.column("Descripción", width=300)
tree.pack()

# ==================== Campos de Entrada ====================

lbl_fecha = tk.Label(frame_entrada, text="Fecha (AAAA-MM-DD):")
lbl_fecha.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)
btn_fecha = tk.Button(frame_entrada, text="📅", command=lambda: abrir_datepicker(entry_fecha))
btn_fecha.grid(row=0, column=2, padx=5, pady=5)

lbl_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
lbl_hora.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

lbl_descripcion = tk.Label(frame_entrada, text="Descripción:")
lbl_descripcion.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_descripcion = tk.Entry(frame_entrada, width=40)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# ==================== Botones ====================

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=10)

# ==================== Ejecutar la Aplicación ====================

root.mainloop()
