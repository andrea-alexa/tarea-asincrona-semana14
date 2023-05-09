'''Se solicita crear un programa que permita ejecutar mediante una función, este deberá preguntar al usuario si quiere ejecutar el programa.
La función debe de tener una arrays esta tendrá los nombres de los departamentos del país, mediante un bucle for recorrerá los departamentos
registrados.
Luego solicitara al usuario ingresar el nombre de uno de los departamentos y este mostrar los municipios que el departamento ingresado por
el usuario estos deberán se deberán mostrar también mediante una arrays que será recorrida por un bucle for.
Luego indicar que, si desea consultar otro departamento, si su respuesta es no finalizar programa.
'''
#Inicio del programa
print("========================================================")
print("================ Bienvenido al programa ================")
print("========================================================\n")

#Empieza el nucleo del programa donde le preguntamos al usuario que si lo quiere usar
def start():
#Declaramos algunas varables y Arrays
    departamentos = ["Chalatenango", "Ahuachapán", "Cabañas", "Cuscatlán"]
#Con este boleano vamos a controlar el momento en el que se ejecute el programa
    pasar = False
#Iniciamos el bucle principal donde se van a realizar todas las interacciones
    while True:
#preguntamoms al usuario si quiere ejecutar el programa, además escribimos las variaciones de lo que pueda escribir el usuario y lo que aparezca lo controlamos con el boleano

        if not pasar:
            ejecucion = input("¿Desea ejecutar el programa? (Si/No): \n")
            if ejecucion.lower() == "no":
                print("Está bien, si desea usar el programa vuelva a ejecutar el código.")
                break
            elif ejecucion.lower() == "si":
                pasar = True
                print("¡Perfecto! ¡Estos son los departamentos disponibles!")
                print("===================================================================================")
                for departamento in departamentos:
                    print(departamento)
            else:
                print("Escriba una respuesta váida")
#en esta parte ponemos el else para que cuando el usuario quiera preguntar por otro depaartamento lo devuelva para esta parte
        else:
            print("===================================================================================")
#preguntamos de qué departamenot quiere saber los municipios
            selec_dep = input("De qué departamento quieres saber sus municipios?: \n")
# y dependiendo de lo que escriba hacemos una estructura if para abarcar todas esas posibilidades
            if selec_dep.capitalize() in departamentos: #usamos .capitalize() que es una herramienta que en este caso funciona como un .lower() o un .upper().
#hacemos otra estructura if para controlar la opcion que haya elegido el usuario
                if selec_dep.capitalize() == "Chalatenango":
#declaramos array con los municipios
                    chalatenango = ["Agua Caliente", "Arcatao", "Azacualpa", "Chalatenango", "Citalá", "Comalapa"]
                    print("Estos son los municipios del departamento de", selec_dep)
                    print("===================================================================================")
#y los imprimimos como una lista usando For. así con los demás departamentos
                    for municipio in chalatenango:
                        print(municipio)
                    print("===================================================================================")
                elif selec_dep.capitalize() == "Ahuachapán":
                    ahuachapan = ["Ahuachapán", "Apaneca", "Atiquizaya", "Concepción de Ataco", "El Refugio"]
                    print("===================================================================================")
                    print("Estos son los municipios del departamento de", selec_dep)
                    for municipio in ahuachapan:
                        print(municipio)
                    print("===================================================================================")
                elif selec_dep.capitalize() == "Cabañas":
                    la_libertad = ["Cojutepeque", "Candelaria", "El Carmen", "El Rosario", "Monte San Juan"]
                    print("Estos son los municipios del departamento de", selec_dep)
                    print("===================================================================================")
                    for municipio in la_libertad:
                        print(municipio)
                    print("===================================================================================")
                elif selec_dep.capitalize() == "Cuscatlán":
                    cuscatlan = ["Sensuntepeque", "Cinquera", "Dolores", "Guacotecti", "Ilobasco"]
                    print("===================================================================================")
                    print("Estos son los municipios del departamento de", selec_dep)
                    for municipio in cuscatlan:
                        print(municipio)
                    print("===================================================================================")
                else:
                    print("Ese departamento no se encuentra en la lista, intente de nuevo.")
                    continue
#luego le preguntamos al usuario si desea volver a usar el programa
                respuesta = input("¿Desea consultar otro departamento? (Si/No): ")
#hacemos un bucle por si el usuario se equivoca 
                while True:
#y construimos una estructura if para controlar las espuestas que nos pueda dar el usuario
                    if respuesta.lower() == "si":
                        break
                    elif respuesta.lower() == "no":
                        print("Está bien, Gracias por usar el programa")
                        return
                    else:
                        print("Respuesta no válida, por favor responda 'Si' o 'No'")
                        respuesta = input("¿Desea consultar otro departamento? (Si/No): ")
            else:
                print("Ese departamento no se encuentra en la lista elija otro")
                continue
#ponemos la funcion def para que funcione todo el programa   
start()
#y señalamos el fin del programa
print("Fin del programa, gracias por usar.")


                  
                  
         
         
         