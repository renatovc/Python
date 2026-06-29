#entrada
print("**********************************************************")
print("*              Bienvenido a Mercado......                *")
print("**********************************************************")
#FUNCIONES DEFINIDAS LAS CUALES SE USARAN EN SU PROCESO___________________
def leer(nombre): #FUNCION PARA LEER ARCHIVOS
    try:
        archivo = open(nombre,"r")
    except:
        esc(nombre,"")
        archivo = open(nombre,"r")
    lista = archivo.readlines()
    archivo.close()
    return lista

#________________________________________________________________________


def esc(nombre,texto): #FUNCION LA CUAL ESCRIBIRA AL FINAL DEL CSV, SIN BORRAR DATOS
    archivo = open(nombre,"a")
    archivo.write(texto)
    archivo.close()
    return True



#________________________________________________________________________     
def tipo_usuario(respu, usuario): #PREGUNTARA QUE ACCION VA A HACER
    if respu == 'a':#REALIZAR SUS PREGUNTAS RESPECTIVAS E IR ALMACENANDO EN ARCHIVOS
        x = 1 #ESTA PARTE SER PARA UN VENDEDOR EL CUAL LE PEDIRA QUE INGRESE DETALLES
        cant_venta = int(input("Cantidad de productos a vender: "))
        while x <= cant_venta:
            lista_basica_compra = ''
            print(" ")
            nombre_producto  = input("Nombre producto: ")
            precio = input("Precio: ")
            print('')
            print('categorias de producto disponibles: '+'\n'+ 'plastico(1)' + '\n'+ 'lata(2)' + '\n' + 'fierro(3)'+ '\n'+ 'mueble(4)' +'\n' + 'electrodomestico(5)' + '\n' )
                  
            categoria = input("Categoria de producto: ")
            categoria1 = ''
            if categoria == '1':
                categoria1 = 'plastico'
            elif categoria == '2' :
                cateogria1 = 'lata'
            elif categoria == '3':
                categoria1  = 'fierro'
            elif categoria == '4':
                categoria1 = 'mueble'
            elif categoria == '5':
                categoria1 = 'electrodomestico'
            catego_final = categoria1
                
            nombre_persona = usuario
           
            datos_gener = leer('datos_general.csv')
            i = 0
            while i <len(datos_gener):
                datos = datos_gener[i]
                dato2 = datos.split(';')
                dato3 = dato2[2]
                dato4 = dato2[5]
                
                if nombre_persona == dato3:
                    telefono = dato4
                    
                i+=1
                
            

            lista_basica_compra += nombre_producto +';' + precio+ ';' +catego_final +';' + nombre_persona + ';'+ telefono

            esc('inventario.csv', lista_basica_compra)        

            if x == cant_venta:
                resp = 'su inventario se ha guardado con exito'
                print(resp)
                return resp
            x += 1
    
    
    elif respu == 'b':#PARTE DE UN COMPRADOR, EL CUAL BUSCARA LO QUE NECESITE EL 
        plastico = 0 #USUARIO, DONDE SE LE MOSTRARA LAS CATEGORIAS DISPONIBLES 
        latas = 0
        fierros =0
        muebles =0
        electrodomestico =0

        informacio_inventario = leer('inventario.csv')
        w = 0
        
        
        print('categorias disponibles:')
        while w < len(informacio_inventario):
            info = informacio_inventario[w]
            info = info.split(';')
            
            info2 = info[2].rstrip()
            
            
            if info2 == 'plastico':
                plastico +=1

            elif info2 == 'lata':
                latas += 1
            elif info == 'fierro':
                fierros += 1
            elif info2 == 'mueble':
                muebles += 1
            elif info2== 'electrodomestico':
                electrodomestico +=1
            
        
            w +=1

        
        lista = []
        if plastico > 0:
            lista.append('plastico')
            
        if latas > 0:
            lista.append('lata')
            
        if fierros > 0:
            lista.append('fierro')
            
        if muebles > 0:
            lista.append('mueble')
            
        if electrodomestico > 0:
            lista.append('electrodomestico')
            
        i = 0
        dato_mostrar = ''
        while i < len(lista):
            nuevo = lista[i]
            dato_mostrar += nuevo + '; '
            i += 1
        print( dato_mostrar)
        
        
        dato_ver = input('ingrese que categoria desea buscar: ')
        dato_ver.lower()
        
        x = 0
        print('')
        print('PRODUCTO - PRECIO - CATEGORIA - USUARIO - TELEFONO, INDICE')
        while x < len(informacio_inventario):
            informacio_ = informacio_inventario[x]
            informacio_ = informacio_.split(';')
            
            mostrar_usu = informacio_[2]
            
            
            
            if mostrar_usu == dato_ver :
                info = informacio_[4].rsplit()
                info = info[0]
                precio = '$' + informacio_[1]
                
                informacio_[4] = info
                telefono = '+569' + informacio_[4]
                informacio_[1] = precio
                informacio_[4] = telefono 
                print(informacio_, x)
               
            x+=1
        acc = input("¿DESEA AGREGAR UNO O MÁS DE ESTOS ARTÍCULOS A:  a(FAVORITOS) b(CARRITO) otro caracter(NINGUNO)?:   ")
        if acc == "a":
            i= int(input("CUANTOS ELEMENTOS DESEA AGREGAR?: "))
            while i > x :
                    print("UPS, ESE VALOR ES MUY ALTO, INGRESAR DE NUEVO, POR FAVOR.")
                    i= int(input("CUANTOS ELEMENTOS DESEA AGREGAR?: "))
            j=0
            while j<i:
                fav= int(input("PARA AGREGAR UN PRODUCTO A FAVORITOS INGRESE EL INDICE DEL PRODUCTO DESEADO, DE NO SER ASÍ, INGRESE UN VALOR MENOR A 0."))    
                if fav>=0:
                    while fav > x :
                        print("UPS, ESE VALOR ES MUY ALTO, INGRESAR DE NUEVO, POR FAVOR.")
                        fav= int(input("CUANTOS ELEMENTOS DESEA AGREGAR?: "))
                    addfav(fav)
                    j+=1
                else:
                    break 
        elif acc =="b":
            i= int(input("CUANTOS ELEMENTOS DESEA AGREGAR?: "))
            while i > x :
                    print("UPS, ESE VALOR ES MUY ALTO, INGRESAR DE NUEVO, POR FAVOR.")
                    i= int(input("CUANTOS ELEMENTOS DESEA AGREGAR?: "))
            j=0
            while j<i:
                cart= int(input("PARA AGREGAR UN PRODUCTO A EL CARRITO INGRESE EL INDICE DEL PRODUCTO DESEADO, DE NO SER ASÍ, INGRESE UN VALOR MENOR A 0."))    
                if cart>=0:
                    while cart > x :
                        print("UPS, ESE VALOR ES MUY ALTO, INGRESAR DE NUEVO, POR FAVOR.")
                        cart= int(input("CUANTOS ELEMENTOS DESEA AGREGAR?: "))
                    addcart(cart)
                    j+=1
                else:
                    break 

    elif respu == "c":
        favorito = leerfav(usuario1)  
        x = 0
        print("")
        print("FAVORITOS")
        print('')
        print('PRODUCTO - PRECIO - CATEGORIA - USUARIO - TELEFONO')
        while x < len(favorito):
            informacio_ = favorito[x]
            informacio_ = informacio_.split(';')
            
            mostrar_usu = informacio_[2]
            
            info = informacio_[4].rsplit()
            info = info[0]
            precio = '$' + informacio_[1]   
            informacio_[4] = info
            telefono = '+569' + informacio_[4]
            informacio_[1] = precio
            informacio_[4] = telefono 
            print(informacio_)
            x+=1
    elif respu == "d":
        carrito = leercart(usuario1)  
        x = 0
        print("")
        print("CARRITO")
        print('')
        print('PRODUCTO - PRECIO - CATEGORIA - USUARIO - TELEFONO')
        while x < len(carrito):
            informacio_ = carrito[x]
            informacio_ = informacio_.split(';')
            
            mostrar_usu = informacio_[2]
            
            info = informacio_[4].rsplit()
            info = info[0]
            precio = '$' + informacio_[1]   
            informacio_[4] = info
            telefono = '+569' + informacio_[4]
            informacio_[1] = precio
            informacio_[4] = telefono 
            print(informacio_)
            x+=1    
