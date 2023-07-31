# INTEGRANTES Fausto Bustos, Fernando Pellegrinni, Santiago Gerez. Comision 107.

import os       #Libreria para limpiar la pantalla
import pwinput  #Libreria para ocultar la escritura de contraseña en la consola. SE DEBE INSTALAR PARA QUE FUNCIONE EL PROGRAMA, (pip install pwinput)

#Limpieza de pantalla
os.system('cls')

#Declaracion de las variables de tipo array
"""
-String = nombreUsuario, claveUsuario, nombreLocal, ubicacionLocal, rubroLocal, 
continuarCreacion, ingresoClave, ingresoUsuario, numeroSeleccionado, 
letraSeleccionadaGestion, numeroSeleccionado, letraSeleccionadaNovedades

-Integer = contadorCrearLocales, contadorRubro1, contadorRubro2, contadorRubro3, 
contadorErrorCrearLocales, contadorMenu, contadorRepeticionBucleMenu2, 
contadorRepeticionBucleMenu, contadorLoginIncorrecto

-Las siguientes variables, almacenan colores o han sufrido un cambio con una funcion de 
python, por ejemplo, rubroLocalMinuscula, se almacena dentro de ella rubroLocal modificada
por la funcion lower nativa de python, si bien el tipo de dato que almacenan es string, 
pensamos que aclarar era necesario.
rubroLocalMiniscula, nombreLocalSinEspacios, ubicacionLocalSinEspacios, 
continuarCreacionSinEspacios, red, blue, white, green, nocolor, black, yellow

-Funciones utilizadas: lower() y strip(). Para los colores usamos el codigo ACSII, decidimos no 
incluir esto en Chapin por recomendación del profesor.

-Hemos utilizado las librerias os y pwinput, para limpiar la consola y para codificar la 
contraseña

TYPE
    arreglousuarios = [1..4, 1 .. 4] of string, arreglolocales = [1...50, 1..5] of string, arreglorubros = [1..3] of string, arraylocal = [1..5] of string, arraycod = [1..50] of integer
VAR
    usuarios: arreglousuarios, locales: arreglolocales, rubros: arreglorubros, local: arraylocal, rubros_ordenados: arreglorubros, localesordenadosalfabeticamente: arreglolocales, codigo_locales: arraycod
"""


# Pongo estas variables dentro de un procedimiento asi queda mas comodo para escribirlo en CHAPIN
#Colores en formato ACSII
def inicializar():
    global usuarios,locales, rubros, black, red, green, yellow, blue, nocolor, nombreUsuario, claveUsuario, contadorLoginIncorrecto, contadorRubro1, contadorRubro2, contadorRubro3, contadorCrearLocales
    black   = "\033[0;30m"
    red     = "\033[0;31m"
    green   = "\033[0;32m"
    yellow  = "\033[0;33m"
    blue    = "\033[0;34m"
    nocolor = "\033[0m"

    #Constantes
    usuarios = [
    ["1", 'admin@shopping.com', '12345', 'administrador'],
    ["4", 'localA@shopping.com', 'AAAA1111', 'dueñoLocal'],
    ["6", 'localB@shopping.com', 'BBBB2222', 'dueñoLocal'],
    ["9", 'unCliente@shopping.com', '33xx33', 'cliente']
    ]

    #arreglos
    locales = 50 * [5 * [""]]
    rubros = 3*[0]
    
    #Contador
    contadorLoginIncorrecto = 1

    #Contadores de la cantidad de tipos de rubros de los locales creados.
    contadorRubro1= 0
    contadorRubro2= 0
    contadorRubro3= 0

    #50 locales como maximo. Ademas se le preguntara si quiere continuar la creacion de locales cada vez que finalice el bucle
    contadorCrearLocales = 1       

# ===================== CREAR LOCALES ==========================
def verLocales():
    rta = str(input(f"\n{green}¿Desea ver los locales?{nocolor} (S/N): \n"))
    rta_sinespacios = rta.strip()
    if rta_sinespacios == "s" or rta_sinespacios =="S":
        print(ordenamientoReal(locales[:], 1)) #jugada maestra
            
def busquedaNombreRepetido(nombre):
    izquierda = 0
    derecha = 50 - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if locales[medio][1] == nombre:
            return medio
        elif locales[medio][1] < nombre:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

