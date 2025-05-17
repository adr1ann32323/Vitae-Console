from datetime import datetime

hoja_vida = {}   
#---------------------datos personales--------------------------------------- 
def datos_personales():    
    while True:
        documento = input("Ingrese su numero de identificacion: ").strip()
        if documento.isdigit():
            break
        print("El documento debe ser solo numeros.")
        
    nombre = input ("Ingresa tu nombre completo ").title().strip()
    while nombre == "":
        nombre = input("Nombre no puede estar vacio. Intenta de nuevo: ").title().strip()
        
    contacto =input("Ingrese tu numero de contacto: ")
    while not contacto.isdigit() or len(contacto) < 7 or len(contacto) > 10:
        contacto = input("Numero invalido. Solo puedes ingresar digitos, minimo 7 numeros y maximo 10: ").strip()
        
    direccion =input("Ingrese tu direccion de residencia: ").strip()
    while direccion == "":
        direccion = input("Direccion no puede estar vacia. Intenta de nuevo: ").strip()

    correo =input("Ingrese tu correo electronico: ")
    while "@" not in correo or "." not in correo:
        correo = input("Correo invalido. Debe tener '@' y '.': ").strip()

    while True:
        fecha = input("Ingrese tu fecha de nacimiento separado por '/' :(DD/MM/AAAA): ").strip()
        try:
            fecha_valida = datetime.strptime(fecha, "%d/%m/%Y")
            break
        except ValueError:
            print("Fecha inválida. Usa el formato DD/MM/AAAA, por ejemplo 15/05/2000.")
            
    doc_fecha = (documento, fecha)
    datos = {
        "documento y fecha": doc_fecha,
        "contacto": contacto, 
        "direccion": direccion,
        "correo": set(correo),
    }
    
    return nombre, datos

#-----------------titulo---------------
formacion = []
def add_titulo():
    print("Te pediremos tus titulos uno por uno a continuacion:\n")
    print("Ingresa el titulo profesional que deseas agregar a tu hoja de vida")
    titulo = input()
    while not titulo.strip().replace(" ","").isalpha():
        print("Ingresaste numeros o caracteres, intenta de nuevo: ")
        titulo = input()

    print(f"Ingresa la institucion donde aquiriste el titulo de {titulo}")
    institucion = input()
    while not institucion.strip().replace(" ",""):
        print("No puedes dejarlo vacio, intenta de nuevo: ")
        institucion = input()

    print(f"Ingresa el año que te graduaste de {titulo}")
    año = input()
    while not año.strip().isdigit():
        print("Ingresaste solo digitos:")
        año = input()
        
    titulo = {
        "institucion": institucion,
        "año": año
    }
    formacion.append(titulo)
    
#---------------------formacion academica-------------
def formacion_academica():
    while True:
        print("Tienes formacion academica?, solo digita(si/no)")
        academica = input().lower().strip()
        if academica == "si" or academica == "no":
            break
        else:
            print('solo puedes ingresar "si" o "no" como respuesta')
   
    if academica == "si":
        print("Te pediremos tus titulos uno por uno a continuacion:\n")
        print("Ingresa el titulo profesional que deseas agregar a tu hoja de vida")
        titulo = input()
        while not titulo.strip().replace(" ","").isalpha():
            print("Ingresaste numeros o caracteres, intenta de nuevo: ")
            titulo = input()

        print(f"Ingresa la institucion donde aquiriste el titulo de {titulo}")
        institucion = input()
        while not institucion.strip().replace(" ",""):
            print("No puedes dejarlo vacio, intenta de nuevo: ")
            institucion = input()

        print(f"Ingresa el año que te graduaste de {titulo}")
        año = input()
        while not año.strip().isdigit():
            print("Ingresaste solo digitos:")
            año = input()

        titulo = {
            "institucion": institucion,
            "año": año
        }
        formacion.append(titulo)

        print("Deseas registar otro titulo, solo digita (si/no)")
        pregunta = input()
        while not pregunta.lower().strip().replace(" ","").isalpha():
            if pregunta == "si" or pregunta == "no":
                break
            else:
                print('solo puedes ingresar "si" o "no" como respuesta:')
        
        if pregunta == "si":
            add_titulo()
        else:
            print()
    else:
        print()

#------------------experiencia----------------------
profesional = []

def experiencia_profesional(): 
    while True:
        while True:
            try:
                experiencia = input("Cuentas con alguna experiencia laboral (si/no): ").lower().strip()
                if experiencia.replace(" ", "").isalpha() and (experiencia == "si" or experiencia == "no"):              
                    break
                else:
                    print("Ingrese bien lo que se pide (si/no)")
            except Exception as e:
                print("Error inesperado")

        if experiencia == "si":
            empresa = input("Ingrese el nombre de la empresa: ").strip()
            while not empresa.replace(" ", "").isalpha():
                print("Ingrese un nombre de empresa válido")
                empresa = input("Ingrese el nombre de la empresa: ").strip()

            cargo = input("Ingrese el cargo que tenías: ").title().strip()
            while not cargo.replace(" ", "").isalpha():
                print("Ingrese un cargo válido")
                cargo = input("Ingrese el cargo que tenías: ").title().strip()

            funciones = input("Ingrese qué función tenías: ").title().strip()
            while not funciones.replace(" ", "").isalpha():
                print("Ingrese una función válida")
                funciones = input("Ingrese qué función tenías: ").title().strip()

            duracion = input("Ingrese la duración que tuviste en la empresa (ej. 1 año, 2 meses): ").strip()
            while not duracion.replace(" ", "").replace(",", "").isalnum():
                print("Ingrese una duración válida")
                duracion = input("Ingrese la duración que tuviste en la empresa (ej. 1 año, 2 meses): ").strip()

            experiencias = {
                "empresa": empresa,
                "cargo": cargo,
                "funciones": funciones,
                "duracion": duracion
            }
            profesional.append(experiencias)
        elif experiencia == "no":
            break

        agregar_mas = input("¿Desea agregar otra experiencia laboral? (si/no): ").lower().strip()
        while agregar_mas not in ["si", "no"]:
            print("Ingrese bien lo que se pide (si/no)")
            agregar_mas = input("¿Desea agregar otra experiencia laboral? (si/no): ").lower().strip()
        if agregar_mas == "no":
            break

