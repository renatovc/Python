## Start: Import ##
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import pandas as pd
import matplotlib.pyplot as plt

## End: Import ##

###################

## Start: Class & def ##
# Start Class Estudiante #
class Estudiante:
    def __init__(self, nombre, edad, rut, genero, notas):
        self.__nombre = nombre
        self.__edad = edad
        self.__rut = rut
        self.__genero = genero
        self.__notas = notas

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def rut(self):
        return self.__rut

    @property
    def genero(self):
        return self.__genero

    @property
    def notas(self):
        return self.__notas

    def mostrar_informacion(self):
        return f"""Datos del estudiante:
        Nombre: {self.__nombre}
        Edad: {self.__edad}
        Rut: {self.__rut}
        Género: {self.__genero}
        Notas: {self.__notas}
        """

    def calcular_promedio(self):
        if self.__notas:
            promedio = sum(self.__notas) / len(self.__notas)
            return promedio
        else:
            return None
# End Class Estudiante #

# Start Class Grupo #
class Grupo:
    def __init__(self):
        self.__estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        for estudiante in self.__estudiantes:
            print(estudiante.mostrar_informacion())

    def calcular_promedio_grupo(self):
        if not self.__estudiantes:
            return None
        total_notas = sum(estudiante.calcular_promedio() for estudiante in self.__estudiantes if estudiante.calcular_promedio() is not None)
        total_estudiantes = len([e for e in self.__estudiantes if e.calcular_promedio() is not None])
        return total_notas / total_estudiantes if total_estudiantes else None

    def exportar_csv(self, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["Nombre", "Edad", "RUT", "Género", "Notas", "Promedio", "Aprobación"])
            for estudiante in sorted(self.__estudiantes, key=lambda e: e.calcular_promedio() or 0):
                promedio = estudiante.calcular_promedio()
                aprobacion = 'Aprueba' if promedio >= 4.0 else 'Reprueba'
                writer.writerow([estudiante.nombre, estudiante.edad, estudiante.rut, estudiante.genero, estudiante.notas, promedio, aprobacion])
# End Class Grupo #

