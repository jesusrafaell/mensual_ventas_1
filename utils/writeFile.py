from io import TextIOWrapper
from utils.utilitis import Util as StringUtils
from variables import *
import os

class File:
    def get_dirs_of_dir_mes(dir_path, mes):
        return [file for file in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, file)) and file[:3].lower() == mes.lower()]

    def get_file_of_dir_credito(ruta: str, mes_proceso: str, out: TextIOWrapper, log: TextIOWrapper) -> int:
        dirs =  File.get_dirs_of_dir_mes(ruta, mes_proceso);
        # Recorrer las carpetas y buscar los archivos FCPUTC57.860

        def escribir(formato: str, item1: str, item2: str, item3: str, item4: str, item5: str, item6: str):
            contenido: str = formato.format(
                item1, 
                item2, 
                item3, 
                item4, 
                item5,
                item6 
            )
            out.write(contenido + "\n")

        lineas = 0;
        for carpeta in dirs:
            # print('Carpeta:',carpeta)
            ruta_carpeta = os.path.join(ruta, carpeta)
            
            # Verificar si la carpeta existe
            if os.path.exists(ruta_carpeta):
                print('FCPUTC57.860')
                len: int = 0;
                len = File.FCPUTC57_860(carpeta, ruta_carpeta,'FCPUTC57.860', escribir)
                lineas +=  len
                print(len, lineas)

                bin1_720 = ["411851", "499930", "494170", "406267", "486520", "414764", "411850", "499929", "423691", "476515", "430906", "415366", "407440"]
                bin2_720 = ["517707", "518310", "536570"]
                # print(*bin1)
                len = File.FCPUTC57_720_722(carpeta, ruta_carpeta,'FCPUTC57.720',escribir, bin1_720, bin2_720)

                bin1_722 = ["433485", "433486", "422271", "425888"]
                bin2_722 = ["541841", "541842", "521359", "552462"]
                # print(*bin1)

                print('FCPUTC57.722')
                len = File.FCPUTC57_720_722(carpeta, ruta_carpeta,'FCPUTC57.722',escribir, bin1_722, bin2_722)

                print('FCPUTC57.872')
                len = File.FCPUTC57_720_722(carpeta, ruta_carpeta,'FCPUTC57.744',escribir, bin1_722, bin2_722)

                print('FCPUTC57.744')
                len = File.FCPUTC57_720_722(carpeta, ruta_carpeta,'FCPUTC57.744',escribir, bin1_722, bin2_722)

                print('FCPUTC57.btrans')
                len = File.FCPUTC57_Btrans(carpeta, ruta_carpeta,'FCPUTC57.Btrans',escribir)
            else:
                print(f"La carpeta {carpeta} no existe en la ruta {ruta}")
                log.write(f"La carpeta {carpeta} no existe en la ruta {ruta} \n")
        return dirs

    def FCPUTC57_860(carpeta, ruta_carpeta, fileName, escribir) -> int:
        #Buscar el archivo
        archivos = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.startswith(fileName)]
        #Leer el archivo
        arcContent:list[str] = []
        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            with open(ruta_archivo, "r") as file:
                arcContent = file.readlines()

        if(len(arcContent) == 0):
            return 0;

        # print('Carpeta:', carpeta, 'file: ' ,fileName, 'registros:', len(arcContent))
        dia = StringUtils.mid(arcContent[0], 10, 3)
        afiliado = "" 
        monto = ""
        pan = ""
        cr = ""
        for l in arcContent:
            codigo = l[166:].strip()
            if codigo == '10':
                afiliado = StringUtils.mid(l, 93, 9);
            elif codigo == '20':
                monto = StringUtils.mid(l, 22, 12);
                terminal = StringUtils.mid(l, 153, 8)
                pan = StringUtils.mid(l, 49, 19);
                cr = '' if StringUtils.mid(l, 76, 1) == '5' else '-';
                if(StringUtils.left(pan, 1) == '4'):
                    if StringUtils.containsAny(StringUtils.left(pan, 6), "422044", "422045", "422046", "446334", "425881"):
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;1;{4}{5};0;0;0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                    else:
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;1;{4}{5};0;0;0;0;0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )

                elif StringUtils.left(pan, 1) == '0':
                    escribir('{0}{1};{2};{3};0;0;0;0;1;{4}{5};0;0;0;0;0;0;0;0', 
                        afiliado, 
                        terminal,
                        pan, 
                        dia, 
                        cr,
                        monto
                    )
                elif int(StringUtils.left(pan, 2)) >= 51 and int(StringUtils.left(pan, 2)) <= 57:
                    if StringUtils.containsAny(StringUtils.left(pan, 6), "520148", "528004", "515673", "552327", "520154"):
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;0;0;0;0;1;{4}{5}', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                    else:
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;0;0;1;{4}{5};0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                elif StringUtils.left(pan, 6) == '627609':  #3322
                    escribir('{0}{1};{2};{3};0;0;1;{4}{5};0;0;0;0;0;0;0;0;0;0', 
                        afiliado, 
                        terminal,
                        pan, 
                        dia, 
                        cr,
                        monto
                    )
                else:
                    escribir('{0}{1};{2};{3};1;{4}{5};0;0;0;0;0;0;0;0;0;0;0;0', 
                        afiliado, 
                        terminal,
                        pan, 
                        dia, 
                        cr,
                        monto
                    )
        return len(arcContent)


    def FCPUTC57_720(carpeta, ruta_carpeta, fileName, escribir)-> int:
        #Buscar el archivo
        archivos = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.startswith(fileName)]
        #Leer el archivo
        arcContent:list[str] = []
        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            with open(ruta_archivo, "r") as file:
                arcContent = file.readlines()

        if len(arcContent) == 0:
            return 0;

        # print('Carpeta:', carpeta, 'file: ' ,fileName, 'registros:', len(arcContent))
        dia = StringUtils.mid(arcContent[0], 10, 3)
        afiliado = "" 
        monto = ""
        pan = ""
        cr = ""
        for l in arcContent:
            codigo = l[166:].strip()
            if codigo == '10':
                afiliado = StringUtils.mid(l, 93, 9);
            elif codigo == '20':
                monto = StringUtils.mid(l, 22, 12);
                terminal = StringUtils.mid(l, 153, 8)
                pan = StringUtils.mid(l, 49, 19);
                cr = '' if StringUtils.mid(l, 76, 1) == '5' else '-';
                if(StringUtils.left(pan, 1) == '4'):
                    if StringUtils.containsAny(StringUtils.left(pan, 6), "411851", "499930", "494170", "406267", "486520", "414764", "411850", "499929", "423691", "476515", "430906", "415366", "407440"):
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;1;{4}{5};0;0;0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                    else:
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;1;{4}{5};0;0;0;0;0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                else: 
                    if StringUtils.containsAny(StringUtils.left(pan, 6),  "517707", "518310", "536570"):
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;0;0;0;0;1;{4}{5}', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                    else: 
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;0;0;1;{4}{5};0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                    contenido = '{0}{1};{2};{3};1;{4}{5};0;0;0;0;0;0;0;0;0;0;0;0'.format(
                        afiliado, 
                        terminal,
                        pan, 
                        dia, 
                        cr,
                        monto)
                    if contenido == '72000014100000000;000006012886165275004;02;1;00000002067;0;0;0;0;0;0;0;0;0;0;0;0':
                        print(contenido)
        return  len(arcContent)


    def FCPUTC57_720_722(carpeta, ruta_carpeta, fileName, escribir, bin1, bin2)-> int:
        #Buscar el archivo
        archivos = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.startswith(fileName)]
        #Leer el archivo
        arcContent:list[str] = []
        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            with open(ruta_archivo, "r") as file:
                arcContent = file.readlines()

        if len(arcContent) == 0:
            return 0;

        # print('Carpeta:', carpeta, 'file: ' ,fileName, 'registros:', len(arcContent))
        dia = StringUtils.mid(arcContent[0], 10, 3)
        afiliado = "" 
        monto = ""
        pan = ""
        cr = ""
        for l in arcContent:
            codigo = l[166:].strip()
            if codigo == '10':
                afiliado = StringUtils.mid(l, 93, 9);
            elif codigo == '20':
                monto = StringUtils.mid(l, 22, 12);
                terminal = StringUtils.mid(l, 153, 8)
                pan = StringUtils.mid(l, 49, 19);
                cr = '' if StringUtils.mid(l, 76, 1) == '5' else '-';
                if(StringUtils.left(pan, 1) == '4'):
                    if StringUtils.containsAny(StringUtils.left(pan, 6), *bin1):
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;1;{4}{5};0;0;0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                    else:
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;1;{4}{5};0;0;0;0;0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                else: 
                    if StringUtils.containsAny(StringUtils.left(pan, 6), *bin2):
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;0;0;0;0;1;{4}{5}', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                    else: 
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;0;0;1;{4}{5};0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
        return  len(arcContent)

    def FCPD0602_720_txt(carpeta, ruta_carpeta, fileName, escribir):
        #Buscar el archivo
        archivos = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.startswith(fileName)]
        #Leer el archivo
        arcContent:list[str] = []
        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            with open(ruta_archivo, "r") as file:
                arcContent = file.readlines()

        if(len(arcContent) == 0):
            return;

        # print('Carpeta:', carpeta, 'file: ' ,fileName, 'registros:', len(arcContent))
        dia = StringUtils.mid(arcContent[0], 27, 2)
        afiliado = "" 
        monto = ""
        pan = ""
        cr = ""
        for l in arcContent:
            codigo = StringUtils.left(l, 1)
            if codigo == '6':
                monto = StringUtils.mid(l, 29, 11);
                pan = StringUtils.mid(l, 40, 21);
                cr = '' if StringUtils.mid(l, 76, 2) == '40' else '-';
            elif codigo == '7':
                afiliado = StringUtils.mid(l, 62, 9);
                terminal = StringUtils.mid(l, 13, 8)
                if(StringUtils.containsAny(StringUtils.mid(pan, 5, 6), "621984", "422050", "526749", "422228", "499929", "476515")):
                    if StringUtils.mid(pan, 5, 7) == "6219841" or StringUtils.containsAny(StringUtils.mid(pan, 5, 6), "422050", "526749", "422228"):
                        escribir('{0}{1};{2};{3};0;0;0;0;1;{4}{5};0;0;0;0;0;0;0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                    else:
                        escribir('{0}{1};{2};{3};0;0;1;{4}{5};0;0;0;0;0;0;0;0;0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                else: 
                    escribir('{0}{1};{2};{3};1;{4}{5};0;0;0;0;0;0;0;0;0;0;0;0', 
                        afiliado, 
                        terminal,
                        pan, 
                        dia, 
                        cr,
                        monto
                    )

    def FCPUTC57_722(carpeta, ruta_carpeta, fileName, escribir) -> int:
        #Buscar el archivo
        archivos = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.startswith(fileName)]
        #Leer el archivo
        arcContent:list[str] = []
        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            with open(ruta_archivo, "r") as file:
                arcContent = file.readlines()

        if(len(arcContent) == 0):
            return;

        # print('Carpeta:', carpeta, 'file: ' ,fileName, 'registros:', len(arcContent))
        dia = StringUtils.mid(arcContent[0], 10, 3)
        afiliado = "" 
        monto = ""
        pan = ""
        cr = ""
        for l in arcContent:
            codigo = l[166:].strip()
            if codigo == '10':
                afiliado = StringUtils.mid(l, 93, 9);
            elif codigo == '20':
                monto = StringUtils.mid(l, 22, 12);
                terminal = StringUtils.mid(l, 153, 8)
                pan = StringUtils.mid(l, 49, 19);
                cr = '' if StringUtils.mid(l, 76, 1) == '5' else '-';
                if(StringUtils.left(pan, 1) == '4'):
                    if StringUtils.containsAny(StringUtils.left(pan, 6),  "433485", "433486", "422271", "425888"):
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;1;{4}{5};0;0;0;0', 
                                afiliado, 
                                terminal,
                                pan, 
                            dia, 
                            cr,
                            monto
                        )
                    else:
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;1;{4}{5};0;0;0;0;0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                else: 
                    if StringUtils.containsAny(StringUtils.left(pan, 6), "541841", "541842", "521359", "552462"):
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;0;0;0;0;1;{4}{5}', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
                    else: 
                        escribir('{0}{1};{2};{3};0;0;0;0;0;0;0;0;0;0;1;{4}{5};0;0', 
                            afiliado, 
                            terminal,
                            pan, 
                            dia, 
                            cr,
                            monto
                        )
        return len(arcContent)



    def FCPUTC57_Btrans(carpeta, ruta_carpeta, fileName, escribir) -> int:
        #Buscar el archivo
        archivos = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.startswith(fileName)]
        #Leer el archivo
        arcContent:list[str] = []
        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            with open(ruta_archivo, "r") as file:
                arcContent = file.readlines()

        if(len(arcContent) == 0):
            return 0;

        # print('Carpeta:', carpeta, 'file: ' ,fileName, 'registros:', len(arcContent))
        dia = StringUtils.mid(arcContent[0], 10, 3)
        afiliado = "" 
        monto = ""
        pan = ""
        cr = ""
        for l in arcContent:
            if StringUtils.mid(l, 84, 12) == '000000720720':
                afiliado = StringUtils.mid(l, 93, 9)
            if StringUtils.mid(l, 34, 3) == '937':
                monto = StringUtils.mid(l, 22, 12);
                pan = StringUtils.mid(l, 49, 19)
                cr: str = '' if StringUtils.mid(l, 76, 1) == '5' else '-'
                terminal = ''
                if(StringUtils.left(pan, 1) == '4'):
                    if StringUtils.containsAny(
                            StringUtils.left(pan, 6), 
                            "411851", "499930", "494170", 
                            "406267", "486520", "414764", 
                            "411850", "499929", "423691", 
                            "476515", "430906", "415366", 
                            "407440"
                        ):
                        escribir('{0};{1};{2};0;0;0;0;0;0;0;0;1;{3}{4};0;0;0;0', 
                            afiliado, 
                            pan, 
                            dia, 
                            cr,
                            monto,
                            terminal,
                        )
                    else:
                        escribir('{0};{1};{2};0;0;0;0;0;0;1;{3}{4};0;0;0;0;0;0', 
                            afiliado, 
                            pan, 
                            dia, 
                            cr,
                            monto,
                            terminal,
                        )
                else: 
                    if StringUtils.containsAny(StringUtils.left(pan, 6), "517707", "518310", "536570"):
                        escribir('{0};{1};{2};0;0;0;0;0;0;0;0;0;0;0;0;1;{3}{4}', 
                            afiliado, 
                            pan, 
                            dia, 
                            cr,
                            monto,
                            terminal,
                        )
                    else: 
                        escribir('{0};{1};{2};0;0;0;0;0;0;0;0;0;0;1;{3}{4};0;0', 
                            afiliado, 
                            pan, 
                            dia, 
                            cr,
                            monto,
                            terminal,
                        )
        return len(arcContent) 


    def get_file_of_dir_debito(ruta: str, mes_proceso: str, out: TextIOWrapper, log: TextIOWrapper)-> int:
        dirs =  File.get_dirs_of_dir_mes(ruta, mes_proceso);
        # Recorrer las carpetas y buscar los archivos FCPUTC57.860

        def escribir(formato: str, item1: str, item2: str, item3: str, item4: str, item5: str, item6: str):
            contenido: str = formato.format(
                item1, 
                item2, 
                item3, 
                item4, 
                item5,
                item6 
            )
            out.write(contenido + "\n")

        for carpeta in dirs:
            # print('Carpeta:',carpeta)
            ruta_carpeta = os.path.join(ruta, carpeta)
            
            # Verificar si la carpeta existe
            if os.path.exists(ruta_carpeta):
                print('FCPD0602_720.txt')
                File.FCPD0602_720_txt(carpeta, ruta_carpeta,'FCPD0602_720.txt',escribir)
            else:
                print(f"La carpeta {carpeta} no existe en la ruta {ruta}")
                log.write(f"La carpeta {carpeta} no existe en la ruta {ruta} \n")
        return dirs

