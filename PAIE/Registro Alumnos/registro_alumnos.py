from tkinter import *
from tkinter import ttk, messagebox
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import registro_alumnos_css

# Configuración de la base de datos
engine = create_engine('sqlite:///alumnos.db')
Base = declarative_base()

class Alumno(Base):
    __tablename__ = 'alumnos'
    id = Column(Integer, primary_key=True)
    rut = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
    carrera = Column(String, nullable=False)
    año_ingreso = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Configuración de la ventana principal
window = Tk()
window.geometry("500x500")
window.resizable(0, 0)
window.title("Registro Alumnos")


# Funciones
def agregar_alumno():
    rut = entry_rut.get()
    nombre = entry_nombre.get()
    carrera = carrera_var.get()
    año_ingreso = spinbox_año_ingreso.get()
    genero = genero_var.get()
    
    if rut and nombre and carrera and año_ingreso and genero:
        alumno = Alumno(rut=rut, nombre=nombre, carrera=carrera, año_ingreso=int(año_ingreso), genero=genero)
        session.add(alumno)
        session.commit()
        messagebox.showinfo("Éxito", "Alumno agregado con éxito.")
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")

def buscar_alumno():
    rut = entry_buscar_rut.get()
    alumno = session.query(Alumno).filter_by(rut=rut).first()
    if alumno:
        messagebox.showinfo("Alumno Encontrado", f"Nombre: {alumno.nombre}\nCarrera: {alumno.carrera}\nAño Ingreso: {alumno.año_ingreso}\nGénero: {alumno.genero}")
    else:
        messagebox.showerror("Error", "Alumno no encontrado")

def limpiar_campos():
    entry_rut.delete(0, END)
    entry_nombre.delete(0, END)
    combobox_carrera.set("")
    spinbox_año_ingreso.set("2000")
    genero_var.set("")

# Interfaz de usuario
frame_agregar = Frame(window, padx=10, pady=10)
frame_agregar.pack(pady=10)

Label(frame_agregar, text="RUT").grid(row=0, column=0, sticky=W)
entry_rut = Entry(frame_agregar)
entry_rut.grid(row=0, column=1)

Label(frame_agregar, text="Nombre").grid(row=1, column=0, sticky=W)
entry_nombre = Entry(frame_agregar)
entry_nombre.grid(row=1, column=1)

