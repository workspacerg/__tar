from Tar import Tar
from TarDir import TarDir
from TarFile import TarFile


print("Start : ")
Recup = ["",""]
#Creation d'un nouvelle objet tar

FileOpen = 0
#clavier = raw_input("Chemin du Tar : ")
#Archive = Tar("Dir1.tar")
#Archive = Tar(clavier)
#print "Current File :" + str(Archive.getpwd_tar()[0])
#Dir = Archive.opendir_tar()
#Dir.readdir()

while Recup[0] != "Exit" :
    if FileOpen == 0 :
        clavier = raw_input("Tar & : ")
    else : 
        clavier = raw_input("Tar" + Archive.getpwd_tar()[0] + " & : ")
    
    Recup = clavier.split()
    if Recup[0] == "opentar" :
        try : 
            Archive = Tar(Recup[1])
            Dir = Archive.opendir_tar()
            FileOpen = 1
        except IndexError:
            print "Pas de fichier en parametre"        
        
    elif FileOpen == 0 :
        print "Aucun Fichier tar ouvert"  
    elif Recup[0] == "pwd" : 
        print  Archive.getpwd_tar()[0]
    elif Recup[0] == "ls" : 
        Dir.readdir()      
    elif Recup[0] == "cd" :
        try:
            Archive.chdir_tar(Recup[1])
            #print "Current File :" + str(Archive.getpwd_tar()[0])
            Dir = Archive.opendir_tar()  
        except IndexError:
            print "Il manque un argument"
    elif Recup[0] == "Exit" :
        print "Merci"     
    else :
        print "Commande introuvable"

    print ""

print("Stop  ")

'''

Archive.chdir_tar("/Dir1/")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "\n"


Archive.chdir_tar("/")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "\n"

Archive.chdir_tar("/Dir1/SDir1/")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "\n"

Archive.chdir_tar("../")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "\n"

Archive.chdir_tar("./SDir1/")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "\n"

Archive.chdir_tar("../SDir2/")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "pwd : " + Archive.getpwd_tar()[0]
print "\n"

Archive.chdir_tar("../")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "pwd : " + Archive.getpwd_tar()[0]
print "\n"

Archive.chdir_tar("SDir2/SSDir1/")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "pwd : " + Archive.getpwd_tar()[0]
print "\n"




#print "Test de lecture de fichier : "
#File = TarFile(["Dir/SSDIr/File1.txt","5","Contenue"])
'''