#________________________________________________________________________ 

def realizar_nueva_accion(usuario1):
    desea_volver = input('desea volver a realizar otra acción (si o no): ')
    desea_volver.lower()
    if desea_volver == 'si':
        accion = input('a(vendedor) o b(comprador): ')
        
        w = tipo_usuario(accion, usuario1)
        return w

    

#________________________________________________________________________         

def contrasena(usuario,contra):
    datos_reco = leer('contrasenas.csv')

    i = 0
    while i < len(datos_reco):
        texto = datos_reco[i]
        texto2= texto.split(';')
        contador = len(datos_reco)
        
        usuario_ = texto2[0].rstrip()
        contrasena = texto2[2].rstrip()
        x = "usuario validado"
        
        if usuario == usuario_:
            
            if contra == contrasena:
                print(x)
                return x
                
            else:
                x = 'lo siento no se pudo validar su sesion'
                print(x)
                return x
        elif i ==  contador - 1:
            x = 'lo siento no se pudo validar su sesion'
            print(x)
            return x
         
            
            
            
        i+=1

#________________________________________________________________________
        
def preguntador(numero):
    x = input('desea volver a intentarlo: ')
    if x == 'si' :
        usuario = input('ingrese su usuario: ')
        contrase =input('ingrese su contraseña: ')
        variable = contrasena(usuario,contrase)
        return variable
    elif x == 'no':
        w= 'Gracias por usar Mercado....'
        print(w)
        return w
    else:
        print('respuesta no reconocida,vuelva a ingresar su respuesta')
        respuesta = input('si o no: ')
        return preguntador(respuesta)
    

