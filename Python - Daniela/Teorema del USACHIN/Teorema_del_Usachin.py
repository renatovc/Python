# BLOQUE DE IMPORTACIONES
from discord.ui import Button, View  # Importa para crear botones y perosonalizarlos.
from discord import app_commands  # Importa comandos específicos para Discord.
from discord.ext import commands  # Importa la extensión de comandos de discord.py para crear comandos de bot.
from prettytable import PrettyTable  # Importa PrettyTable para formatear datos en tablas.
import discord  # Importa la biblioteca principal de discord.py.
import asyncio  # Importa asyncio para permitir operaciones asincrónicas.
import csv  # Importa CSV para poder trabajar con archivos CSV.
import re  # Importa el módulo de expresiones regulares para manejo de patrones en cadenas.

# Clave del bot para autenticación
keyBot = ""

# Inicializa los intents de Discord para suscribirse a eventos específicos del servidor.
intents = discord.Intents.all()

# Crea un prefijo de comando personalizado "u/" y los intents definidos para invocar al bot.
bot = commands.Bot(command_prefix="u/", intents=intents)
bot.remove_command("help")  # Elimina el comando de ayuda por defecto para personalizarlo más tarde.

#############################
# BLOQUE DE FUNCIONES
#### Start: funciones generales ####
## Start: comando hi ##
# Comando u/hi: saluda al usuario que invocó el comando, mencionándolo y mostrando su rol actual.
@bot.command()
async def hi(ctx):  # El comando es asincrónico para trabajar con la API de Discord de manera eficiente.
    # ENTRADA
    citar_autor = ctx.message.author.mention  # Obtiene la mención del autor del mensaje para etiquetarlo.
    rol_autor = ctx.message.author.roles  # Obtiene todos los roles del autor del mensaje.
    # PROCESO
    # Si el usuario tiene más de un rol, se selecciona el segundo rol (evitando el rol @everyone).
    if len(rol_autor) > 1:
        rol_principal = rol_autor[1].name
    else:
        rol_principal = "@everyone"  # Si solo tiene un rol, se utiliza @everyone.

    # Crea un mensaje (embed) de Discord con un saludo y la información del rol del usuario.
    embed = discord.Embed(
        title="¡Hola!",
        description=f"Bienvenid@ {citar_autor}.\nTu rol actual es {rol_principal}\n\nEscribe u/help para saber más sobre mis comandos.",
        color=discord.Color.orange()
    )
    embed.add_field(name="Roles", value=f"{rol_principal}", inline=False)
    embed.set_footer(text="¡Disfruta de tu estancia!")
    # SALIDA
    # Envía el mensaje al canal donde se ejecutó el comando.
    await ctx.send(embed=embed)
## End: comando hi ##

## Start: comando help ##
# Comando u/help: Muestra una lista de comandos disponibles que el bot puede ejecutar, etiquetando al usuario que invocó el comando.
@bot.command()
async def help(ctx):  # Define un comando asincrónico llamado 'help' que se puede invocar con el prefijo 'u/'.
    # ENTRADA
    autor = ctx.message.author.mention  # Obtiene la mención del autor del mensaje para etiquetarlo en la respuesta.
    # PROCESO
    # Crea un mensaje (embed) para mostrar la ayuda del bot.
    embed = discord.Embed(
        title="Ayuda - Comandos Disponibles",  # Título del mensaje embed.
        description=f"{autor}, estos son mis comandos para ayudarte en tu curso de Cálculo 1:",  # Descripción con la mención del autor.
        color=discord.Color.blue()  # Color del borde del mensaje embed.
    )
    
    # Añade campos al embed con información sobre cada comando disponible.
    embed.add_field(name="u/hi", value="Te doy la bienvenida.", inline=False)
    embed.add_field(name="u/informacion", value="Sabrás sobre las reglas e información del servidor actual.", inline=False)
    embed.add_field(name="u/profesores", value="Te entrego una tabla con los profesores, sus horarios y sus salas.", inline=False)
    embed.add_field(name="u/drive", value="Diseñado para entregarte links de evaluaciones que tú elijas.", inline=False)
    embed.add_field(name="u/youtube", value="Entrega una recopilación de videos que te pueden servir.", inline=False)
    embed.add_field(name="u/promedio", value="Te ayudo a calcular tu promedio y verificar qué nota requieres para aprobar.", inline=False)
    
    # Añade un pie de página al embed con un mensaje adicional.
    embed.set_footer(text="¡Estoy aquí para ayudarte en lo que necesites!")
    # SALIDA
    # Envía el mensaje embed al canal donde se ejecutó el comando.
    await ctx.send(embed=embed)