def ordenamiento(M, colu):
    for i in range(len(M) - 1):
        for j in range(i + 1, len(M)):
            if M[i][colu] > M[j][colu]:
                aux = M[i]
                M[i] = M[j]
                M[j] = aux

def ordenamientoReal(M, colu):
    
    #
    for i in range(len(M) - 1):
        for j in range(i + 1, len(M)):
            if M[i][colu] != '' and M[j][colu] != '' and M[i][colu] < M[j][colu]:
                aux = M[i]
                M[i] = M[j]
                M[j] = aux
                
                
    # Mover los locales vacíos al final
    i = 0
    j = len(M) - 1
    while i < j:
        if M[i][colu] == '':
            while M[j][colu] == '' and j > i:
                j -= 1
            aux = M[i]
            M[i] = M[j]
            M[j] = aux
        i += 1
    return M
                    
def creacionLocales():
    
    global contadorErrorCrearLocales, contadorCrearLocales, contadorRubro1, contadorRubro2, local, contadorRubro3, codigoUsuario, fila, busqueda1
    
    #Indicaciones
    print(f'\n ==={yellow} Recuerde que si uno de los ingresos esta en blanco, o no usa {red}exclusivamente minisculas{yellow} no se guardara y dara error.{nocolor} ===') 
    print(f" ==={yellow} Se pueden crear 15 Locales como maximo y tiene 6 intentos fallidos.{nocolor} === \n")
       
    ordenamiento(locales, 1)
    
    verLocales()
    
    
    #Ingreso para crear Locales
    nombreLocal=    str(input(f"-Ingrese nombre del local: {nocolor}"))
    
    ubicacionLocal= str(input(f"-Ingrese ubicacion del local: {nocolor}"))
    rubroLocal =    str(input(f"-Ingrese rubro al que pertenece el local, {yellow}(indumentaria, perfumería o comida): {nocolor}"))
    codigoUsuario= str(input(f"-Ingrese codigo del usuario al que le corresponde el local: {nocolor}"))
    
    
    # Verificar si ya existe un local con el mismo nombre
    indice = busquedaNombreRepetido(nombreLocal)
    
    if indice != -1:
        print(f"\n{red}Ya existe un local con el mismo nombre. No se pudo crear el local.{nocolor}")
        
    #Convirtiendo el ingreso de datos en miniscula para evitar errores
    rubroLocalMinuscula = rubroLocal.lower()
    
    # Convirtiendo el ingreso de datos a sin espacios para validar que el usuario no ingrese un valor vacio
    nombreLocalSinEspacios = nombreLocal.strip()
    ubicacionLocalSinEspacios = ubicacionLocal.strip()
    
    
    busqueda1 = False
    
    #Hace busqueda del codigo de usuario para verificar que pertenezca a un usuario existente
    fila = busquedaSecuencialBidimensional(usuarios, codigoUsuario, 0)
    
    #Si el codigo existe, verifica que en la fila donde se encontro el codigo este dueño local
    if fila != False:
        busqueda1 = busquedaSecuencialUnidimensional(fila, "dueñoLocal")
    
     #Validacion de ingreso
    if (nombreLocalSinEspacios != '' and ubicacionLocalSinEspacios != '') and (rubroLocalMinuscula == "indumentaria" or rubroLocalMinuscula == "perfumeria" or rubroLocalMinuscula == "comida") and (busqueda1 == True) and (indice == -1):
        #Cada vez que se cree un local, se le asignara por defecto el estado A, de activo
        estado = "A"
        contadorCrearLocales_cadena = str(contadorCrearLocales)
        local = [contadorCrearLocales_cadena, nombreLocal, ubicacionLocal, rubroLocal, estado]
        
        #Ahora iremos guardando cada local en una lista de todos los locales
        locales[contadorCrearLocales] = local
        
        #Cuenta los locales creados asi puede establecer un limite(15) y el codigo del local
        contadorCrearLocales = contadorCrearLocales + 1
        
        #Info del local creado
        print(f"\n{green}Local creado exitosamente{nocolor}")
        print(f"El nombre del local es, ", nombreLocal, ", su ubicacion es, ", ubicacionLocal, ", y su rubro es, ", rubroLocalMinuscula, "\n")
        
        # Almacenamiento del rubro del local que fue creado
        if rubroLocalMinuscula == "indumentaria":
            contadorRubro1 = contadorRubro1 + 1
        elif rubroLocalMinuscula == "perfumeria":
            contadorRubro2 = contadorRubro2 + 1
        elif rubroLocalMinuscula == "comida": 
            contadorRubro3 = contadorRubro3 + 1
    
    else:
        #Cuenta los errores para terminar el bucle cuando sobrepasa el maximo permitido e imprime una alerta
        contadorErrorCrearLocales = contadorErrorCrearLocales + 1
        print(f"{red}\n No has ingresado un valor correcto. Vuelve a intentarlo. Recuerde que puede equivocarse 6 veces como maximo{nocolor}")
    
    #Preguntar si quiere seguir creando locales   
    continuarCreacion = str(input(f"\n{green}¿Desea continuar creando locales?{nocolor} (En caso de que quiera seguir, presione cualquier tecla, sino escriba '*', sin repetirlo): "))
    continuarCreacionSinEspacios = continuarCreacion.strip()
    
    #Le damos la posibilidad al usuario de salir del bucle ingresando unicamente un asterisco, si ingresa 2 u otro valor, continuara en el bucle.
    if (continuarCreacionSinEspacios == "*"):
        contadorErrorCrearLocales = contadorErrorCrearLocales + 10
        print(f"{red}\nHa decidido no continuar con la creacion de locales. Volviendo...{nocolor}")
     
