
import sqlite3
conexion = sqlite3.connect("Clientes.db")
cursor = conexion.cursor()

# == CREAR LA DB
cursor.execute("""
               CREATE TABLE IF NOT EXISTS Clientes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   apellido TEXT NOT NULL,
                   correo TEXT NOT NULL
               )
               """)
conexion.commit()


# ======== FUNCIONES ==========

def agregar_clientes():
            nombre = input("Ingrese su nombre: ").upper().strip()
            apellido = input("Ingrese su apellido: ").title().strip()
            correo = input("ingrese su correo: ").strip().lower()
            
            if nombre == "" or apellido == "":
                print("Error, el nombre o el apellido no puede estar vacios.")
                return None
            
            if "@" not in correo or correo.count("@") != 1:
                print("Error, correo invalido")
                return None
            
            return nombre, apellido, correo
 
def ver_clientes():
    cursor.execute("Select * FROM Clientes ORDER BY id ASC")
    clientes = cursor.fetchall()
    
    if len(clientes) == 0:
        print("La base de datos se encuentra vacia.\n")
        return
    
    print("\n==Lista de clientes==")
    for id_cliente, nombre, apellido, correo in clientes:
        print(f"ID: {id_cliente} / Nombre: {nombre} / Apellido: {apellido} / Correo: {correo}")
    print()
          
def buscar_clientes():
    while True:
        buscar = input("Coloque el nombre de la persona que quiera buscar: ").upper().strip()
        if buscar == "":
            print("Error. El nombre no puede estar vacio.")
            continue
        return buscar
    
def eliminar_cliente():
    try:
        eliminar = int(input("A que cliente desea eliminar?: "))
        return eliminar
    except ValueError:
        print("Error. Coloque solo numeros ID.")
        return

def menu_principal():
    print("\n===Menu de clientes===")
    print("1. Agregar clientes.")
    print("2. Ver clientes.")
    print("3. Buscar clientes.")
    print("4. Eliminar clientes con ID.")
    print("5. Salir.")
    
           
                          
# =============================================================================



while True:
    menu_principal()
    try:
        opciones = int(input("Hola! Bienvenido al sistema de clientes, por favor coloque que opcion desea: "))
        if opciones < 1 or opciones > 5:
            print("Error, coloco un numero fuera del rango, las opciones validas son de 1 al 5.")
            continue
    except ValueError:
        print("Error. Coloque solo numeros.")
        continue
  
# == AGREGAR CLIENTES  
    if opciones == 1:
        datos = agregar_clientes()
        if datos:
            cursor.execute("""
               INSERT INTO clientes (nombre, apellido, correo)
               VALUES (?,?,?)
               """, datos)            
            conexion.commit()
            print("Cliente agregado correctamente")
        else:
            print("No se pudo agregar el cliente.")
        
# == VER LOS CLIENTES DE LA DB       
    if opciones == 2:
        ver_clientes()
        
   
# == BUSCAR CLIENTES DE LA DB
    if opciones == 3:
        persona_buscada = buscar_clientes()
        cursor.execute("select * from clientes where nombre = ?", (persona_buscada,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Cliente no encontrado")
            continue
        else:
            id_cliente, nombre, apellido, correo = resultado
    
            print("\nCliente encontrado: ")
            print(f"Id: {id_cliente}")
            print(f"Nombre:  {nombre}")
            print(f"Apellido: {apellido}")
            print(f"Correo: {correo}")
    
# == ELIMINAR CLIENTE
    if opciones == 4:
        ver_clientes()
        persona_eliminada = eliminar_cliente()
        cursor.execute("Select * from clientes where id = ?", (persona_eliminada,))
        resultado = cursor.fetchone()

        if persona_eliminada is None:
            continue
        else:
            id_cliente, nombre, apellido, correo = resultado
    
            cursor.execute("Delete from clientes where id = ?", (persona_eliminada,))
            conexion.commit()
 
            print("\nCliente encontrado y eliminado: ")
            print(f"Id_Cliente: {id_cliente}")
            print(f"Nombre: {nombre}")
            print(f"Apellido: {apellido}")
            print(f"Correo: {correo}")
    
# == SALIR
    if opciones == 5:
        print("Saliendo de las base de datos!")
        conexion.close()
        break
    
    
   

     