'''
# Carreras:
## por facultad ##
administracion_y_economia = ["Administración Pública",
                             "Contador Público y Auditor (Diurno)",
                             "Contador Público y Auditor (Vespertino)",
                             "Ingeniería Comercial"]
tecnologia = ["Análisis y Gestión de Procesos Productivos",
              "Diseño en Comunicación Visual",
              "Diseño Industrial",
              "Publicidad",
              "Tecnología en Administración de Personal",
              "Tecnología en Alimentos",
              "Tecnología en Automatización Industrial",
              "Tecnología en Construcciones",
              "Tecnología en Mantenimiento Industrial",
              "Tecnología en Telecomunicaciones"]
ciencia = ["Analista en Computación Científica/Lic. en Ciencias de la Computación",
           "Astrofísica con Mención en Ciencia de Datos",
           "Ingeniería Estadística",
           "Ingeniería Física",
           "Ingeniería Matemática"
           "Pedagogía en Física y Matemática",
           "Pedagogía en Matemática y Computación"]
arquitectura_y_ambiente_construido = ["Arquitectura"]
bachillerato = ["Bachillerato en Ciencias y Humanidades"]
quimica_y_biologia = ["Bioquímica y Licenciatura en Bioquímica",
                      "Pedagogía en Química y Biología",
                      "Química y Farmacia",
                      "Química y Licenciatura en Química",
                      "Técnico Universitario en Análisis Químico y Físico (Diurno)"]
derecho = ["Derecho"]
ciencias_medica = ["Enfermería",
                   "Kinesiología",
                   "Licenciatura en Ciencias de la Actividad Física/Entrenador Deportivo",
                   "Licenciatura en Ciencias de la Actividad Física/Terapeuta en Actividad Física y Salud",
                   "Medicina",
                   "Obstetricia y Puericultura",
                   "Pedagogía en Educación Física",
                   "Terapia Ocupacional"]
ingenieria = ["Ingeniería Civil Biomédica",
              "Ingeniería Civil en Ambiente",
              "Ingeniería Civil en Biotecnología",
              "Ingeniería Civil en Electricidad",
              "Ingeniería Civil en Geomensura y Geomática",
              "Ingeniería Civil en Informática",
              "Ingeniería Civil en Mecánica",
              "Ingeniería Civil en Metalurgia",
              "Ingeniería Civil en Minas",
              "Ingeniería Civil en Obras Civiles",
              "Ingeniería Civil en Química",
              "Ingeniería Civil en Telemática",
              "Ingeniería Civil Industrial",
              "Ingeniería Civil Mecatrónica",
              "Ingeniería de Alimentos",
              "Ingeniería de Ejecución en Climatización",
              "Ingeniería de Ejecución en Computación e Informática",
              "Ingeniería de Ejecución en Electricidad",
              "Ingeniería de Ejecución en Mecánica",
              "Ingeniería de Ejecución en Metalurgia",
              "Ingeniería de Ejecución en Minas",
              "Ingeniería de Ejecución en Química",
              "Ingeniería de Ejecución Industrial",
              "Ingeniería en Agronegocios"]
humanidades = ["Licenciatura en Estudios Internacionales",
               "Licenciatura en Historia",
               "Licenciatura en Linguística aplicada a la Traducción Ingles-Japonés e Inglés-Portugués",
               "Pedagogía en Castellano",
               "Pedagogía en Educación General Básica",
               "Pedagogía en Filosofía",
               "Pedagogía en Historia y Ciencias Sociales",
               "Pedagogía en Inglés",
               "Periodismo",
               "Psicología"]
'''

Label(frame_agregar, text="Carrera").grid(row=2, column=0, sticky=W)
carreras = ["Ing. Civil en Electricidad",
            "Ing. Ejecucion en Electricidad",
            "Ing. Civil Informatica"]
carrera_var = StringVar(value=carreras[0])
combobox_carrera = ttk.Combobox(frame_agregar, textvariable=carrera_var, values=carreras, state="readonly")
combobox_carrera.grid(row=2, column=1)

Label(frame_agregar, text="Año de Ingreso").grid(row=3, column=0, sticky=W)
spinbox_año_ingreso = ttk.Spinbox(frame_agregar, from_=1900, to=2100, increment=1)
spinbox_año_ingreso.set(2000)
spinbox_año_ingreso.grid(row=3, column=1)

Label(frame_agregar, text="Género").grid(row=4, column=0, sticky=W)
genero_var = StringVar(value="")
frame_genero = Frame(frame_agregar)
frame_genero.grid(row=4, column=1, columnspan=3, sticky=W)
Radiobutton(frame_genero, text="Masculino", variable=genero_var, value="Masculino").grid(row=0, column=0)
Radiobutton(frame_genero, text="Femenino", variable=genero_var, value="Femenino").grid(row=0, column=1)
Radiobutton(frame_genero, text="Otro", variable=genero_var, value="Otro").grid(row=0, column=2)

Button(frame_agregar, text="Agregar Alumno", command=agregar_alumno).grid(row=5, columnspan=2, pady=10)

frame_buscar = Frame(window, padx=10, pady=10)
frame_buscar.pack(pady=10)

Label(frame_buscar, text="Buscar Alumno por RUT").grid(row=0, column=0, sticky=W)
entry_buscar_rut = Entry(frame_buscar)
entry_buscar_rut.grid(row=0, column=1)

Button(frame_buscar, text="Buscar Alumno", command=buscar_alumno).grid(row=1, columnspan=2, pady=10)

window.mainloop()