## End: comando help ##

## Start: comando informacion ##
# Comando u/informacion: Envía un mensaje privado al usuario que invocó el comando con información sobre el servidor actual.
@bot.command()
async def informacion(ctx):  # Define un comando asincrónico llamado 'informacion'.
    # ENTRADA
    autor = ctx.message.author.mention  # Obtiene la mención del autor del mensaje para etiquetarlo en la respuesta.
    servidor = ctx.guild  # Obtiene el objeto del servidor (guild) donde se ejecutó el comando.
    cantidad_usuarios = servidor.member_count  # Obtiene la cantidad total de miembros en el servidor.
    # PROCEOS
    # Obtiene todos los roles del servidor excepto el rol predeterminado "@everyone".
    roles = []
    for rol in servidor.roles:
        if rol.name != "@everyone":
            roles.append(rol.name)

    # Obtiene todos los miembros con permisos de gestionar roles (moderadores).
    moderadores = []
    for miembro in servidor.members:
        if miembro.guild_permissions.manage_roles:
            moderadores.append(miembro.mention)

    # Obtiene una lista con el nombre de todos los canales del servidor.
    canales = []
    for canal in servidor.channels:
        canales.append(canal.name)

    # Muestra las reglas del servidor.
    reglas = (
        "1 - Respetar al staff, incluyendo a los usuarios.\n"
        "No se tolerará cualquier falta de respeto.\n\n"
        "2 - No insultar ni discriminar por orientaciones/creencias.\n"
        "Cualquiera que lo haga, recibirá un kick y dependiendo de su gravedad, será un baneo permanente.\n\n"
        "3 - No poner ningún contenido explícito (+18/NSFW).\n"
        "No pongas ningún tipo de contenido +18/NSFW. Si esto sucede, reporta al usuario, adjuntando las pruebas suficientes y nos haremos cargo en caso de que el usuario esté en este servidor.\n\n"
        "4 - No pases información personal de otro usuario.\n"
        "Bajo ninguna circunstancia se permitirá que un usuario divulgue información de otro usuario. En el caso de que esto suceda, el usuario recibirá un baneo permanente y sin excepciones.\n\n"
        "5 - Si piensas que algo está mal, simplemente no lo hagas.\n"
        "Utiliza el sentido común, si sabes que algo está mal, no lo hagas.\n\n"
        "6 - Se prohíbe tener comportamientos molestos o hacer ruidos molestos en los canales de voz."
    )

    # Crea un mensaje incrustado (embed) para mostrar la información del servidor.
    embed = discord.Embed(
        title=f"Información del Servidor: {servidor.name}",  # Título del embed que incluye el nombre del servidor.
        description=f"Hola {autor}, te presento la información del servidor actual: ",  # Descripción del embed con la mención del autor.
        color=discord.Color.purple()  # Color del borde del mensaje embed.
    )
    # Añade campos al embed con información del servidor.
    embed.add_field(name="Cantidad de usuarios", value=f"{cantidad_usuarios} usuarios", inline=False)
    embed.add_field(name="Roles disponibles", value=", ".join(roles), inline=False)
    embed.add_field(name="Moderadores", value=", ".join(moderadores) if moderadores else "No hay moderadores", inline=False)
    embed.add_field(name="Canales existentes", value=", ".join(canales), inline=False)
    embed.add_field(name="Reglas del Servidor", value=reglas, inline=False)
    embed.set_footer(text="Información proporcionada por tu servidor de Discord.")  # Añade un pie de página al embed.
    # SALIDA
    # Envía el mensaje embed como un mensaje privado (DM) al usuario que ejecutó el comando.
    await ctx.message.author.send(embed=embed)
## End: comando informacion ##

