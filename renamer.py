from pathlib import Path

def walk(dir,extension):
    dirs = [x for x in dir.iterdir() if x.is_dir()]#list of directories
    for d in dirs:
        walk(d,extension)
        renameNow(d,extension)#when there is no direcroties below
#################################################        
    
def renameNow(dir,extension):# rename all files in dir directory
    t = dir.parts
    
#######removing repetitions in t
    seen = []
    answer = []
    for elem in t:
        if elem not in seen:
            seen.append(elem)
            answer.append(elem)
######repetitions removed

#############
    n = len(answer)-1
    newName=''
    while(n>=0):
        newName = answer[n]+'_'+ newName
        n=n-1
############# 
    files = list(dir.glob('./*'+extension))##lista com todos os arquivos com a mesma extensao dada deste diretorio
    i=0
    for file in files:
        i=i+1
        finalName = newName+str(i)+extension
        print(file)##arquivo a ser renomeado
        print('newname'+finalName)##novo nome do arquivo
        file.rename(str(dir)+'/'+finalName)
##############################################       
        
    

#####   main script   ####
p = Path('.')## path to this directory
extension = ".jpg" # change extension here
print("trocando nome dos arquivos "+extension+'...')

walk(p,extension)

print('\nPRONTO.')


