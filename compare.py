import os


def comparar_archivos(ruta, python, java):
    ruta_python = os.path.join(ruta, python)
    ruta_java = os.path.join(ruta, java)
    
    lineas_diferentes = []
    
    with open(ruta_python, 'r') as file_python, open(ruta_java, 'r') as file_java:
        linea_python = file_python.readlines()
        linea_java = file_java.readlines()
        
        cont = 0
        for i, linea in enumerate(linea_python):
            cont += 1;
            if linea != linea_java[i]:
                print("La siguiente linea es diferente linea:", cont, "file", python)
                print('java')
                print(linea_java[i])
                print('---------------')
                print('python')
                print(linea)
                return 1
    
    return lineas_diferentes


ruta = "C:/archivos"
python = "Deposito_python.txt"
java = "Deposito_java.txt"

lineas_diferentes = comparar_archivos(ruta, python, java)

if lineas_diferentes == 0:
    print("No se encontraron diferencias en los archivos.")
