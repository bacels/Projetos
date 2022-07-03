import cv2
import numpy as np
import time
from datetime import datetime
import os

duracaoFilme = 10
fimGravacao= False

cap = cv2.VideoCapture(0)

caminho = r"/home/szlab/Desktop/"
destino = r"/home/szlab/Desktop/Projetos"

horaInicio = time.time()

now = datetime.now()
ano = int(now.strftime('%Y'))
mes = int(now.strftime('%m'))
dia = int(now.strftime('%d'))
hora = int(now.strftime('%H'))
minuto = int(now.strftime('%M'))
segundo = int(now.strftime('%S'))

nomeArquivo= 'vid_Dia%d' %dia
nomeArquivo += '_%d' %mes
nomeArquivo += '_%d' %ano
nomeArquivo += '_'
nomeArquivo += 'Hora_%d' % hora
nomeArquivo += '_%d' %minuto
nomeArquivo += '_%d' %segundo
nomeArquivo += ".avi"

largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
altura =  int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
dimensoes = (largura,altura)
    
saida = cv2.VideoWriter(nomeArquivo, cv2.VideoWriter_fourcc('M','J','P','G') , 15.5, dimensoes)  

if cap.isOpened():
    try:
        ret, fme = cap.read()
        while ret:
            try:
                ret, fme = cap.read()
                cv2.imshow("Sz_Cloud", fme)
                saida.write(fme)
                k = cv2.waitKey(5)
                if k == 27: #esc
                    break
                horaAtual= time.time() 
                tempo_atual_do_filme =  (int(horaAtual - horaInicio))
                print(tempo_atual_do_filme)
                if tempo_atual_do_filme >= duracaoFilme:
                    break
            except:
                print("Erro na captura ou exibicao da imagem!") 
    except:
        print("Erro na leitura da camera")
else:
    print("Erro na abertura da camera!")        
cap.release()
saida.release()
cv2.destroyAllWindows()

lista_arquivos = os.listdir(caminho)
for arquivo in lista_arquivos:
    if '.avi' in arquivo:
        os.rename(caminho + arquivo, destino + f"/Saves/{arquivo}")
        print(arquivo)