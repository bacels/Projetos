# Projetos

# Os videos serão salvos na pasta onde o programa estiver, ou seja, os arquivos de video serão salvos na mesma pasta onde o programa estiver sendo executado, logo, o "caminho" dessa pasta deve ser utilizado para pega-los e transferi-los para a pasta de "destino".

# No programa, "caminho" e "destino" sao as variaveis que armazenam os caminhos onde as pastas que vão sr utilizadas estão.

# "Save_Videos" e "Saves" são as pastas que EU utilizei e devem ser trocadas pelos respectivos caminhos que serão utilizados por quem quer que esteja utilizando este codigo, e "arquivos" são as gravaçoes de video.

# As pastas utilizadas para pegas as gravações e o destino para onde elas deve ir deverão existir antes de executar o programa para evitar erros.

# Caso esteja tendo problemas com  o tempo do video saiba que a linha /saida = cv2.VideoWriter(nomeArquivo, cv2.VideoWriter_fourcc('M','J','P','G') , 21.0, dimensoes) / se refere respectivamente ao nome do arquivo geradoo, codec utilizado, fps do video, altura e largura da janela, onde ao mexer no fps do video, sera alterado proporcionalmente o tamanho do mesmo.

# by Vitor Barcelos