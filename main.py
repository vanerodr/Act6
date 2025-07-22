import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

ARCHIVO = "libros.txt"

class Libro:
    def __init__(self, id, titulo, autor, anio):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"{self.id},{self.titulo},{self.autor},{self.anio}"

    @staticmethod
    def from_string(linea):
        partes = linea.strip().split(',')
        if len(partes) == 4:
            return Libro(*partes)
        return None

def crear_libro(libro):
    with open(ARCHIVO, "a") as f:
        f.write(str(libro) + "\n")

def leer_libros():
    libros = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                libro = Libro.from_string(linea)
                if libro:
                    libros.append(libro)
    return libros

def actualizar_libro(id, nuevo_libro):
    libros = leer_libros()
    with open(ARCHIVO, "w") as f:
        for libro in libros:
            if libro.id == id:
                f.write(str(nuevo_libro) + "\n")
            else:
                f.write(str(libro) + "\n")

def eliminar_libro(id):
    libros = leer_libros()
    with open(ARCHIVO, "w") as f:
        for libro in libros:
            if libro.id != id:
                f.write(str(libro) + "\n")

# GUI
def app():
    ventana = tk.Tk()
    ventana.title("Gestión de Libros")

    tk.Label(ventana, text="ID").grid(row=0, column=0)
    tk.Label(ventana, text="Título").grid(row=1, column=0)
    tk.Label(ventana, text="Autor").grid(row=2, column=0)
    tk.Label(ventana, text="Año").grid(row=3, column=0)

    id_entry = tk.Entry(ventana)
    titulo_entry = tk.Entry(ventana)
    autor_entry = tk.Entry(ventana)
    anio_entry = tk.Entry(ventana)

    id_entry.grid(row=0, column=1)
    titulo_entry.grid(row=1, column=1)
    autor_entry.grid(row=2, column=1)
    anio_entry.grid(row=3, column=1)

    area_texto = scrolledtext.ScrolledText(ventana, width=40, height=10)
    area_texto.grid(row=5, column=0, columnspan=2, pady=10)

    def limpiar():
        id_entry.delete(0, tk.END)
        titulo_entry.delete(0, tk.END)
        autor_entry.delete(0, tk.END)
        anio_entry.delete(0, tk.END)

    def btn_crear():
        libro = Libro(id_entry.get(), titulo_entry.get(), autor_entry.get(), anio_entry.get())
        crear_libro(libro)
        limpiar()
        messagebox.showinfo("Éxito", "📚 Libro creado")

    def btn_leer():
        libros = leer_libros()
        area_texto.delete(1.0, tk.END)
        for l in libros:
            area_texto.insert(tk.END, str(l) + "\n")

    def btn_actualizar():
        libro = Libro(id_entry.get(), titulo_entry.get(), autor_entry.get(), anio_entry.get())
        actualizar_libro(libro.id, libro)
        limpiar()
        messagebox.showinfo("Actualizado", "🔁 Libro actualizado")

    def btn_eliminar():
        eliminar_libro(id_entry.get())
        limpiar()
        messagebox.showinfo("Eliminado", "❌ Libro eliminado")

    tk.Button(ventana, text="Crear", command=btn_crear).grid(row=4, column=0)
    tk.Button(ventana, text="Leer", command=btn_leer).grid(row=4, column=1)
    tk.Button(ventana, text="Actualizar", command=btn_actualizar).grid(row=6, column=0)
    tk.Button(ventana, text="Eliminar", command=btn_eliminar).grid(row=6, column=1)

    ventana.mainloop()

if __name__ == "__main__":
    app()