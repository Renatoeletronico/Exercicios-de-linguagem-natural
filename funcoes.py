from collections import defaultdict


def buscador (alvo,texto):
    texto = texto.replace('\n',' ')
    texto = texto.replace('\t',' ')
    
    ocorrencias = []
    encontrado_aqui = texto.find(alvo,0) 
    #se encontrar a palavar informa a posição 
    #senão informa -1 
    
    while encontrado_aqui > -1 :
        pos_inicial  = encontrado_aqui - (40 - len(alvo))
        trecho = texto[pos_inicial:pos_inicial + 80]
        ocorrencias.append(trecho)
        
        encontrado_aqui = texto.find(alvo, encontrado_aqui + 1)
        #inicia a busca a partir da palavra anterior + 1
        #se encontrar a palavar informa a posição 
        #senão informa -1 
    return ocorrencias


#Função para limpeza dos dados em lista 
def limpar(lista):
    lixo = '.,:;?!"´`^~()[]{}/\|@#$%"&*'
    quase_limpo = [x.strip(lixo).lower() for x in lista]
    return[x for x in quase_limpo if x.isalpha() or '-' in x ]


def ocorrencias(lista_palavras):
	dicionario = defaultdict(int)
	for p in lista_palavras:
		dicionario[p] += 1
	return dicionario 

#Função para a leitura dos arquivos a serem utilizados 
def ler(nome_arquivo):
    arquivo = open(nome_arquivo, "r",encoding='utf-8')
    conteudo_arq = arquivo.read()
    arquivo.close()
    return conteudo_arq
