import os
from datetime import datetime

now = datetime.now()
dia = (int(now.strftime('%d')))-1


lista_arquivos = os.listdir(r"C:\Users\Vitor\Desktop")
for arquivo in lista_arquivos:
    print(arquivo)
    if '.avi' in arquivo:
        if f'vid_Dia{dia}'in arquivo:
            os.remove(arquivo)