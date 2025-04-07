print ("1.- Longitud de una frase")
print ("2.- Encontrar cuadrante")
print ("3.- Salir")

opciones = int(input("Seleccione que desea hacer: "))
#uso del ciclo while para hacer el menú de opciones
while opciones >= 1 and opciones <= 3:
    
    if opciones == 1:
        #se usa la funcion len para obtener el numero de caracteres que ingreso el usuario
        palabra = input("Ingrese una palabra de 4 y 8 letras:")
        long = str(len(palabra))
        #mientras la palabra que ingreso el usuario sea mayor igual a 4 y menor igual a 8 se ejecutara el escenario correcto
        if len(palabra) >=4 and len(palabra) <=8:
            
            print("la palabra es correcta, tiene " + long + " letras")
            
            break
        elif len(palabra) <4:
            
            print("Hacen falta letras. Solo tiene " + long + " letras")
            #no inserto un brake ya que debe repetirse hasta que el usario ingrese el escenario correcto
        elif len(palabra) >8:
            
            print("Sobran letras. Tiene " + long + " letras")
    
    elif opciones == 2:
        
        x = int (input("Ingrese el valor de X:"))
        y = int (input("Ingrese el valor de Y:"))
        #para este ejercicio me parecio un buen ejemplo para el uso de if else 
        if x == 0 and y == 0:
            
            print("El punto se encuentra en el origen")
            break
            
        elif x == 0:
            
            print("El punto se encuentra en el eje Y")
            break
        
        elif y == 0:
            
            print("El punto se encuentra en el eje X")
            break
        
        elif x > 0 and y > 0:
            
            print("El punto se encuentra en el cuadrante I")
            break
        
        elif x < 0 and y > 0:
            
            print("El punto se encuentra en el cuadrante II")
            break
        
        elif x < 0 and y < 0:
            
            print("El punto se encuentra en el cuadrante III")
            break
        
        elif x > 0 and y < 0:
            
            print("El punto se encuentra en el cuadrante IV")
            break      
        
    elif opciones == 3:
        print("Hasta luego")
        break
                

        

            
            
            
        
        
        
        
        