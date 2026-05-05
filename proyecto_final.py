import sqlite3

#def crear_tabla():
#    conexion = sqlite3.connect("Base_Datos.db")
#    cursor = conexion.cursor()
#    cursor.execute('''CREATE TABLE IF NOT EXISTS Inventario ( id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, descripcion TEXT, cantidad INTEGER, precio INTEGER, categoria TEXT)''')
#    conexion.commit()
#    conexion.close()

def cargar_productos_sql():
    conexion = sqlite3.connect("Base_Datos.db")
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    descripcion = input("Ingrese la descripcion del producto: ").capitalize()
    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad <= 0:
                print("Ingrese una cantidad mayor a 0")
        except ValueError:
            print("Ingrese una cantidad")
    precio = 0.0
    while precio <= 0:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio <= 0:
                print("Ingrese un precio mayor a 0")
        except ValueError:
            print("Ingrese un precio")
    categoria = input("Ingrese la categoria: ").capitalize()
    cursor.execute('''INSERT INTO Inventario (nombre,descripcion,cantidad,precio,categoria) VALUES (?,?,?,?,?) ''',(nombre,descripcion,cantidad,precio,categoria))
    conexion.commit()
    conexion.close()

def mostrar_productos_sql():
    conexion = sqlite3.connect("Base_Datos.db")
    cursor = conexion.cursor()    
    cursor.execute("SELECT* FROM Inventario")
    resultado = cursor.fetchall()
    print(f"{"codigo":<10}{"nombre":<20}{"descripcion":<20}{"cantidad":<10}{"precio":<10}{"categoria":<10}")
    for registro in resultado:
        print(f"{registro[0]:<10}{registro[1]:<20}{registro[2]:<20}{registro[3]:<10}{registro[4]:<10}{registro[5]:<10}")   
    conexion.close()

def actualizar_producto_sql():
    conexion = sqlite3.connect("Base_Datos.db")
    cursor = conexion.cursor()   
    print("Estos son los productos registrados")
    mostrar_productos_sql() 
    id = 0
    while id <= 0:
        try:
            id = int(input("Ingrese id a actualizar: "))
            if id <= 0:
                print("Ingrese un numero mayor 0")
        except ValueError:
            print("Ingrese un numero")
            id = 0
    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese la cantidad nueva: "))
            if cantidad < 0:
                print("Ingres un numero mayor a 0")
        except ValueError:
            print("Ingrese un numero")
            cantidad = 0
    print("Si el id ingresado no se encuentra en lista, no se agregara y tampoco afectara en la lista")
    cursor.execute("UPDATE Inventario SET cantidad = ? WHERE id = ?",(cantidad,id))
    conexion.commit()
    conexion.close()

def eliminar_producto():
    conexion = sqlite3.connect("Base_Datos.db")
    cursor = conexion.cursor()
    id = 0
    while id <= 0:
        try:
            id = int(input("Ingrese id a eliminar: "))
            if id <= 0:
                print("Ingrese un numero mayor 0")
        except ValueError:
            print("Ingrese un numero")
            id = 0
    cursor.execute("DELETE FROM Inventario WHERE id = ?",(id,))
    print("Si el id ingresado no se encuentra en lista, la misma no sera modificada")
    conexion.commit()
    conexion.close()

def buscar_producto():
    conexion = sqlite3.connect("Base_Datos.db")
    cursor = conexion.cursor()
    mostrar_productos_sql()
    id = 0
    while id <= 0:
        try:
            id = int(input("Ingrese id a buscar: "))
            if id <= 0:
                print("Ingrese un numero mayor 0")
        except ValueError:
            print("Ingrese un numero")
            id = 0
    cursor.execute("SELECT* FROM Inventario WHERE id = ?",(id,))
    resultado = cursor.fetchone()
    if resultado != None:
        print(f"Id: {resultado[0]}",
              "Nombre: ", resultado[1],
              "Descripcion: ", resultado[2],
              "Cantidad: ", resultado[3],
              "Precio: ", resultado[4],
              "Categoria: ", resultado[5])
    else:
        print("Id no encontrado")
    conexion.commit()
    conexion.close()

def reporte_stock_bajo():
    mostrar_productos_sql()
    import sqlite3
    conexion = sqlite3.connect("Base_Datos.db")
    cursor = conexion.cursor()
    minimo = 0
    while minimo <= 0:
        try:
            minimo = int(input("Ingrese la cantidad minimo de stock: "))
            if minimo <= 0:
                print("Ingrese un numero mayor 0")
        except ValueError:
            print("Ingrese un numero")
            minimo = 0
    cursor.execute("SELECT* FROM Inventario WHERE cantidad < ?",(minimo,))
    resultado = cursor.fetchall()
    cant = len(resultado)
    if cant > 1:
        print("Los productos con stock bajo son: ")
        for producto in resultado:
                print(f"Id:{producto[0]}",
                    "Nombre:",producto[1],
                    "Descripcion:",producto[2],
                    "Cantidad:",producto[3],
                    "Precio:",producto[4],
                    "Categoria:",producto[5])
    elif cant == 1:
        print("El producto con stock bajo es: ")
        print(resultado)
        ##print(f"Id:{resultado[0]}","Nombre: ", resultado[1],"Descripcion: ", resultado[2],"Cantidad: ", resultado[3],"Precio: ", resultado[4],"Categoria: ", resultado[5])
    else:
        print("No se encontro productos con stock bajo")
    conexion.commit()
    conexion.close()

def menu_opcines():
    menu = True
    while menu:
        print("\nMenu Principal.\n")
        opcion=input("----------------------------------------------"
                     "\n\t\t***menu***"
                     "\n----------------------------------------------"
                     "\n 1. registro producto."
                     "\n 2. mostrar prouctos."
                     "\n 3. actualizar productos."
                     "\n 4. eliminar producto."
                     "\n 5. buscar producto."
                     "\n 6. reportar stock bajo."
                     "\n 7. salir."
                     "\n ingrese opciones (1-7): ").lower()
        if opcion=="1":
            cargar_productos_sql()
        elif opcion=="2":
            mostrar_productos_sql()
        elif opcion=="3":
            actualizar_producto_sql()
        elif opcion=="4":
            eliminar_producto()
        elif opcion=="5":
            buscar_producto()
        elif opcion=="6":
            reporte_stock_bajo()
        elif opcion=="7":
            menu=False
        else:
            print("Opcion incorrecta.")


menu_opcines()