## Start: on_message ##
# Evento on_message: Se ejecuta cada vez que se envía un mensaje en cualquier canal donde el bot tiene permisos.
@bot.event
async def on_message(message):
    # ENTRADA: message
    # PROCESO:
    # Ignora los mensajes enviados por el propio bot.
    if message.author == bot.user:
        return

    # Lista de palabras inapropiadas que se desea detectar y eliminar del chat.
    improperios = {
        "ktm", "ktmre", "kongshetumare", "kongchetumare", "mamahuevo", "maraca", "maraka",
        "marak", "chupasapo", "vagina", "pene", "mierda", "carajo", "maldito", "maldita",
        "coño", "puta", "joder", "joputa", "fuck", "shit", "damn", "bitch", "asshole",
        "bastardo", "motherfucker", "perra", "weon", "wn", "conchetumadre", "conchetumare",
        "ctm", "culiao", "qlo", "klo", "huevón", "maraco", "pico", "shetumare", "shushetumare",
        "maricon", "marikon", "teta", "pichula", "pixula", "chucha"
    }

    mensaje = message.content.lower()  # Convierte el contenido del mensaje a minúsculas para facilitar la comparación.
    citar_autor = message.author.mention  # Obtiene la mención del autor del mensaje para etiquetarlo en la respuesta.

    # Obtén el rol llamado 'Team3' en el servidor actual.
    team3_role = discord.utils.get(message.guild.roles, name="Team3")

    # Si el mensaje contiene alguna palabra inapropiada, elimina el mensaje y alerta al autor.
    if any(improperio in mensaje for improperio in improperios):
        advertencia = f"{citar_autor}, NO se permite el uso de improperios.\nEl equipo moderador {team3_role.mention} ha sido alertado."
        await message.channel.send(advertencia)
        # await message.delete()  # Elimina el mensaje que contiene la palabra inapropiada.

    # Lista de patrones de enlaces prohibidos que se desean detectar y eliminar del chat.
    links_prohibidos = [
        r'linktr.ee/', r'twitch.tv/', r'patreon.com/', r'twitter.com/', r'x.com/', r'https://short.io/',
        r'onlyfans.com/', r't.co/', r'gumroad.com/', r'sheer.com/', r'fans.ly/', r'tiktok.com/',
        r'https://discord.gg/', r'arsmate.com/', r'https://cutt.ly/', r'https://www.twitch.tv/'
    ]
    # SALIDA:
    # Si el mensaje contiene algún enlace prohibido, elimina el mensaje y alerta al autor.
    if any(re.search(link, mensaje) for link in links_prohibidos):
        advertencia_link = f"{citar_autor}, los links de ese tipo NO están permitidos.\nEl equipo moderador {team3_role.mention} ha sido alertado."
        await message.channel.send(advertencia_link)
        # await message.delete()  # Elimina el mensaje que contiene el enlace prohibido.

    '''
    # Manejo de archivos CSV (código comentado para futuras funcionalidades)
    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename.endswith('.csv'):
                user_mention = message.author.mention
                csv_file = await attachment.read()
                csv_content = csv_file.decode('utf-8').splitlines()

                # Pregunta al usuario si desea imprimir el CSV.
                pregunta = await message.channel.send(f"{user_mention}, ¿quieres que imprima el archivo CSV como una tabla en el chat? Responde con Y para sí o N para no.")

                def check(m):
                    return m.author == message.author and m.channel == message.channel and m.content.upper() in ['Y', 'N']

                try:
                    respuesta = await bot.wait_for('message', check=check, timeout=30.0)
                    if respuesta.content.upper() == 'Y':
                        reader = csv.reader(csv_content)
                        table = PrettyTable()
                        headers = next(reader, None)
                        
                        if headers:
                            table.field_names = headers
                            for row in reader:
                                table.add_row(row)

                        table_message = f"{user_mention} ha decidido imprimir el archivo como una tabla (✿◡‿◡):\n```{table}```"
                        await message.channel.send(table_message)
                    else:
                        await message.channel.send(f"{user_mention} esta bien, no imprimire nada ~_~.")
                except asyncio.TimeoutError:
                    await message.channel.send(f"{user_mention}, no se recibió una respuesta a tiempo. No se imprimirá el archivo CSV.")
    '''

    # Procesa otros comandos que puedan haber sido enviados en el mensaje.
    await bot.process_commands(message)
## End: on_message ##
#### End: funciones generales ####

#############################