# Start Class App #
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión y Análisis de Estudiantes")
        self.geometry("1400x600")

        self.grupo = Grupo()

        self.create_widgets()

    def create_widgets(self):
        # Formulario de entrada
        self.nombre_label = tk.Label(self, text="Nombre:")
        self.nombre_label.grid(row=0, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        self.edad_label = tk.Label(self, text="Edad:")
        self.edad_label.grid(row=1, column=0, padx=10, pady=5)
        self.edad_entry = tk.Entry(self)
        self.edad_entry.grid(row=1, column=1, padx=10, pady=5)

        self.rut_label = tk.Label(self, text="RUT (sin puntos, con guion y digito verificador):")
        self.rut_label.grid(row=2, column=0, padx=10, pady=5)
        self.rut_entry = tk.Entry(self)
        self.rut_entry.grid(row=2, column=1, padx=10, pady=5)

        self.genero_label = tk.Label(self, text="Género:")
        self.genero_label.grid(row=3, column=0, padx=10, pady=5)
        self.genero_combobox = ttk.Combobox(self, values=["Hombre", "Mujer", "Otro", "Prefiero no decir"])
        self.genero_combobox.grid(row=3, column=1, padx=10, pady=5)

        self.notas_label = tk.Label(self, text="Notas del 1.0 al 7.0 (separadas por coma):")
        self.notas_label.grid(row=4, column=0, padx=10, pady=5)
        self.notas_entry = tk.Entry(self)
        self.notas_entry.grid(row=4, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self, text="Agregar Estudiante", command=self.agregar_estudiante)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.promedio_button = tk.Button(self, text="Calcular Promedio Grupo", command=self.calcular_promedio_grupo)
        self.promedio_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.export_button = tk.Button(self, text="Exportar a CSV", command=self.exportar_csv)
        self.export_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.mejor_peor_button = tk.Button(self, text="Mejor y Peor Promedio", command=self.obtener_mejor_peor_promedio)
        self.mejor_peor_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.analisis_button = tk.Button(self, text="Análisis y Gráficos", command=self.realizar_analisis)
        self.analisis_button.grid(row=9, column=0, columnspan=2, pady=5)

        # Tabla de estudiantes
        self.tree = ttk.Treeview(self, columns=("nombre", "edad", "rut", "genero", "notas", "promedio", "aprobacion"), show='headings')
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("edad", text="Edad")
        self.tree.heading("rut", text="RUT")
        self.tree.heading("genero", text="Género")
        self.tree.heading("notas", text="Notas")
        self.tree.heading("promedio", text="Promedio")
        self.tree.heading("aprobacion", text="Aprueba o no?")

        self.tree.grid(row=10, column=0, columnspan=2, pady=5)

    def validar_rut(self, rut):
        if '.' in rut:
            return False
        if '-' not in rut:
            return False
        rut_partes = rut.split('-')
        if len(rut_partes) != 2:
            return False
        rut_num, digito = rut_partes
        if not rut_num.isdigit():
            return False
        if digito not in '1234567890Kk':
            return False
        return True

    def validar_notas(self, notas_str):
        try:
            notas = list(map(float, notas_str.split(',')))
            if len(notas) != 4:
                return False
            if any(n < 1.0 or n > 7.0 for n in notas):
                return False
            return True
        except ValueError:
            return False

    def agregar_estudiante(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        rut = self.rut_entry.get()
        genero = self.genero_combobox.get()
        notas_str = self.notas_entry.get()

        if not self.validar_rut(rut):
            messagebox.showerror("Error", "RUT inválido. Debe contener un guion seguido de un dígito verificador sin puntos.")
            return

        if not self.validar_notas(notas_str):
            messagebox.showerror("Error", "Las notas deben ser cuatro números separados por coma, cada uno en el rango de 1.0 a 7.0.")
            return

        try:
            notas = list(map(float, notas_str.split(',')))
            estudiante = Estudiante(nombre, edad, rut, genero, notas)
            self.grupo.agregar_estudiante(estudiante)
            self.actualizar_tabla()
            self.limpiar_formulario()
        except ValueError:
            messagebox.showerror("Error", "Las notas deben ser números válidos.")

    def limpiar_formulario(self):
        self.nombre_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self.rut_entry.delete(0, tk.END)
        self.genero_combobox.set('')
        self.notas_entry.delete(0, tk.END)

    def actualizar_tabla(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for estudiante in sorted(self.grupo._Grupo__estudiantes, key=lambda e: e.calcular_promedio() or 0):
            promedio = estudiante.calcular_promedio()
            aprobacion = 'Aprueba' if promedio >= 4.0 else 'Reprueba'
            self.tree.insert("", tk.END, values=(estudiante.nombre, estudiante.edad, estudiante.rut, estudiante.genero, estudiante.notas, promedio, aprobacion))

    def exportar_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.grupo.exportar_csv(file_path)
            messagebox.showinfo("Exportación Completa", f"Datos exportados a {file_path}")

    def calcular_promedio_grupo(self):
        promedio = self.grupo.calcular_promedio_grupo()
        if promedio is not None:
            messagebox.showinfo("Promedio del Grupo", f"El promedio del grupo es {promedio:.2f}")
        else:
            messagebox.showinfo("Promedio del Grupo", "No hay estudiantes en el grupo.")

    def obtener_mejor_peor_promedio(self):
        if not self.grupo._Grupo__estudiantes:
            messagebox.showinfo("Mejor y Peor Promedio", "No hay estudiantes en el grupo.")
            return

        df = pd.DataFrame([{
            "Nombre": e.nombre,
            "Promedio": e.calcular_promedio()
        } for e in self.grupo._Grupo__estudiantes])

        mejor_promedio = df['Promedio'].max()
        peor_promedio = df['Promedio'].min()
        mejor_alumno = df[df['Promedio'] == mejor_promedio]['Nombre'].values[0]
        peor_alumno = df[df['Promedio'] == peor_promedio]['Nombre'].values[0]

        messagebox.showinfo("Mejor y Peor Promedio", f"Mejor promedio: {mejor_promedio:.2f}, Alumno: {mejor_alumno}\n"
                                                     f"Peor promedio: {peor_promedio:.2f}, Alumno: {peor_alumno}")

    def realizar_analisis(self):
        if not self.grupo._Grupo__estudiantes:
            messagebox.showinfo("Análisis y Gráficos", "No hay estudiantes en el grupo.")
            return

        df = pd.DataFrame([{
            "Nombre": e.nombre,
            "Edad": e.edad,
            "RUT": e.rut,
            "Género": e.genero,
            "Notas": e.notas,
            "Promedio": e.calcular_promedio(),
            "Aprobación": 'Aprueba' if e.calcular_promedio() >= 4.0 else 'Reprueba'
        } for e in self.grupo._Grupo__estudiantes])

        # Mostrar información separada por género
        generos = df.groupby('Género')
        for nombre_genero, grupo in generos:
            messagebox.showinfo(f"Información por Género: {nombre_genero}", grupo.to_string(index=False))

        # Generar tabla estadística con notas y promedios
        estadisticas = df.describe()
        messagebox.showinfo("Estadísticas", estadisticas.to_string())

        # Generar gráfico de barras
        plt.figure(figsize=(10, 5))
        plt.bar(df['Nombre'], df['Promedio'], color='skyblue')
        plt.xlabel('Nombre del Alumno')
        plt.ylabel('Promedio')
        plt.title('Promedio de los Estudiantes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
# End Class App #

if __name__ == "__main__":
    app = App()
    app.mainloop()

###################

"""
## Start: opciones interfaz ##
# Añadir estudiante #
nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingrese la edad del estudiante: ")

print("Ingrese el RUT sin puntos, con guion y digito verificador")
while True:
    rut = input("Ingrese el RUT del estudiante: ")
    if "-" not in rut:
        print("Ingrese un RUT valido")
    else:
        break

genero = input("Ingrese el género (Hombre, Mujer, Otro, Prefiero no decir): ")

print("Indique las notas en una escala del 1.0 al 7.0.")
notas = []
i = 1
while i <= 4:  # Cambié el < 5 por <= 4 para que solo pida 4 notas
    notasEstudiante = float(input(f"Ingrese la nota numero {i} del estudiante: "))
    if notasEstudiante < 1.0 or notasEstudiante > 7.0:
        print("Nota no válida, debe estar entre 1.0 y 7.0")
    else:
        notas.append(notasEstudiante)
        i += 1

estudiante = Estudiante(nombre, edad, rut, genero, notas)

## End: opciones interfaz ##
estudiante.mostrarInformacion()
estudiante.mostrarPromedioNotas()
"""