#------------------referencias---------------------
referencias = []       
def referencias_personales_o_laborales():
    while True:
        try:
            agregar_referencia = input("Deseas agregar una referencia (si/no): ").lower()
            if agregar_referencia.replace(" ","").isalpha():
                if agregar_referencia == "si":
                    flat = True
                    while flat:
                        tipo_referencia = input("Deseas agregar una referencia (personal o laboral): ").lower()
                        if tipo_referencia == "personal":
                            nombre = input("Ingrese nombre de la referencia personal: ").title().strip()
                            flat = False
                            while nombre == "":
                                print("Solo son validos numeros y letras")

                            while True:
                                parentesco = input("Ingrese el parentesco de tu referencia personal: ")
                                if parentesco.isalpha():
                                    break       
                                else:
                                    print("Solo se permiten letras")

                            telefono = input("Ingrese el telefeno de tu referencia personal: ")
                            while not telefono.isdigit() or len((telefono)) < 7 or len((telefono)) > 10:
                                telefono = input("Numero invalido. Solo puedes ingresar digitos, minimo 7 numeros y maximo 10: ").strip() 

                            referencia_personal = {
                                "tipo": "personal",
                                "nombre": nombre,
                                "parentesco": parentesco,
                                "telefono": telefono,   
                            }
                            referencias.append(referencia_personal)
                            

                        if tipo_referencia == "laboral":
                            nombre = input("Ingrese nombre de la referencia laboral: ").title().strip()
                            flat = False

                            while nombre == "":
                                print("Solo son validos numeros y letras")

                            while True:
                                parentesco = input("Ingrese el parentesco de tu referencia personal: ")
                                if parentesco.isalpha():
                                    break       
                                else:
                                    print("Solo se permiten letras")

                            telefono = input("Ingrese el telefeno de tu referencia personal: ")
                            while not telefono.isdigit() or len((telefono)) < 7 or len((telefono)) > 10:
                                telefono = input("Numero invalido. Solo puedes ingresar digitos, minimo 7 numeros y maximo 10: ").strip() 

                            referencia_laboral = {
                                "tipo": "laboral",
                                "nombre": nombre,
                                "parentesco": parentesco,
                                "telefono": telefono,   
                            }
                            referencias.append(referencia_laboral)
                            
                elif agregar_referencia == "no":
                    break                   
        except ValueError:
            print("Ingresa correctamente")

#---------------habilidades--------------
def habilidades_certificaciones():
    habilidades = input("Ingresa tus habilidades o certificaciones adicionales (separa por guion (-) o deja vacío si no aplica):\n").strip().lower()
    if not habilidades:
        return set()
    lista_habilidades = [item.strip() for item in habilidades.split("-") if item.strip()]
    return set(lista_habilidades)

#----------------buscar por nombre-----------------
def consultar_por_nombre():
    nombre_buscar = input("Ingrese el nombre completo de la persona que desea buscar: ").title().strip()
    encontrado = False
    for nombre, datos in hoja_vida.items():
        if nombre == nombre_buscar:
            print("\n--- Hoja de vida encontrada ---")
            print(f"Nombre: {nombre}")
            print(f"Datos personales: {datos.get('datos_personales', {})}")
            print(f"Formación académica: {datos.get('formacion', [])}")
            print(f"Experiencia profesional: {datos.get('experiencia', [])}")
            print(f"Referencias: {datos.get('referencias', [])}")
            print(f"Habilidades: {datos.get('habilidades', set())}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ninguna hoja de vida con ese nombre.")

#----------------INICIA-----------------
while True:
    print("1. Datos personales ")
    print("2. Buscar hoja de vida por nombre")
    print("3. Actualizar informacion")
    print("4. Generar reporte")
    print("5. ")
    print("6. ")
    print("7. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        nombre, datos = datos_personales()
        formacion_academica()
        experiencia_profesional()
        referencias_personales_o_laborales()
        habilidades = habilidades_certificaciones()

        hoja_todos_datos = {
            "datos_personales": datos,
            "formacion": formacion.copy(),
            "experiencia": profesional.copy(),
            "referencias": referencias.copy(),
            "habilidades": habilidades
        }
        hoja_vida[nombre] = hoja_todos_datos

        # borrar datos ya ingresados
        formacion.clear()
        profesional.clear()
        referencias.clear()
        print("Hoja de vida registrada correctamente.")

    elif opcion == "2":
        consultar_por_nombre()
    elif opcion == "3":
        ()
    elif opcion == "4":
        ()
    elif opcion == "5":
        ()
    elif opcion == "6":
        ()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")