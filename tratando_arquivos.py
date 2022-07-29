


    # Abertura do arquivo desejado
resultados = []
with open("Local do aquivivo que vai ser lido aqui","r") as arquivo_entrada:
   
    linhas = arquivo_entrada.readlines()[1: ]                     # nesse exemplo fiz a remoção do cabeçario para poder alterar os dados, caso não seja nescessario remova [1:]
    
    
    # Criar os parametros de modificação do arquivo adequado a suas nescessidades  
    for linha in linhas:                                          # A cada linha do arquivo será feitos as alteraçãos descristas a baixo
        dados = linha.split(',')                                  # A variavel dados recebe recebe linha separada na virgula formando uma Lista | dados = []
        email = dados[3].replace("\n","")                         # Tratamento fora da f'' pois não suporta \\ ou \n dentro {}
        resultados.append(f'{dados[1]} {dados[2]}, {email}\n')    # Aqui coloca os dados que queira salvar no novo arquivo

    pass

    # Gravação do Novo Arquivo de saida com as alteraçãoes desejadas
with open("local onde será salvo/arquivo.csv","w") as arquivo_saida:    # Caso deseja salvar no mesmo diretorio onde o programa tratamento_arquivos.py apenas adicione ./ e o nome do arquivo.csv
    for resultado in resultados:
        arquivo_saida.write(resultado)
