#Lote version python v1
import time
from typing import List
import os
import os
from utils.db import Database
from utils.utilitis import Util
from utils.writeFile import File
from variables import *


from datetime import datetime

#log
logName = "logApp.txt"
log_file = os.path.join(rutaArchivo, logName)
with open(log_file, "w") as log:
  outFile = os.path.join(rutaArchivo + "Deposito.txt")
  if not os.path.exists(outFile):
    print('No existe deposito en la ruta', rutaArchivo)
    log.write('No existe deposito en la ruta' + rutaArchivo + '\n')

  now = datetime.now()
  mes_proceso = now.strftime("%b").lower()

  print("actual", mes_proceso)

  mes_proceso = "mar"; #remove

  print("Mes: " + mes_proceso);
  dia, afiliado, monto, pan, cr = None, None, None, None, None
  #** dev
  # primero
  dirs_ad = File.get_dirs_of_dir_mes(rutaCredito, mes_proceso)

  print("Total carpetas credito:", len(dirs_ad));

  with open(outFile, "w") as out:
    #Primero
    credito = File.get_file_of_dir_credito(rutaCredito, mes_proceso, out, log) #credito
    print('Credito: ', len(credito))

    # segundo
    debito = File.get_file_of_dir_debito(rutaDebito, mes_proceso, out, log) #debito
    print('Debito: ', len(debito))
