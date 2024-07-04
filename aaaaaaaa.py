import csv

with open('tss.csv', 'w', newline='') as tss_csv:
    escritor_csv = csv.writer(tss_csv)
    writer = csv.writer(tss.csv)
    writer.writerow([[]])
    
    
    
    
    
    
def menu(): 
     print("1, reservar habitacion:")
     print("2, buscar habitacion disponible:  ")
     print("3, estado habitacion:  ")
     print("4, ventas diarias: ")
     print("5, guardar informacion: ")
     print("6, salir:  ")
     
def  reserva_habitacion():
        usuario = input("ingrese el nombre del responsable: ")
        apellido = input("ingrese su apellido:  ")
        rut_responsable = int(input("rut del responsable, si termina en K remplazalo por un 1 :  "))
        buscador_habitacion = int(input("busca una habitacion del (1-40):"))
        hora_de_llegada = time.now(input("ingresa hora de llegada: "))
        
def buscar_habitacion():
    for habitacion in range(8):
        print(habitacion)
        for piso in range(6):
            print(piso)
    codigo = int(input("debes ingresar tu codigo:", codigo))

def estado_habitacion():
    disponibles = "-"
    ocupadas = "-"

def ventas():
    ventas_diarias = ventas_diarias + date.now().strftime("%d-%m-%Y-%H:%M:%S")

def guardar():  
  print("asdasdas")
  

       
while True: 
    menu()
    try: 
        opciones = int(input("debes ingresar un numero de (1-6):   "))
    except ValueError:
        print("debes ingresar un numero valido :c  ")
    if opciones == 1:
        reserva_habitacion()
        print("tu codigo de usuario para buscar una habitacion es 1234")
    if opciones == 2:
        buscar_habitacion()
    if opciones == 3:
        estado_habitacion()
    if opciones == 4:
        ventas()
    if opciones ==  5:
        guardar()
    elif opciones == 6:
        print("saliste del hostal")
    
        
print( "  -----  m   ---------")
print( "  ------   e ---------")
print( "  ------  f  ---------")
print( "  ------  u  ---------")
print( "  ------   e ---------")
print( "  ------  m  ---------")
print( "  ------   a ---------")
print( "  ------  l  ---------")