def ordenarRubros(rubros, tam):
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if rubros[i][1] < rubros[j][1]:
                # Forma normal de intercambiar elementos
                aux = rubros[i]
                rubros[i] = rubros[j]
                rubros[j] = aux

    return rubros

def analizar_rubros(contadorRubro1, contadorRubro2, contadorRubro3):
   
    nombres_rubros = ['indumentaria', 'perfumeria', 'comida']

    rubros = [
        [nombres_rubros[0], contadorRubro1],
        [nombres_rubros[1], contadorRubro2],
        [nombres_rubros[2], contadorRubro3]
    ]

    rubros_ordenados = ordenarRubros(rubros, 3)

    print(f"\n {blue}Lista con los rubros de forma descendente con respecto a cantidad de locales que posee cada uno: {nocolor}", rubros_ordenados)
   
#===================== MODIFICAR LOCALES ============================ 
def modificarLocal():
    
    verLocales()
    
    ingresarCodLocal = str(input("Ingrese el codigo a modificar del local: "))
    
    fila = busquedaSecuencialBidimensional(locales, ingresarCodLocal, 0)
    
    if fila != False:
        
        if fila[4] == "A":
            print("Esta activo")
            modificandoLocal(fila)
            
        elif fila[4] == "B":
            print("Esta inactivo")
            reactivar = str(input("Desea restaurar este local? (S/N)"))
            if reactivar == "S" or reactivar == "s":
                fila[4] = "A"
                modificandoLocal(fila)
    else:
        print("El local con el codigo que ingresaste no existe")
    
