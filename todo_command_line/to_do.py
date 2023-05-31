to_do_list = {}

def create():
    index = len(to_do_list) + 1
    tarea = input("ingrese su tarea: ")
    to_do_list.update({
        f"{index}":{
            "tarea":tarea,
            "estado":"pendiente"
        }
    })

def read():
    for item in to_do_list.items():
        print(item)

def update():
    read()
    index = input("Seleccione el index de la tarea actualizar: ")
    print(to_do_list[index])
    selector = input("1.Pendiente\n2.En progreso\n3.Terminado\n")
    if selector == "1": estado = "Pendiente"
    if selector == "2": estado = "En progreso"
    if selector == "3": estado = "Terminado"
    to_do_list[index]["estado"] = estado
    print(to_do_list[index])

while True:
    print("""
            1. Crear una nueva tarea.
            2. mostrar las tareas.
            3. Actualizar una tarea.
        """)
    selection = input("Seleccione una opción: ")

    if selection == "1":
        create()
    
    if selection == "2":
        read()

    if selection == "3":
        update()
    
    else:
        print("Selección invalida".center(50,"*"))

    print("=="*50)