#### Start: funciones de contenido ####
## Start: Cargar links ##
# Cargar los enlaces desde el archivo CSV
def cargar_links_desde_csv():
    # ENTRADA: archivo data/enlaces.csv
    # PROCESO:
    # Inicializa un diccionario para almacenar los enlaces categorizados.
    links = {
        "apuntes": [],
        "guias": [],
        "libros": [],
        "pep1": [],
        "pep2": [],
        "control1": [],
        "control2": [],
        "por": [],
        "up": [],
        "cr": [],
        "pl": []
    }
    
    # Abre el archivo CSV que contiene los enlaces, en modo lectura y con codificación UTF-8.
    with open("data/enlaces.csv", mode="r", encoding="utf-8") as file:
        # Utiliza csv.DictReader para leer el archivo CSV con el delimitador ';'.
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            # Extrae la categoría, enlace y título de cada fila del archivo.
            categoria = row["categoria"].strip().lower()  # Limpia y convierte la categoría a minúsculas.
            enlace = row["link"].strip()  # Limpia los espacios en blanco del enlace.
            titulo = row["titulo"].strip()  # Limpia los espacios en blanco del título.
            # Si la categoría extraída está en el diccionario de enlaces, añade el enlace formateado.
            if categoria in links:
                links[categoria].append(f"[{titulo}]({enlace})")  # Formato para crear un enlace.
    
    # Devuelve el diccionario de enlaces organizados por categoría.
    return links
# SALIDA
# Cargar los enlaces al iniciar el bot
links = cargar_links_desde_csv()
## End: Cargar links ##

