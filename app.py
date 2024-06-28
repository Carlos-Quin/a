from modules.construccion import sol_ans, listar, limpieza, recuperar_data, existencia, mostrar_elementos, sol_data, buscar, exportar, sol_code, eliminar
from modules.data import rutaj, menup, rutac

while True:
    listar(menup)
    ans = sol_ans()
    limpieza()
    if ans == '1':
        existencia(rutaj)
        cont = recuperar_data(rutaj)
        mostrar_elementos(cont)
    elif ans == '2':
        buscar(rutaj, sol_data())
    elif ans == '3':
        pass
    elif ans == '4':
        eliminar(rutaj, sol_code())
    elif ans == '5':
        exportar(rutaj, rutac)
    else:
        print('Opción no válida\n')