def modificandoLocal(fila):
    
    global contadorRubro1, contadorRubro2, contadorRubro3
    
    nuevoNombreLocal= str(input(f"-Ingrese nombre del local: {nocolor}"))
    nuevoUbiLocal=str(input(f"-Ingrese ubicacion del local: {nocolor}"))
    nuevoRubroLocal= str(input(f"-Ingrese rubro al que pertenece el local, {yellow}(indumentaria, perfumería o comida): {nocolor}"))
    
    # Verificar si ya existe un local con el mismo nombre
    indice = busquedaNombreRepetido(nuevoNombreLocal)
    
    if indice != -1:
        print(f"\n{red}Ya existe un local con el mismo nombre. No se pudo crear el local.{nocolor}")
        
    #Convirtiendo el ingreso de datos en miniscula para evitar errores
    nuevoRubroLocalMinuscula = nuevoRubroLocal.lower()
    
    # Convirtiendo el ingreso de datos a sin espacios para validar que el usuario no ingrese un valor vacio
    nuevoNombreLocalSinEspacios = nuevoNombreLocal.strip()
    nuevoUbicacionLocalSinEspacios = nuevoUbiLocal.strip()
    
    if (nuevoNombreLocalSinEspacios != '' and nuevoUbicacionLocalSinEspacios != '') and (nuevoRubroLocalMinuscula == "indumentaria" or nuevoRubroLocalMinuscula == "perfumeria" or nuevoRubroLocalMinuscula == "comida") and (indice == -1):

        # #descontarrubro
        if fila[3] == "indumentaria":
            contadorRubro1 = contadorRubro1 - 1
        elif fila[3] == "perfumeria":
            contadorRubro2 = contadorRubro2 - 1
        elif fila[3] == "comida": 
            contadorRubro3 = contadorRubro3 - 1
            
        #modificar valores por los nuevos
        fila[1] = nuevoNombreLocalSinEspacios
        fila[2] = nuevoUbicacionLocalSinEspacios
        fila[3] = nuevoRubroLocalMinuscula
        
        #Info del local creado
        print(f"\n{green}Local modificado exitosamente{nocolor}")
        print(f"El nombre del local es, ", nuevoNombreLocalSinEspacios, ", su ubicacion es, ", nuevoUbicacionLocalSinEspacios, ", y su rubro es, ", nuevoRubroLocalMinuscula, "\n")
         

        #sumar rubro
        if nuevoRubroLocalMinuscula == "indumentaria":
            contadorRubro1 = contadorRubro1 + 1
        elif nuevoRubroLocalMinuscula == "perfumeria":
            contadorRubro2 = contadorRubro2 + 1
        elif nuevoRubroLocalMinuscula == "comida": 
            contadorRubro3 = contadorRubro3 + 1
            
#====================== ELIMINAR LOCALES ======================
def eliminarLocal():
    
    verLocales()
    
    ingresarCodLocal = str(input("Ingrese el codigo a eliminar del local: "))
    
    filanga = busquedaSecuencialBidimensional(locales, ingresarCodLocal, 0)
    
    if filanga != False:
        
        if filanga[4] == "A":
            print("Esta activo")
            eliminandoLocal(filanga)
            
        elif filanga[4] == "B":
            print("Este local ya esta inactivo ")

    else:
        print("El local con el codigo que ingresaste no existe")

def eliminandoLocal(filanga):
    
    global contadorRubro1, contadorRubro2, contadorRubro3
    
    filanga[4] = "B"
    
# #descontarrubro para que no se tenga en cuenta en el reporte de cantidad
    if filanga[3] == "indumentaria":
        contadorRubro1 = contadorRubro1 - 1
    elif filanga[3] == "perfumeria":
        contadorRubro2 = contadorRubro2 - 1
    elif filanga[3] == "comida": 
        contadorRubro3 = contadorRubro3 - 1
            
    print(f"\n{green}Local eliminado exitosamente{nocolor}")
       
#======================= MAPA LOCALES ==========================
def mapaLocal():
    
    # creo un arreglo nuevo con los locales ordenados alfabeticamente por su nombre
    localesordenadosalfabeticamente = ordenamientoReal(locales[:], 1)
    
    #creo un localesordenadosalfabeticamente array que es donde se almacenaran los codigos de cada uno de los locales que ya fueron ordenados
    codigos_locales = 50*[0]

    # Iterar sobre la matriz y obtener los códigos de la primera columna
    for i in range(50):
        if localesordenadosalfabeticamente[i][0] == "":
            localesordenadosalfabeticamente[i][0] = "0"
        codigoint = int(localesordenadosalfabeticamente[i][0])
        codigos_locales[i] = codigoint

    
    #creamos el mapa a partir de las condiciones dadas
    filas = 10
    columnas = 5

    # Creamos la cuadrícula utilizando un bucle for
    for i in range(filas):
        print("+--+--+--+--+--+")
        for j in range(columnas):
            
            #esta linea es para acceder al numero que se va a mostrar en la celda actual, i * columnas representa la cantidad de 
            #numeros que se han mostrado antes en las filas anteriores, y j representa la columna actual dentro de ella
            index = i * columnas + j
            
            #se convierte en una cadena  para que podamos darle formato y manipularlo para mostrarlo correctamente.
            num_str = str(codigos_locales[index])
            
            # Agregar espacio si el número tiene solo un dígito, esto lo hago para que el mapa de locales quede simetrico
            #POrque si hay numeros de un caracter y numeros de 2, se desalinea todo, entonces tengo que corrroborar que los numeros
            #que tengan menos de dos caracteres, se les agregue un espacio
            if len(num_str) == 1:
                num_str = " " + num_str
            print(f"|{num_str}", end="") #end representa un salto de lineae
        
        #imprime el ultimo separador de la linea
        print("|")

    print("+--+--+--+--+--+")

    