#________________________________________________________________________    
def cuenta(respuesta):
    if respuesta == 'si' :
        
        confirmar_usuario = str(input("ingrese su usuario: "))
        confirmar_contraseña = str(input("ingrese su contraseña: "))
        
        return (confirmar_usuario, confirmar_contraseña)
    
        
        
    elif respuesta == 'no':
        
        print("creacion de perfil")
        
        datos_usuario = ""
        print("DATOS GENERALES")
        print("")
        nombre = input("Nombre: ")
        nombre = nombre.lower()
        
        apellidos = input("Apellidos: ")
        apellidos = apellidos.lower()
        
        usuario = input("Nombre de usuario: ")
        usuario = usuario.lower()
        
        nombrerepetido= True
        data = leer("datos_general.csv")
        
        while nombrerepetido == True:
            nombrerepetido=False
            i=0
            while i<len(data):
                user= data[i].split(";")
                if usuario == user[2]:
                    print("Ese nombre de usuario ya está ocupado, por favor elegir otro.")
                    usuario = input("Nombre de usuario: ")
                    usuario = usuario.lower()
                    nombrerepetido=True
                i+=1




        comuna = input("Comuna: ")
        comuna = comuna.lower()
        
        Direccion = input("Direccion: ")
        Direccion = Direccion.lower()
        
        numero_telefonico = input("Numero telefonico: +569 ")
        numero_telefonico = numero_telefonico.lower()
        
        datos_usuario += nombre + ';' + apellidos + ';' + usuario +';' + comuna + ';'+ Direccion + ';' +numero_telefonico + '\n'

        esc('datos_general.csv' , datos_usuario)
        
        print("")
        
        datos_clave = ''        
        usuario_clave = usuario
        clave = input("ingrese su nueva clave: ")
        clave = clave.lower()
        
        correo = input("correo electronico: ")
        correo = correo.lower()

        datos_clave += usuario_clave + ';' + correo + ';' + clave + '\n'
        

        
        esc('contrasenas.csv',  datos_clave)
        w = 'usuario creado'
        print(w)
        return w
        
    else:
        print('respuesta no validada, vuelva a ingresar')
        respuesta = input('si o no: ')
        return cuenta(respuesta)
#________________________________________________________________________     
def no_valida(respuesta2):
    if respuesta2 =='losiento no se pudo validar su sesion':
        novalidado = '*'
        resul = preguntador(novalidado)
        resultado1 = resul[0]
        resultado2 = resul[1]
        return no_valida(resul)
    
    if respuesta2 == 'usuario validado':
        x = 'usuario validado'
        return x
#_______________________________________________________________________________

