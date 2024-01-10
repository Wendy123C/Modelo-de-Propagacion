import math #Importación del math para tener acceso a funciones matematicas como es el caso de logaritmo

# Función para calcular a(hr) para ciudad mediana
def a_hr_ciudad_mediana(fc, hr): #Permite definir una función q calcule y devuelva un valor.
    return (1.1 * math.log10(fc) - 0.7) * hr - (1.56 * math.log10(fc) - 0.8)  #Realiza el calculo y devuelve el resultado.

# Pérdida de trayectoria para una ciudad mediana 
def perdida_ciudad_mediana(fc, ht, hr, d):  #define una funcion que permita calcular la perdida de trayectoria.
    return 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - a_hr_ciudad_mediana(fc, hr) + (44.9 - 6.55 * math.log10(ht)) * math.log10(d)  #Calcula la perdida y devuelve el resultado

#Función para calcular A(hr) para gran ciudad cuando fc <= 300 MHz
def A_hr_menor_frecuencia(hr):
    return 8.29*(math.log10(1.54*hr))**2 -1.1

# Función para calcular A(hr) para gran ciudad cuando fc >= 300 MHz
def A_hr_mayor_frecuencia(hr):
    return 3.2 * (math.log10(11.75 * hr))** 2 - 4.97

# Pérdida de trayectoria para una gran ciudad
def perdida_gran_ciudad(fc, ht, hr, d):
    if 150 <= fc <= 1500:          #Comprueva que la frecuencia sea menor o igual a 300 MHz para saber cual de las funciones se va a utilizar
        ahr = A_hr_menor_frecuencia(hr) # Dentro de esta condicion se verifica si la frecuencia es menor para hacer uso de la funcion de menor frecuencia 
    else:
        ahr = A_hr_mayor_frecuencia(hr)   # Dentro de esta condicion se verifica si la frecuencia es mayor para hacer uso de la funcion de mayor frecuencia 
    return 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - ahr + (44.9 - 6.55 * math.log10(ht)) * math.log10(d) #Calcula la perdida total para una gran ciudad y devuelve el resultado

#Perdida de trayectoria de extención PSC modelo Hata para una ciudad mediana

def perdida_PSC_ciudad_mediana(fc, hbs, hr, d, cm):
    a_hr = a_hr_ciudad_mediana(fc, hr)
    return 46.3 + 33.9 * math.log10(fc)- 13.82 * math.log10(hbs) - a_hr + (44.9 - 6.55 * math.log10(hbs))* math.log10(d) + cm
#Perdida de trayectoria de extención PSC modelo Hata para una gran ciudad
def perdida_PSC_gran_ciudad(fc, hbs, hr, d, cm):
    #Calculo de perdida de trayectoria de la extencion PSC del modelo hata
    if 1500 <= fc <= 2000:
        ahr = A_hr_menor_frecuencia(hr) # Dentro de esta condicion se verifica si la frecuencia es menor para hacer uso de la funcion de menor frecuencia 
    else:
        ahr = A_hr_mayor_frecuencia(hr)
    return 46.3 + 33.9 * math.log10(fc)- 13.82 * math.log10(hbs) - ahr + (44.9 - 6.55 * math.log10(hbs))* math.log10(d) + cm

# Pérdida de trayectoria para un entorno suburbano
def perdida_suburbana(fc, ht, hr, d):
    P_suburbana = perdida_ciudad_mediana(fc, ht, hr, d)
    return P_suburbana - 2 * (math.log10(fc / 28))**2 - 5.4

# Pérdida de trayectoria para un entorno rural
def perdida_rural(fc, ht, hr, d):
    P_rural = perdida_ciudad_mediana(fc, ht, hr, d)
    return P_rural - 4.78 * (math.log10(fc))**2 - 18.733 * math.log10(fc) - 40.98

# Pérdida de trayectoria para el espacio libre
def perdida_espacio_libre(fc, d, n): #Define esta funcion para calcular la perdida de trayectoria en el espacio libre
    return 20 * math.log10(fc*10**9) + 10 * n * math.log10(d*10**3) - 147.56 #Realiza el calculo para el espacio libre y devuelve el resultado

def obtener_entrada_numerica(mensaje): # Define una funcion que agarre el armunento mensaje para que el usuario ingrese una entrada numerica valida y convertirla a flotante.
            while True:   # Blucle infinito. Este se ejecuta hasta que se encuentre una instruccion return
                try:   #manejo de excepciones. En caso de que halla un error se pasara a la sepcion except
                    valor = float(input(mensaje)) # Muestra el mensaje y espera la entrada. Posteriormente esta entrada la convierte en un numero flotante
                    return valor    # Si la conversion es correcta devuelve el valor flotante y se da por terminado el bloque
                except ValueError:
                    print("Por favor, ingrese un número válido.") # En caso de haber un error el programa le presenta ese mensaje.

