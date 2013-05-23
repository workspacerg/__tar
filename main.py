from Tar import Tar
from TarDir import TarDir
from TarFile import TarFile

    
###########################################################################
# Debut des test RomainG
# Ca peut servir pour voir vite fais coment ca marche, mais nllement du code final xD
# Je me en forme mercredi dans les bons fichier.
###########################################################################

print("Start : ")
Recup = ["",""]
#Creation d'un nouvelle objet tar


clavier = raw_input("Chemin du Tar : ")
Archive = Tar("Dir1.tar")
#Archive = Tar(clavier)
#print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
#Dir.readdir()

while Recup[0] != "Exit" :
    clavier = raw_input("Tar" + Archive.getpwd_tar()[0] + " &: ")
    
    Recup = clavier.split()
    
    if Recup[0] == "pwd" : 
        print  Archive.getpwd_tar()[0]
    elif Recup[0] == "ls" : 
        Dir.readdir()      
    elif Recup[0] == "cd" :
        Archive.chdir_tar(Recup[1])
        #print "Current File :" + str(Archive.getpwd_tar()[0])
        Dir = Archive.opendir_tar()  
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
