import os

caminho = r"C:\Users\Vitor Barcelos\Desktop"
lista_arquivos = os.listdir(caminho + '\Save_Videos')

for arquivo in lista_arquivos:
    if '.avi' in arquivo:
        os.rename(caminho + f"/Save_Videos/{arquivo}", caminho + f"/Save_Videos/Jan/{arquivo}")
                # caminho da pasta + f (para dizer que tem uma variavel dentro de aspas do texto) + Nome da pasta onde se encontram os arquivos + nome do arquivo
                # , a mesma coisa porem com o Novo caminho da onde o arquivo tem que ir (no caso aqui a pasta Jan)
        print(cam_comp +  arquivo)