## Start: comando drive ##
@bot.command()
# Comando u/drive: lista interactiva con botones para seleccionar lo que quiere el usuario
async def drive(ctx):
    # ENTRADA: Usuario ejecuta el comando /drive.
    # PROCESO:
    # Creación de botones con etiquetas, estilos y emojis para la interacción
    apuntes_button = Button(label="Apuntes", style=discord.ButtonStyle.primary, emoji="📒")
    guias_button = Button(label="Guías", style=discord.ButtonStyle.primary, emoji="📄")
    libros_button = Button(label="Libros", style=discord.ButtonStyle.primary, emoji="📚")
    pruebas_button = Button(label="Pruebas", style=discord.ButtonStyle.primary, emoji="☠")

    # PROCESO: Para manejar la lógica de cada botón.
    
    # Callback para el botón "Apuntes": muestra una lista de enlaces de apuntes
    async def apuntes_callback(interaction):
        apuntes_button.style = discord.ButtonStyle.success  # Cambia el estilo del botón al hacer clic
        await interaction.response.edit_message(view=main_view)  # Actualiza la vista del mensaje original
        # SALIDA: Enviar lista de apuntes
        await interaction.followup.send(f"Tienes que escribir en clases (¬_¬ ), pero te encontré estos apuntes...\n" + "\n".join(links["apuntes"]))  # Envía un mensaje con los enlaces de apuntes

    # Callback para el botón "Guías": muestra una lista de enlaces de guías
    async def guias_callback(interaction):
        guias_button.style = discord.ButtonStyle.success
        await interaction.response.edit_message(view=main_view)
        # SALIDA: Enviar lista de guías
        await interaction.followup.send(f"Estudia usachino, esto NO se pasa solo. ╰（‵□′）╯\n" + "\n".join(links["guias"]))

    # Callback para el botón "Libros": muestra una lista de enlaces de libros
    async def libros_callback(interaction):
        libros_button.style = discord.ButtonStyle.success
        await interaction.response.edit_message(view=main_view)
        # SALIDA: Enviar lista de libros
        await interaction.followup.send(f"El conocimiento es poder. (✿◡‿◡)\n" + "\n".join(links["libros"]))

    # Callback para el botón "Pruebas": despliega opciones adicionales para elegir tipo de prueba
    async def pruebas_callback(interaction):
        # PROCESO: Crea una nueva vista para los submenús de pruebas
        pruebas_view = View()
        pep_button = Button(label="PEP", style=discord.ButtonStyle.primary)
        controles_button = Button(label="Controles", style=discord.ButtonStyle.primary)
        por_button = Button(label="POR", style=discord.ButtonStyle.primary)

        # Callback para el botón "PEP": muestra opciones de PEP1 y PEP2
        async def pep_callback(interaction):
            pep_view = View()
            pep1_button = Button(label="PEP 1", style=discord.ButtonStyle.primary)
            pep2_button = Button(label="PEP 2", style=discord.ButtonStyle.primary)

            # Callback para el botón "PEP 1": muestra una lista de enlaces de PEP 1
            async def pep1_callback(interaction):
                # SALIDA: Enviar lista de PEP 1
                await interaction.response.send_message("Aquí tienes algunas PEPs 1 que encontré por ahí...\n" + "\n".join(links["pep1"]))

            # Callback para el botón "PEP 2": muestra una lista de enlaces de PEP 2
            async def pep2_callback(interaction):
                # SALIDA: Enviar lista de PEP 2
                await interaction.response.send_message("Aquí tienes algunas PEPs 2 que encontré por ahí...\n" + "\n".join(links["pep2"]))

            pep1_button.callback = pep1_callback
            pep2_button.callback = pep2_callback

            pep_view.add_item(pep1_button)
            pep_view.add_item(pep2_button)

            pep_button.style = discord.ButtonStyle.success
            await interaction.response.edit_message(view=pruebas_view)
            # SALIDA: Mostrar submenú de PEPS
            await interaction.followup.send("¿Qué PEP estás buscando?", view=pep_view)

        # Callback para el botón "Controles": muestra opciones de Control 1 y Control 2
        async def controles_callback(interaction):
            controles_view = View()
            control1_button = Button(label="Control 1", style=discord.ButtonStyle.primary)
            control2_button = Button(label="Control 2", style=discord.ButtonStyle.primary)

            # Callback para el botón "Control 1": muestra una lista de enlaces de Control 1
            async def control1_callback(interaction):
                # SALIDA: Enviar lista de Control 1
                await interaction.response.send_message("Creo que encontré lo que me pediste. Aquí tienes múltiples Controles 1\n" + "\n".join(links["control1"]))

            # Callback para el botón "Control 2": muestra una lista de enlaces de Control 2
            async def control2_callback(interaction):
                # SALIDA: Enviar lista de Control 2
                await interaction.response.send_message("Creo que encontré lo que me pediste. Aquí tienes múltiples Controles 2\n" + "\n".join(links["control2"]))

            control1_button.callback = control1_callback
            control2_button.callback = control2_callback

            controles_view.add_item(control1_button)
            controles_view.add_item(control2_button)

            controles_button.style = discord.ButtonStyle.success
            await interaction.response.edit_message(view=pruebas_view)
            # SALIDA: Mostrar submenú de Controles
            await interaction.followup.send("¿Qué control buscas?", view=controles_view)

        # Callback para el botón "POR"
        async def por_callback(interaction):
            por_button.style = discord.ButtonStyle.success
            await interaction.response.edit_message(view=pruebas_view)
            # SALIDA: Enviar lista de POR
            await interaction.followup.send("Estas son algunas POR que encontré por ahí...\n" + "\n".join(links["por"]))

        # Asignar los callbacks correspondientes a los botones de pruebas
        pep_button.callback = pep_callback
        controles_button.callback = controles_callback
        por_button.callback = por_callback

        pruebas_view.add_item(pep_button)
        pruebas_view.add_item(controles_button)
        pruebas_view.add_item(por_button)

        pruebas_button.style = discord.ButtonStyle.success
        await interaction.response.edit_message(view=main_view)
        # SALIDA: Mostrar menú de opciones de evaluaciones disponibles
        await interaction.followup.send("Selecciona alguna evaluación:", view=pruebas_view)

    # Asignar los callbacks correspondientes a los botones principales
    apuntes_button.callback = apuntes_callback
    guias_button.callback = guias_callback
    libros_button.callback = libros_callback
    pruebas_button.callback = pruebas_callback

    # Crear la vista principal y agregar los botones
    main_view = View()
    main_view.add_item(apuntes_button)
    main_view.add_item(guias_button)
    main_view.add_item(libros_button)
    main_view.add_item(pruebas_button)

    # SALIDA: Envía el mensaje inicial con la vista de botones interactivos
    await ctx.send("¿Con qué te toca sufrir ahora? (°ロ°)", view=main_view)
## End: comando drive ##

