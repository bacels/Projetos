import urllib.request
import cv2
import numpy as np
import time
from datetime import datetime


video_ip_on = True
duracaoFilme = 10
fimGravacao= False

cap = cv2.VideoCapture()
url='http://192.168.0.11:8080/shot.jpg'
cap.open(url)

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
    
saida = cv2.VideoWriter(nomeArquivo, cv2.VideoWriter_fourcc('M','J','P','G') , 10.0, dimensoes)  

cv2.namedWindow('Sz_Laboratorio_XVO', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Sz_Laboratorio_XVO', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while video_ip_on:
        try:
            
            imgResp=urllib.request.urlopen(url)
            imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
            img=cv2.imdecode(imgNp,-1)
            # cv2.imshow('Sz_Laboratorio_XVO',img) # nome e frame
            saida.write(img) #salvamos quadro a quadro
            if ord('x')==cv2.waitKey(1):
                video_ip_on = False
            horaAtual= time.time()
            if (horaAtual - horaInicio)> duracaoFilme:
                break 
        except:
            print("erro na captura")
            #video_ip_on = False
            
cap.release()
saida.release()
cv2.destroyAllWindows() 