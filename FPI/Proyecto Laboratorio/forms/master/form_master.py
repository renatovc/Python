import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#E6E6E6')
        self.ventana.resizable(width=0, height=0)            
        
        logo =utl.leer_imagen("./img/bioeduca.png", (200, 200))
                        
        label = tk.Label( self.ventana, image=logo,bg='#FDC42C' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        self.ventana.mainloop()