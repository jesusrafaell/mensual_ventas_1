import os
from datetime import datetime
from utils.writeFile import File
from variables import *

#log
logName = "logApp.txt"
log_file = os.path.join(rutaArchivo, logName)
with open(log_file, "w") as log:
  outFile = os.path.join(rutaArchivo + "Deposito.txt")
  #if not os.path.exists(outFile):
    #print('No existe deposito en la ruta', rutaArchivo)
    #log.write('No existe deposito en la ruta' + rutaArchivo + '\n')

  now = datetime.now()
  mes_actual = now.month
  anio_actual = now.year

  #Diccionario de nombres de meses en español
  meses_espanol = {
      1: "ene",
      2: "feb",
      3: "mar",
      4: "abr",
      5: "may",
      6: "jun",
      7: "jul",
      8: "ago",
      9: "sep",
      10: "oct",
      11: "nov",
      12: "dic"
  }

  now = datetime.now()
  mes_actual = now.month
  anio_actual = now.year

  if mes_actual == 1:  # Si es enero, el mes anterior es diciembre del año anterior
      mes_anterior = 12
      anio_anterior = anio_actual - 1
  else:
      mes_anterior = mes_actual - 1
      anio_anterior = anio_actual

  fecha_anterior = datetime(anio_anterior, mes_anterior, 1)

  # mes_proceso = fecha_anterior.strftime("%b").lower()

  mes_proceso = meses_espanol[mes_anterior]

  print("Mes anterior:", mes_proceso)

  # mes_proceso = "mar"; #remove

  print("Mes: " + mes_proceso,outFile );
  # primero
  # pdirs_ad = File.get_dirs_of_dir_mes(rutaCredito, mes_proceso)

  # pprint("Total carpetas credito:", len(dirs_ad));

  with open(outFile, "w") as out:
    #Primero
    credito = File.get_file_of_dir_credito(rutaCredito, mes_proceso, out, log) #credito
    print('Credito: ', len(credito))

    # segundo
    debito = File.get_file_of_dir_debito(rutaDebito, mes_proceso, out, log) #debito
    print('Debito: ', len(debito))
