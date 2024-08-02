import osc
import shutil

#Enter path you wish to clean up
path = input("Enter Path: ")
files = os.listdir(path)

#for the files mentioned above look at the extention

for file in files:
    filename,extention = os.path.splitext(file)
    extention = extention[1:]

#find file with said extention, if extention exsists put it in corresponding folder
    if os.path.exists(path+"/"+extention):
        shutil.move(path+"/"+file, path+"/"+extention+"/"+file)

        #if not folder excists then make folder and then put file into created folder
    else:
        os.makedirs(path+"/"+extention)
        shutil.move(path+"/"+file, path+"/"+extention+"/"+file)

