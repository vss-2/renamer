from pathlib import Path

def walk(dir,newName,extension):
    dirs = [x for x in dir.iterdir() if x.is_dir()]#list of directories
    for d in dirs:
        walk(d,newName,extension)
        renameNow(d,newName,extension)#when there is no direcroties below
        
    
def renameNow(dir,newName,extension):# rename all files in dir directory
    t = dir.parts
    
    #removing repetitions in t
    seen = []
    answer = []
    for elem in t:
        if elem not in seen:
            seen.append(elem)
            answer.append(elem)
    #repetitions removed
    
    
    n = len(answer)-1
    while(n>=0):
        newName = answer[n]+'_'+ newName
        n=n-1
    
    print('\ndirectory: '+newName)
    files = list(dir.glob('**/*'+extension))##lista com todos os arquivos com a mesma extensao dada deste diretorio e dos diretorios dentro deles(merda)
    i=0
    for file in files:
        i=i+1
        finalName = newName+str(i)+extension
        print(file)##arquivo a ser renomeado
        print(finalName)##novo nome do arquivo
        file.rename(str(dir)+'/'+finalName)
        
        
    


p = Path('.')## path to this directory
newName = '' #dont touch here
extension = ".jpg" # change extension here
print("trocando nome dos arquivos "+extension+'...')

walk(p,'',extension)

print('\npronto')


