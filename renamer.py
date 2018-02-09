from pathlib import Path

def walk(dir,previousname,extension):
    dirs = [x for x in dir.iterdir() if x.is_dir()]#list of directories
    for d in dirs:
        t = d.parts
        n = len(t)
        dirname = t[n-1]
        print(dirname)
        print
        if(previousname!=''):
            newName = previousname+'_' +dirname
        else:
            newName = dirname
        walk(d,newName,extension)
        renameNow(dir/d,newName,extension)#when there is no direcroties below
        
    
def renameNow(dir,newName,extension):# rename all files in dir directory
    files = list(dir.glob('**/*.'+extension))##lista com todos os arquivos com a mesma extensao dada deste diretorio
    #print(files)
    i=0
    for file in files:
        i=i+1
        finalName = newName+str(i)+extension
        file.rename(str(dir)+'/'+finalName)
        #print(finalName)
    


p = Path('.')## path to this directory
newName = '' #dont touch here
extension = "jpg" # change extension here
print("trocando nome dos arquivos "+extension+'...')

walk(p,newName,extension)

print('\n\npronto')