def main():
   
    print("\nSeleccione el modelo de propagación:") 
    print("1. Modelo de Okumura-Hata")
    print("2. Pérdida de trayectoria en el espacio libre")
    print("3. Extensión PSC Modelo Hata")

    modelo_propagacion = int(input("Ingrese el número correspondiente al modelo: "))#Guarda en la variable modelo_propagacion la opcion que eligio el ususario

    if modelo_propagacion == 1:
        print("\nSeleccione el tipo de zona:")
        print("1. Ciudad Mediana")
        print("2. Gran Ciudad")
        print("3. Suburbana")
        print("4. Rural")

        seleccion_zona = int(input("Ingrese el número correspondiente a la zona: "))

        # Solicitando los valores al usuario
        fc = float(input("Ingrese la frecuencia (MHz): "))
        ht = float(input("Ingrese la altura de la antena transmisora (m): "))
        hr = float(input("Ingrese la altura de la antena receptora (m): "))
        d = float(input("Ingrese la distancia entre las antenas (km): "))
                


        if seleccion_zona == 1:
            perdida = perdida_ciudad_mediana(fc, ht, hr, d)
            zona = "Ciudad Mediana"
        elif seleccion_zona == 2:
            perdida = perdida_gran_ciudad(fc, ht, hr, d)
            zona = "Gran Ciuda"
        elif seleccion_zona == 3:
            perdida = perdida_suburbana(fc, ht, hr, d)
            zona = "Suburbana"
        elif seleccion_zona == 4:
            perdida = perdida_rural(fc, ht, hr, d)
            zona = "Rural"
        else:
            print("Opción no válida para la zona.")
            zona = ""
    elif modelo_propagacion == 2:
        # Menú para el espacio libre con los exponentes de pérdida de trayectoria
        print("\nSeleccione el exponente de pérdida de trayectoria para Espacio Libre:")
        print("1. Espacio libre (n=2)")
        print("2. Radio celular en área urbana (n = 3.5)")
        print("3. Radio celular con sombra (n = 5)")
        print("4. Línea de vista dentro del edificio (n = 1.8)")
        print("5. Obstruido en edificio (n = 6)")
        print("6. Obstruido en fábricas (n = 3)")

        seleccion_espacio_libre = int(input("Ingrese el número correspondiente al exponente: ")) # Se cuarda el valor en seleccion_espacio_libre

        # Solicitando los valores al usuario
        fc = float(input("Ingrese la frecuencia (GHz): "))
        d = float(input("Ingrese la distancia entre las antenas (km): "))
        n = float(input("Ingrese el exponente de perdida de trayectoria (n): "))

        # Asumiendo valores medios para los exponentes de pérdida de trayectoria
        exponentes = [2, 3.5, 5, 1.8, 6, 3]

        if 1 <= seleccion_espacio_libre <= len(exponentes):  # Verifica si el numero ingresado es valido
            n = exponentes[seleccion_espacio_libre - 1] # Asiga a n el valoror que corresponde al exponente
            perdida = perdida_espacio_libre(fc, d, n)    # llama a la funcion 
            zona = "Espacio Libre con exponente " + str(n)   #  Asigna a la variable zona una cadena de texto la cual indica el calculo de perdida de trayectoria del exponente seleccionado
        else:
            print("Opción no válida")
            perdida = None # Indica que no se pudo calcular la perdida seleccion no valida
            zona = ""

    elif modelo_propagacion == 3:
        print("\nSeleccione el tipo de ciudad:")
        print("1. Ciudad mediana")
        print("2. Gran Ciudad")
        
        seleccion_PSC_hata = int(input("Ingrese el número correspondiente a la ciudad: "))

        print("\nSeleccione el tipo de zona:")
        print("1. Urbano")
        print("2. Suburbano")

        seleccion_PSC_zona = int(input("Ingrese el número correspondiente a la ciudad: "))

        fc = obtener_entrada_numerica("Ingrese la frecuencia (MHz): ")
        hbs = obtener_entrada_numerica("Ingrese la altura de la antena transmisora (m): ")
        hr = obtener_entrada_numerica("Ingrese la altura de la antena receptora (m): ")
        d = obtener_entrada_numerica("Ingrese la distancia entre las antenas (km): ")
        cm = obtener_entrada_numerica("Ingrese el desplazamento constante (CM): ")

        if seleccion_PSC_hata == 1:
            if seleccion_PSC_zona == 1: 
                perdida = perdida_PSC_ciudad_mediana(fc, hbs, hr, d, cm)
                zona = "Urbano"
            else:
                perdida = perdida_PSC_ciudad_mediana(fc, hbs, hr, d, cm)
                zona = "Suburbano"
        elif seleccion_PSC_hata == 2:
            if seleccion_PSC_zona == 1: 
                perdida = perdida_PSC_gran_ciudad(fc, hbs, hr, d, cm)
                zona = "Urbano"
            else:
                perdida = perdida_PSC_gran_ciudad(fc, hbs, hr, d, cm)
                zona = "Suburbano"
        else:
            print("Opción no válida para la zona.")
            zona = ""
         
    # Mostrar resultado de la pérdida de trayectoria
    if perdida is not None:
        print(f"Pérdida de trayectoria en {zona}: {perdida:.2f} dB")

        
if __name__ == "__main__":
    main ()
