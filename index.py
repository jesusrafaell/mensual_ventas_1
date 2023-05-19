#Lote version python v1
import time
from typing import List
import os
from classes.Resumen import Resumen
import os
from utils.db import Database
from utils.utilitis import Util
from utils.writeFile import File
from variables import *


from datetime import datetime

db = Database
cnxn = db.conectar()
ahora = datetime.now()
resultado = []
strDate = time.strftime("%y%m%d")
strDate = "230301"  # Test specific date
control = excelControl = 0
print(strDate)


#log
logName = "logApp.txt"
log_file = os.path.join(rutaArchivo, logName)
with open(log_file, "w") as log:
  if (cnxn):
    print("conected DB")
    outFile = os.path.join(rutaArchivo + "Deposito.txt")
    if not os.path.exists(outFile):
      print('No existe deposito en la ruta', rutaArchivo)

    now = datetime.now()
    mes_proceso = now.strftime("%b").lower()

    print("actual", mes_proceso)

    mes_proceso = "mar"; #remove

    print("Mes: " + mes_proceso);
    dia, afiliado, monto, pan, cr = None, None, None, None, None
    #** dev
    # primero
    dirs_ad = File.get_dirs_of_dir_mes(rutaCredito, mes_proceso) #credito
    # segundo
    dirs_x = File.get_dirs_of_dir_mes(rutaDebito, mes_proceso) #debito FTP720

    print("Total carpetas credito:", len(dirs_ad));
    print("Total carpetas debito:",len(dirs_x));
    # List<String> arcContent;
    arcContent = List[str]
    theProcess = None
    inStream = None


    if not os.path.exists(rutaArchivo):
      os.makedirs(rutaArchivo)

    with open(outFile, "w") as out:
      # Credito
      for d in dirs_ad:
        print('Archivo:', d)
        with open(d, "r") as file:
          for linea in file:
            print(linea)
        # file = File.get_files_of_dir(f"{rutaCredito}{d}", "FCPUTC57.860")

        print(d)
        # print(file)
        # dia = Util.mid(f, 10, 3)
        print('dia:', dia)
        for l in d:
          switch = l.substring(166).strip()
          if switch == "10":
            afiliado = Util.mid(l, 93, 9)
          elif switch == "20":
              monto = Util.mid(l, 22, 12)
              pan = Util.mid(l, 49, 19)
              cr = "" if Util.mid(l, 76, 1) == "5" else "-"
              if Util.left(pan, 1) == "4":
                  if Util.containsAny(Util.left(pan, 6), "422044", "422045", "422046", "446334", "425881"):
                      f.write("{0}{1};{2};{3};0;0;0;0;0;0;0;0;1;{4}{5};0;0;0;0\n".format(afiliado, Util.mid(l, 153, 8), pan, dia, cr, monto))
                  else:
                      f.write("{0}{1};{2};{3};0;0;0;0;0;0;1;{4}{5};0;0;0;0;0;0\n".format(afiliado, Util.mid(l, 153, 8), pan, dia, cr, monto))
              elif Util.left(pan, 1) == "0":
                  f.write("{0}{1};{2};{3};0;0;0;0;1;{4}{5};0;0;0;0;0;0;0;0\n".format(afiliado, Util.mid(l, 153, 8), pan, dia, cr, monto))
              elif int(Util.left(pan, 2)) * 1 >= 51 and int(Util.left(pan, 2)) * 1 <= 57:
                  if Util.containsAny(Util.left(pan, 6), "520148", "528004", "515673", "552327", "520154"):
                      f.write("{0}{1};{2};{3};0;0;0;0;0;0;0;0;0;0;0;1;{4}{5}\n".format(afiliado, Util.mid(l, 153, 8), pan, dia, cr, monto))
                  else:
                      f.write("{0}{1};{2};{3};0;0;0;0;0;0;0;0;0;0;1;{4}{5};0;0\n".format(afiliado, Util.mid(l, 153, 8), pan, dia, cr, monto))
            
        print(d)
            
      # orgs: List[str] = ["720","722", "744", "860", "872"];
      # for org in orgs:
      #   resumenes: List[Resumen] = [];
      #   fileName = 'Facturacion' + org + ".txt"
      #   ruta = rutaArchivo + 'Facturacion' + '\\' + fileName
      #   fichero = os.path.join(ruta)
      #   if not os.path.exists(fichero):
      #     print('No existe', fileName)

      #   cont = 0;
      #   with open(ruta) as f:
      #     for linea in f:
      #       lD = linea.split("\t")
      #       resumen = Resumen(lD[0], lD[1], lD[2].strip().replace('"', ''), lD[3].strip(), int(lD[4]), float(lD[5]), int(lD[6]), float(lD[7]), int(lD[8]), float(lD[9]), int(lD[10]), float(lD[11]), int(lD[12]), float(lD[13]), int(lD[14]), float(lD[15]), int(lD[16]), float(lD[17]))
      #       # print(resumen.__str__())
      #       cont += 1
      #       resumenes.append(resumen)

      #   File.generar_reporte_mensual(org, resumenes)

      #   # print(org, 'Registros:', cont)
  else:
    print("error contect")
  