#================= Menues =================
def menuAdministrador():
    print(f"""
    ====== {red}M{yellow}E{red}N{yellow}U{nocolor} ====== 
    \n 1. Gestion de locales 
    \n 2. Crear cuentas de dueños de locales 
    \n 3. Aprobar / Denegar solicitud de descuento 
    \n 4. Gestión de Novedades 
    \n 5. Reporte de utilización de descuentos 
    \n 0. Salir 
    """) 

def menuGestionDeLocales():
    print(f"""
    ====== GESTION DE LOCALES ====== 
    \n a. Crear locales 
    \n b. Modificar local 
    \n c. Eliminar local 
    \n d. Mapa de locales 
    \n e. Volver 
    """) 

def menuGestionDeNovedades():
    print(f"""
    ====== GESTION DE NOVEDADES ====== 
    \n a. Crear novedades 
    \n b. Modificar novedad 
    \n c. Eliminar novedad 
    \n d. Ver reporte de novedad
    \n e. Volver 
    """) 
    
def menuDueñodeLocales():
    print(f"""
    ====== {red}M{yellow}E{red}N{yellow}U{nocolor} ====== 
    \n1. Gestion de Descuentos 
     a. Crear novedades 
     b. Modificar novedad 
     c. Eliminar novedad 
     d. Ver reporte de novedad
     e. Volver 
    \n2. Aceptar / Rechazar pedido de descuento
    \n3. Reporte de uso de descuentos
    \n0. Salir
    """) 

def menuClientes():
    print(f"""
    ====== {red}M{yellow}E{red}N{yellow}U{nocolor} ====== 
    \n 1. Registrarme 
    \n 2. Buscar descuentos en locales 
    \n 3. Solicitar descuento 
    \n 4. Ver Novedades 
    \n 0. Salir 
    """) 

# Mensajes de alertas para las opciones en construccion o de retorno al anterior Menu 
def alertaLetraGestion():
    
    global contadorMenu, contadorRepeticionBucleMenu2
    
    #Mensaje correspondiente a cada letra
    if (letraSeleccionadaGestion == "e"):
        
        #Para cerrar el bucle
        contadorMenu = contadorMenu + 5
        
        #Mensaje
        print(f"{red}Volviendo...{nocolor}")
    else:
        print(f"{yellow}En construccion...{nocolor}")
        
        #Cierra el bucle
        contadorRepeticionBucleMenu2 = contadorRepeticionBucleMenu2 + 3
        
def alertaLetraNovedades():
    
    global contadorMenu, contadorRepeticionBucleMenu
    
    #Mensaje correspondiente a cada letra
    if (letraSeleccionadaNovedades == "e") and contadorRepeticionBucleMenu <= 3:
        contadorMenu = contadorMenu + 5
        print(f"{red}Volviendo...{nocolor}")
    else:    
        print(f"{yellow}En construccion...{nocolor}")
        contadorRepeticionBucleMenu = contadorRepeticionBucleMenu + 3

def alertaNumeroMenu():
    
    global contadorLoginIncorrecto, contadorMenu
    
    if(numeroSeleccionado == "0"):
        contadorLoginIncorrecto= contadorLoginIncorrecto + 3
        print(f"\n{red}Saliendo...{nocolor}")
    
    else:    
        print(f"{yellow}En construccion...{nocolor}")
        contadorMenu = contadorMenu + 3

#============ BUSQUEDAS SECUENCIALES ======================
def busquedaSecuencialBidimensional(M, E, C):#C es la columna donde queremos buscar
    fil = 0

    while fil < len(M):
        if M[fil][C] == E:  # Verificar solo la segunda columna (índice 1)
            return M[fil]
        fil += 1

    return False