## Start: comando youtube ##
@bot.command()
async def youtube(ctx): 
    # ENTRADA: Usuario ejecuta el comando /youtube

    # SALIDA INICIAL: Instrucciones al usuario
    await ctx.send("Coloca en el chat:\nUP para videos de Usach Premium\nCR para canales recomendados\nPL para playlists recomendadas")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    # PROCESO:
    try:
        # Esperar la respuesta del usuario durante 30 segundos
        mensaje = await bot.wait_for('message', timeout=30.0, check=check)
        categoria = mensaje.content.upper()  # Convertir la respuesta a mayúsculas para validación

        # Validar la opción ingresada por el usuario
        if categoria not in ['UP', 'CR', 'PL']:
            await ctx.send("Opción no válida. Intenta nuevamente.")  # SALIDA: Mensaje de error si la opción no es válida
            return

        categoria_lower = categoria.lower()  # Convertir la categoría a minúsculas para coincidencia de claves
        if categoria_lower in links:
            enlaces = links[categoria_lower]  # Recuperar enlaces de la categoría seleccionada
            if enlaces:
                # SALIDA: Enviar lista de enlaces en partes
                mensaje_base = f"Aquí tienes los enlaces de {categoria} (～￣▽￣)～:\n"
                mensaje_actual = mensaje_base
                for enlace in enlaces:
                    if len(mensaje_actual) + len(enlace) + 1 > 2000:  # +1 para el salto de línea
                        await ctx.send(mensaje_actual)  # SALIDA: Enviar mensaje parcial si excede el límite
                        mensaje_actual = mensaje_base
                    mensaje_actual += enlace + "\n"
                
                if mensaje_actual.strip():  # Enviar el último mensaje si tiene contenido
                    await ctx.send(mensaje_actual)  # SALIDA: Enviar mensaje final con enlaces restantes
            else:
                # SALIDA: Mensaje si no se encuentran enlaces para la categoría
                await ctx.send(f"No se encontraron enlaces para la categoría {categoria} (T_T).")

    except asyncio.TimeoutError:
        # SALIDA: Mensaje de tiempo de espera agotado
        await ctx.send("No respondiste a tiempo :c. Intenta nuevamente :D.")
## End: comando youtube ##

### Start: apartado herramientas ###
## Start: comando promedio ##
@bot.command()
async def profesores(ctx):
    # Crear las tablas con PrettyTable
    table_10101 = PrettyTable()
    table_10138_part1 = PrettyTable()
    table_10138_part2 = PrettyTable()
    table_10138_part3 = PrettyTable()

    # Definir los encabezados de las tablas
    field_names = ["Código", "Sección", "Profesores", "Correo Electrónico", "Horario", "Salas"]
    table_10101.field_names = field_names
    table_10138_part1.field_names = field_names
    table_10138_part2.field_names = field_names
    table_10138_part3.field_names = field_names

    # Leer datos desde el archivo CSV
    with open('data/programacion_c1.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Saltar la fila de encabezado si existe
        rows_10138 = []  # Almacenar las filas del código 10138
        for row in reader:
            if row[0].strip() == '10101':  # Filtrar por código 10101
                table_10101.add_row(row)
            elif row[0].strip() == '10138':  # Filtrar por código 10138
                rows_10138.append(row)

    # Dividir las filas de 10138 en tres partes iguales
    third_index = len(rows_10138) // 3
    for row in rows_10138[:third_index]:
        table_10138_part1.add_row(row)
    for row in rows_10138[third_index:2*third_index]:
        table_10138_part2.add_row(row)
    for row in rows_10138[2*third_index:]:
        table_10138_part3.add_row(row)

    # Convertir las tablas a strings
    table_10101_str = f"Tabla de código 10101:\n```\n{table_10101}\n```"
    table_10138_part1_str = f"Tabla de código 10138 (Parte 1):\n```\n{table_10138_part1}\n```"
    table_10138_part2_str = f"Tabla de código 10138 (Parte 2):\n```\n{table_10138_part2}\n```"
    table_10138_part3_str = f"Tabla de código 10138 (Parte 3):\n```\n{table_10138_part3}\n```"

    # Función para enviar el mensaje en partes si supera el límite de 2000 caracteres
    async def send_long_message(ctx, content):
        for i in range(0, len(content), 2000):
            await ctx.send(content[i:i + 2000])

    # Enviar la tabla del código 10101
    await send_long_message(ctx, table_10101_str)
    
    # Enviar las tres partes de la tabla 10138
    await send_long_message(ctx, table_10138_part1_str)
    await send_long_message(ctx, table_10138_part2_str)
    await send_long_message(ctx, table_10138_part3_str)
## End: comando profesores ## 
### End: apartado herramientas ###  
#### End: funciones de contenido ####

#############################

bot.run(keyBot)
