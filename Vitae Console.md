Vitae Console

Este es un sistema sencillo para registrar y consultar hojas de vida, pensado para cualquier tipo de usuario que quiera gestionar información personal, académica y profesional de diferentes personas de manera fácil.

Descripcion general del sistema

Vitae Console permite:
- Registrar una hoja de vida con datos personales, formación académica, experiencia profesional, referencias y habilidades.
- Almacenar varias hojas de vida y consultarlas por nombre.
- Todos los datos se ingresan y consultan desde un menú interactivo en la terminal.
- Los mensajes y validaciones ayudan a que el usuario sepa qué hacer en cada paso.

Paso a paso para ejecutar el programa

1 Verifica que tienes Python 3 instalado. En Linux puedes comprobarlo con:
   python3 -version
2 Descarga el archivo hoja_vida_busqueda.py y guárdalo en la carpeta Descargas.
3 Abre la terminal en Linux.
4 Ve a la carpeta Descargas con el comando:
   cd ~/Descargas
5 Ejecuta el programa con:
   python3 HDV_B_I_A.py
6 Si quieres ver o editar el código, abre Visual Studio Code, elige "Abrir carpeta" y selecciona la carpeta Descargas, luego haz doble clic sobre HDV_B_I_A.py.

Librerías utilizadas y cómo instalarlas

El programa utiliza:
- datetime: ya viene incluida en Python, no necesitas instalar nada más.

No necesitas instalar ninguna otra librería. Solo asegúrate de tener Python 3.

Ejemplo de uso paso a paso

Al ejecutar el programa verás un menú como este:

1 Datos personales
2 Consultar por nombre
3 Actualizar informacion
4 Generar reporte
5.
6.
7 Salir
Ingrese su opción:

Registrar una hoja de vida

Elige la opción 1 y presiona Enter. El programa te pedirá los siguientes datos uno por uno:

Ingrese su numero de identificacion: 123456789
Si ingresas letras o dejas vacío, te pedirá solo números.

Ingresa tu nombre completo Juan Perez
Si dejas vacío, te pedirá de nuevo el nombre.

Ingrese tu numero de contacto: 3201234567
Debe tener entre 7 y 10 dígitos, si no, te pedirá otro número.

Ingrese tu direccion de residencia: Calle 123
No puede quedar vacío.

Ingrese tu correo electronico: juan@gmail.com
Debe contener @ y punto, si no, te lo pedirá otra vez.

Ingrese tu fecha de nacimiento separado por '/' :(DD/MM/AAAA): 15/05/2000
Si el formato es incorrecto, te muestra un mensaje y pide de nuevo la fecha.

Tienes formacion academica?, solo digita(si/no) si
Si contestas "si", te pedirá:
- título profesional (solo letras)
- institución (no vacío)
- año de graduación (solo dígitos)
Puedes agregar más títulos si quieres.

Cuentas con alguna experiencia laboral (si/no): si
Si contestas "si", te pedirá:
- nombre de la empresa (solo letras)
- cargo (solo letras)
- función (solo letras)
- duración (ejemplo: 2 años)
Puedes agregar más experiencias si quieres.

Deseas agregar una referencia (si/no): si
Si contestas "si", puedes agregar referencias personales o laborales, con nombre, parentesco y teléfono.

Ingresa tus habilidades o certificaciones adicionales (separa por guion (-) o deja vacío si no aplica): python - excel

Al terminar, verás:
Hoja de vida registrada correctamente.

Consultar por nombre

Elige la opción 2 y presiona Enter.
Te pedirá el nombre completo de la persona. Si existe una hoja de vida registrada con ese nombre, te mostrará todos los datos. Si no, verás:
No se encontró ninguna hoja de vida con ese nombre.

Salir del programa

Elige la opción 7 y presiona Enter para salir.
En esta opcion el programa dejara de ejecutarse.

Ejemplo de registro y consulta

Ingrese su opción: 1
Ingrese su numero de identificacion: 123456789
Ingresa tu nombre completo Juan Perez
Ingrese tu numero de contacto: 3124567890
Ingrese tu direccion de residencia: Calle 123
Ingrese tu correo electronico: juan@email.com
Ingrese tu fecha de nacimiento separado por '/' :(DD/MM/AAAA): 15/05/2000
Tienes formacion academica?, solo digita(si/no) si
Ingresa el titulo profesional que deseas agregar a tu hoja de vida Ingeniero
Ingresa la institucion donde aquiriste el titulo de Ingeniero Universidad X
Ingresa el año que te graduaste de Ingeniero 2022
Deseas registar otro titulo, solo digita (si/no) no
Cuentas con alguna experiencia laboral (si/no): no
Deseas agregar una referencia (si/no): no
Ingresa tus habilidades o certificaciones adicionales (separa por guion (-) o deja vacío si no aplica):

Hoja de vida registrada correctamente.

Luego puedes consultarla usando el nombre con la opción 2.

Siguiendo todas las instrucciones anteriores podras interactuar con el programa cuanto desees.

integrantes: 
Brandon Stiven Arredondo Muñoz - Berners lee  
Isabella Pulgarin Muñoz - Ritchie  
Adrian Alesis Arboleda Calle - Berners lee