def addfav(num):
    num = str(num)
    fav = usuario1 + ";" + num
    favo = open("favoritos.csv", "a")
    favo.write(fav+"\n")
    favo.close()
    return True        

#______________________________________________________________________________

def addcart(num):
    num = str(num)
    cart = usuario1 + ";" + num
    carto = open("carrito.csv", "a")
    carto.write(cart+"\n")
    carto.close()
    return True        

#______________________________________________________________________________


def leerfav(usuario):
    favoritos = []
    favoritosnor = []
    favfinal = []
    numero = ""
    fav = leer("favoritos.csv") #lista cuyo elemento es tring de forma abc;2\n
    i=0
    while i < len(fav):
        fav[i]=fav[i].split(";") #formacion de una lista de listas

        i+=1
    i=0
    while i<len(fav):
        if usuario == fav[i][0]:
            index= fav[i][1]
            index=list(index)
            index.pop(-1)
            for x in index:
                numero+=x
            favoritos.append(int(numero)) # si el usuario coincide, tomar el indice y llevarlo a una lista.
        i+=1
    for num in favoritos:
        if num not in favoritosnor:
            favoritosnor.append(num) # eliminar elementos repetidos
    inv=leer("inventario.csv")
    for indice in favoritosnor:
        favfinal.append(inv[indice]) #recuperar de el inventario los elementos favoritos
    return favfinal
#_______________________________________________________________________________________

def leercart(usuario):
    carrito = []
    carritonor = []
    cartfinal = []
    numero = ""
    cart = leer("carrito.csv") #lista cuyo elemento es tring de forma abc;2\n
    i=0
    while i < len(cart):
        cart[i]=cart[i].split(";") #formacion de una lista de listas

        i+=1
    i=0
    while i<len(cart):
        if usuario == cart[i][0]:
            index= cart[i][1]
            index=list(index)
            index.pop(-1)
            for x in index:
                numero+=x
            carrito.append(int(numero)) # si el usuario coincide, tomar el indice y llevarlo a una lista.
        i+=1
    for num in carrito:
        if num not in carritonor:
            carritonor.append(num) # eliminar elementos repetidos
    inv=leer("inventario.csv")
    for indice in carritonor:
        cartfinal.append(inv[indice]) #recuperar de el inventario los elementos del carro
    return cartfinal

#procesamiento
        
preguntar_perfil= input("¿ya tiene cuenta creada?(si o no): ")
x = preguntar_perfil.lower()

respuesta = cuenta(x)

usuario1 = respuesta[0]
contr = respuesta[1]

respuesta2 = contrasena(usuario1,contr)


if respuesta2 == 'usuario validado':

    preg = input('que acción desea hacer? a(vender), b(comprar), c(ver favoritos), d(ver carrito): ')
    preg.lower()
    respuesta3 = tipo_usuario(preg,usuario1)
    if respuesta3 == 'su inventario se a guardado con exito':
        
        res4 = realizar_nueva_accion(usuario1)
        print(res4)

        
elif respuesta2 == 'usuario creado':
    w = input('desea iniciar sesion(si o no): ')
    w.lower()
    if w == 'si':
        respuesta = cuenta(x)
        usuario1 = respuesta[0]
        contr = respuesta[1]
        respuesta2 = contrasena(usuario1,contr)
        if respuesta2 == 'usuario validado':

            preg = input('que acción desea hacer? a(vender), b(comprar), c(ver favoritos), d(ver carrito): ')
            preg.lower()
            respuesta3 = tipo_usuario(preg,usuario1)
            if respuesta3 == 'su inventario se a guardado con exito':
                
                res4 = realizar_nueva_accion(usuario1)
                print(res4)
    else:
        print('GRACIAS POR USAR MERCADO....')
elif respuesta2 == 'losiento no se pudo validar su sesion':
    nueva_resp = no_valida(respuesta2)

    
    if nueva_resp == 'usuario validado' :
        preg = input('que acción desea hacer? a(vender), b(comprar), c(ver favoritos), d(ver carrito): ')
        preg.lower()
        respuesta3 = tipo_usuario(preg,usuario1)
        if respuesta3 == 'su inventario se a guardado con exito':
        
            res4 = realizar_nueva_accion(usuario1)
            print(res4)







       
