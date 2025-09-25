# Aplicación GUI de lista de Tareas

import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
from datetime import datetime

class Task:
    """
    Clase que representa una tarea individual.
    Atributos:
        text (str): descripción de la tarea
        date (str): fecha asociada a la tarea (AAAA-MM-DD)
        completed (bool): indica si está completada
    """
    def __init__(self, text: str, date: str):
        self.text = text
        self.date = date
        self.completed = False

    def toggle(self):
        """Alterna el estado completado/no completado."""
        self.completed = not self.completed

    def __str__(self):
        """Representación textual de la tarea (fecha + descripción)."""
        return f"[{self.date}] {self.text}"


class TodoApp:
    """
    Clase principal de la aplicación To-Do.
    Encapsula la interfaz gráfica y la lógica de la aplicación.
    """
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Lista de Tareas - POO (Tkinter)")
        self.root.resizable(False, False)
        # Lista de tareas (modelo)
        self.tasks: list[Task] = []

        # Configuración de fuentes para tareas normales y completadas
        default_font = tkfont.nametofont("TkDefaultFont")
        self.font_normal = default_font
        self.font_completed = tkfont.Font(
            family=self.font_normal.actual("family"),
            size=self.font_normal.actual("size"),
            slant=self.font_normal.actual("slant"),
            weight=self.font_normal.actual("weight"),
            underline=0,
        )
        self.font_completed.configure(overstrike=1)  # tachado para tareas completadas

        # Construcción de la interfaz y eventos
        self._build_ui()
        self._bind_events()

    def _build_ui(self):
        """Construye la interfaz gráfica: fecha, entrada, botones y lista."""
        padding = 8

        # Frame superior con Date Entry (Entry + botón calendario), Entry tarea y botón "Añadir Tarea"
        top_frame = ttk.Frame(self.root, padding=padding)
        top_frame.grid(row=0, column=0, sticky="ew")

        # Campo de fecha (llenado por el datepicker tipo deber)
        self.date_var = tk.StringVar()
        self.date_entry = ttk.Entry(top_frame, textvariable=self.date_var, width=12)
        self.date_entry.grid(row=0, column=0, padx=(0, 6), pady=(0, 6))

        # Botón que abre el datepicker con Spinbox (igual que el deber)
        self.calendar_button = ttk.Button(top_frame, text="📅", width=3,
                                          command=lambda: self._open_datepicker(self.date_entry))
        self.calendar_button.grid(row=0, column=1, padx=(0, 6))

        # Campo de texto para la descripción de la tarea
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(top_frame, textvariable=self.entry_var)
        self.entry.grid(row=0, column=2, padx=(0, 6), pady=(0, 6), sticky="ew")
        top_frame.columnconfigure(2, weight=1)

        # Botón para añadir tarea
        self.add_button = ttk.Button(top_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=3, pady=(0, 6))

        # Frame central con Listbox y scrollbar
        list_frame = ttk.Frame(self.root, padding=padding)
        list_frame.grid(row=1, column=0, sticky="nsew")

        self.listbox = tk.Listbox(list_frame, height=12, activestyle="none", width=60)
        self.listbox.grid(row=0, column=0, sticky="nsew")
        list_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)

        self.scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.listbox.configure(yscrollcommand=self.scrollbar.set)

        # Frame inferior con botones "Marcar como Completada" y "Eliminar Tarea"
        bottom_frame = ttk.Frame(self.root, padding=padding)
        bottom_frame.grid(row=2, column=0, sticky="ew")

        self.complete_button = ttk.Button(bottom_frame, text="Marcar como Completada", command=self.mark_completed)
        self.complete_button.grid(row=0, column=0, padx=(0,6))

        self.delete_button = ttk.Button(bottom_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=1)

        # Mensaje de ayuda
        help_label = ttk.Label(self.root, text="Enter = Añadir. Doble clic = Alternar completada. Supr = Eliminar.")
        help_label.grid(row=3, column=0, pady=(4,8))

    def _bind_events(self):
        """Asigna eventos: Enter, doble clic en tarea, tecla Delete."""
        self.entry.bind("<Return>", self._on_enter_pressed)     # Enter en Entry
        self.listbox.bind("<Double-Button-1>", self._on_double_click)  # Doble clic en tarea
        self.root.bind("<Delete>", lambda e: self.delete_task())       # Tecla Supr/Delete

    # -------------------
    # Datepicker (igual que el deber: Toplevel + Spinbox)
    # -------------------
    def _open_datepicker(self, entry: ttk.Entry):
        """Abre un datepicker tipo 'deber' (Toplevel con Spinbox para año/mes/día)."""
        def seleccionar_fecha():
            fecha_seleccionada = f"{year_var.get()}-{month_var.get():02d}-{day_var.get():02d}"
            entry.delete(0, tk.END)
            entry.insert(0, fecha_seleccionada)
            top.destroy()

        top = tk.Toplevel(self.root)
        top.title("Seleccionar Fecha")
        top.geometry("250x200")
        top.transient(self.root)
        top.grab_set()

        # Variables iniciales con la fecha actual
        year_var = tk.IntVar(value=datetime.now().year)
        month_var = tk.IntVar(value=datetime.now().month)
        day_var = tk.IntVar(value=datetime.now().day)

        # Controles (igual que en el deber)
        ttk.Label(top, text="Año:").pack(pady=(8,0))
        tk.Spinbox(top, from_=2000, to=2100, textvariable=year_var, width=6).pack()

        ttk.Label(top, text="Mes:").pack(pady=(6,0))
        tk.Spinbox(top, from_=1, to=12, textvariable=month_var, width=4).pack()

        ttk.Label(top, text="Día:").pack(pady=(6,0))
        tk.Spinbox(top, from_=1, to=31, textvariable=day_var, width=4).pack()

        ttk.Button(top, text="Seleccionar", command=seleccionar_fecha).pack(pady=12)

    # -------------------
    # Funcionalidad principal
    # -------------------
    def add_task(self):
        """Añade una nueva tarea escrita en el Entry con la fecha seleccionada."""
        text = self.entry_var.get().strip()
        date = self.date_var.get().strip()

        if not date:
            messagebox.showwarning("Atención", "Por favor, seleccione una fecha para la tarea.")
            return
        if not text:
            messagebox.showwarning("Atención", "La tarea no puede estar vacía.")
            return

        # Crear objeto Task y añadirlo a la lista
        task = Task(text, date)
        self.tasks.append(task)
        self._refresh_listbox()

        # Limpiar campos después de añadir
        self.entry_var.set("")
        self.date_var.set("")
        self.entry.focus_set()

    def mark_completed(self):
        """Alterna el estado completada de la tarea seleccionada."""
        idx = self._get_selected_index()
        if idx is None:
            messagebox.showinfo("Información", "Seleccione una tarea para marcarla como completada.")
            return
        self.tasks[idx].toggle()
        self._refresh_listbox()

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        idx = self._get_selected_index()
        if idx is None:
            messagebox.showinfo("Información", "Seleccione una tarea para eliminar.")
            return
        resp = messagebox.askyesno("Confirmar eliminación", f"¿Eliminar la tarea:\n\n{self.tasks[idx].text}?")
        if not resp:
            return
        del self.tasks[idx]
        self._refresh_listbox()

    # -------------------
    # Eventos
    # -------------------
    def _on_enter_pressed(self, event):
        """Evento: tecla Enter en Entry -> añadir tarea."""
        self.add_task()

    def _on_double_click(self, event):
        """Evento: doble clic en tarea -> alternar completada."""
        index = self.listbox.nearest(event.y)
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle()
            self._refresh_listbox()
            # Mantener selección en la tarea clicada
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(index)

    # -------------------
    # Utilidades internas
    # -------------------
    def _get_selected_index(self):
        """Devuelve el índice de la tarea seleccionada o None si no hay selección."""
        sel = self.listbox.curselection()
        if not sel:
            return None
        return sel[0]

    def _refresh_listbox(self):
        """Actualiza el Listbox según el estado de las tareas."""
        self.listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            self.listbox.insert(tk.END, str(task))
            if task.completed:
                try:
                    self.listbox.itemconfig(i, fg="gray", font=self.font_completed)
                except Exception:
                    self.listbox.itemconfig(i, fg="gray")
            else:
                try:
                    self.listbox.itemconfig(i, fg="black", font=self.font_normal)
                except Exception:
                    self.listbox.itemconfig(i, fg="black")


def main():
    """Función principal: crea la ventana y lanza la aplicación."""
    root = tk.Tk()
    app = TodoApp(root)
    # Centrar ventana en pantalla
    root.update_idletasks()
    w = root.winfo_width()
    h = root.winfo_height()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    root.geometry(f"+{x}+{y}")
    root.mainloop()


if __name__ == "__main__":
    main()