# Lo hago aca para tambien verificar que los valores esten dentro del mismo array, 
# porque los input pueden existr los 3 a la vez sin estar en la misma fila, o sea en el mismo usuario
def busquedaSecuencialUnidimensional(lista, input):
    i = 0
    while (i < len(lista)) and (lista[i] != input):  # Agregamos la condición i <= 100
        i = i + 1
    if i < len(lista) and lista[i] == input:  # por que? Verificamos si i está dentro del rango válido y si encontramos el elemento
        return True
    else:
        return False
    

    
# Programa Principal
inicializar()

#Ingreso de Usuario
while contadorLoginIncorrecto <= 3:
    
    print("\n === LOGIN ===")
    #Ingreso de datos
    ingresoTipoUsuario = str(input(f"\n{green}Ingrese su tipo de usuario: {nocolor}"))
    ingresoUsuario = str(input(f"\n{green}Ingrese su nombre de usuario: {nocolor}"))
    ingresoClave   = pwinput.pwinput(str(f"{green}Ingrese su clave: {nocolor}"))
      
    fila = busquedaSecuencialBidimensional(usuarios, ingresoUsuario, 1)
    
    # Inicializar las variables
    busquedaClave = False
    busquedaTipoUsuario = False
    
    if fila != False:
        busquedaClave = busquedaSecuencialUnidimensional(fila, ingresoClave)
        busquedaTipoUsuario = busquedaSecuencialUnidimensional(fila, ingresoTipoUsuario)
        if (fila[1] != ingresoUsuario or fila[2] != ingresoClave or fila[3] != ingresoTipoUsuario) and fila != False:
            contadorLoginIncorrecto +=  1
            print(f"{red}Usuario incorrecto. Recuerde que son 3 intentos maximo.{nocolor}")
    else:
        contadorLoginIncorrecto += 1
        print(f"{red}Usuario incorrecto. Recuerde que son 3 intentos maximo.{nocolor}")
        
    
    # Si el usuario y clave son correctas, se repetira este ciclo en bucle hasta que el usuario ingrese 0
    while (ingresoTipoUsuario == "administrador" ) and (busquedaClave == True) and (contadorLoginIncorrecto <= 3):

        # Menu
        menuAdministrador()
        
        #Decidimos usar str en vez de int, para que no salte error si el usuario ingresa una letra cuando el, de esta forma podemos manejar mejor las restricciones y podemos dirigir al usuario hacia donde nosotros queremos asi no puede buggear el programa
        numeroSeleccionado = str(input(f"{green}Ingrese el numero de la seccion a la cual se quiere dirigir: {nocolor}"))
        
        #Esta aca para cuando el usuario clickee en volver, se reinicie el contador y pueda entrar al ciclo while, ya que la opcion d hace que contadorMenu = 3
        contadorMenu = 0
        
        #Usamos while porque queda definido en el enunciado del tp1, que solo salga del programa cuando toque 0, por el contrario, si no ingresa ningun numero correcto, se repetira infinitamente
        while numeroSeleccionado == "1" and contadorMenu <= 3: 
            
            #Menu
            menuGestionDeLocales()
            
            #Ingreso de datos
            letraSeleccionadaGestion = str(input(f"{green}Ingrese la letra que corresponda de a la seccion que se quiera dirigir: {nocolor}"))
            
            #Esta aca para limpiar cada vez que salga del bucle de a
            contadorErrorCrearLocales = 0   
            
            #Le da fin al bucle
            contadorRepeticionBucleMenu2 = 0
            
            # Mensaje cuando alcanza limite de locales creados
            if (contadorCrearLocales == 50 and letraSeleccionadaGestion == "a"):
                print(f"\n{red}Has alcanzado el limite de locales creados{nocolor}")
            
            while (letraSeleccionadaGestion == "a") and (contadorCrearLocales < 50 and contadorErrorCrearLocales <= 5): 
                                
                #Llamada de funcion para crear Locales
                creacionLocales()   
                
                #Llamada de funcion para mostrar las relaciones de equivalencia entre los rubros de los locales. Hemos decidido que se muestre cada vez que se crea el local asi el usuario puede llevar un mejor control
                analizar_rubros(contadorRubro1, contadorRubro2, contadorRubro3)  
                
            #Dejaremos este bucle asi por un tema de practicidad y legibilidad, a medida que avancemos con el programa, le daremos la division y el desarrollo que le corresponde a cada letra      
            while (letraSeleccionadaGestion == "b") and contadorMenu <= 5 and contadorRepeticionBucleMenu2 <= 3:
                
                modificarLocal()
                continuar = str(input("Si no desea continuar escriba *(asterisco) :")) 
                if continuar == "*" or continuar == "*":
                    contadorRepeticionBucleMenu2 += 4
                
            while (letraSeleccionadaGestion == "c") and contadorMenu <= 5 and contadorRepeticionBucleMenu2 <= 3:
                
                eliminarLocal()
                continuar = str(input("Si no desea continuar escriba *(asterisco) :")) 
                if continuar == "*" or continuar == "*":
                    contadorRepeticionBucleMenu2 += 4
                
            while (letraSeleccionadaGestion == "d") and contadorMenu <= 5 and contadorRepeticionBucleMenu2 <= 3:
                
                mapaLocal()
                continuarmapa = str(input("Si no desea continuarmapa escriba *(asterisco) :")) 
                if continuarmapa == "*" or continuarmapa == "*":
                    contadorRepeticionBucleMenu2 += 4
                
            while (letraSeleccionadaGestion == "e") and contadorMenu <= 5 and contadorRepeticionBucleMenu2 <= 3:
                
                alertaLetraGestion()
    
        #La opcion 4, solo muestra un menu, y al clickear alguna de las opciones de este nuevo menu, aparece un mensaje y se repite el bucle hasta que el usuario presione en salir
        while numeroSeleccionado == "4" and contadorMenu <= 3: 
            
            # Es para cuando se selecciona una opcion en construccion, no se salga al menu principal, sino que le muestre el menu correspondiente, y que para salir tenga que presionar e.(salir)
            contadorRepeticionBucleMenu = 0
            #Menu
            menuGestionDeNovedades()
            
            # Seleccion de la opcion del menu
            letraSeleccionadaNovedades = str(input(f"{green}Ingrese la letra que corresponda de a la seccion que se quiera dirigir: {nocolor}"))
            
            # Dejaremos este bucle bastante compacto, ya que su funcionalidad es unicamente mostrar un mensaje en pantalla, mas adelante cuando sigamos desarrollando le daremos la division que le corresponde a cada letra
            while (letraSeleccionadaNovedades == "a" or letraSeleccionadaNovedades == "b" or letraSeleccionadaNovedades == "c" or letraSeleccionadaNovedades == "d" or letraSeleccionadaNovedades == "e") and contadorMenu <= 5 and contadorRepeticionBucleMenu <= 3:
                
                alertaLetraNovedades()

        #Por ahora este bucle son las opciones quedara asi, ya que son practicamente lo mismo y ahorramos lineas de codigo,
        while (numeroSeleccionado == "0" or numeroSeleccionado == "2" or numeroSeleccionado == "3" or numeroSeleccionado == "5") and contadorMenu <= 3 and contadorLoginIncorrecto <= 3:
            
            alertaNumeroMenu()
    
    while (ingresoTipoUsuario == "dueñoLocal" ) and (contadorLoginIncorrecto <= 3):
        menuDueñodeLocales()
        numeroMenuDueño = str(input("ingrese el numero de la seccion a la cual se quiere dirigir: "))
        if numeroMenuDueño == "1" or numeroMenuDueño == "2" or numeroMenuDueño =="3":
            print("En construccion..")
        elif numeroMenuDueño == "0":
            contadorLoginIncorrecto +=4
    while (ingresoTipoUsuario == "cliente" ) and (contadorLoginIncorrecto <= 3):
        menuClientes()
        numeroMenuCLiente = str(input("ingrese el numero de la seccion a la cual se quiere dirigir: "))
        if numeroMenuCLiente == "1" or numeroMenuCLiente == "2" or numeroMenuCLiente =="3" or numeroMenuCLiente =="4":
            print("En construccion..")
        elif numeroMenuCLiente == "0":
            contadorLoginIncorrecto +=4

print(f"\n{red}======Fin del programa======{nocolor}")
             
