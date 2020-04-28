from pathlib import Path

def DFS_Renamer(pasta, ext):
	# Faz:
	# 1. Visita igual DFS todas as pastas a partir do diretório atual
	# 2. Renomeia, caso já tenha visitado e não existam pastas internas
	pastas = [x for x in pasta.iterdir() if x.is_dir()]
	for p in pastas:
		DFS_Renamer(p, ext)
		renomear(p, ext)
	return 
    
    
def renomear(pastaAtual, ext):
	t = pastaAtual.parts
   
	visto = []
	lista = []

	# Remover repeticoes repetições de t
	for elem in t:
		if elem not in visto:
			visto.append(elem)
			lista.append(elem)

	novoNome=''
	
	for k in range(len(answer)-1,-1,-1):
        	novoNome = lista[k]+'_'+ novoNome

	novoNome = novoNome.lower()

	# Lista com todos os arquivos com a mesma extensão dada deste diretório
	arquivos = list(dir.glob('./*'+ext))
	i = 0
	for a in arquivos:	
		editado = False
		nome = a.name
		if(not nome.startswith(novoNome, 0, len(nome))):
			while(not editado):
                		i = i+1
                		try:
					finalNome = novoNome+str(i).zfill(4)+ext
					a.rename(str(dir)+'/'+finalNome)
					editado = True
				except Exception as Error:
					print('Houve algum erro, parando execução:', Error)
					exit()
	return 

if __name__ == '__main__':
	dirAtual = input('Deseja renomear do diretório atual (s/n)?')
	caminho = Path('.')

	if(dirAtual.lower().find('n') != -1):
		dirAtual = input('Escreva o caminho absoluto do diretório desejado:\n')
		caminho = Path(dirAtual)
	
	extensao = input('Qual extensão você deseja modificar? (ex: \'.doc\')\n')

	print('\nTROCANDO PARA EXTENSÃO '+ extensao +' OS ARQUIVOS DE'+ dirAtual + '!\n')

	DFS_Renamer(dirAtual, extensao)

	print('Encerrando!\n')
	exit()