from Tar import Tar
from TarDir import TarDir
from TarFile import TarFile

    
###########################################################################
# Debut des test RomainG
# Ca peut servir pour voir vite fais coment ca marche, mais nllement du code final xD
# Je me en forme mercredi dans les bons fichier.
###########################################################################

print("Start : ")

#Creation d'un nouvelle objet tar
Archive = Tar("Dir1.tar")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "\n"

Archive.chdir_tar("Dir1/")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "\n"

Archive.chdir_tar("/")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "\n"

Archive.chdir_tar("Dir1/SDir1/")
print "Current File :" + str(Archive.getpwd_tar()[0])
Dir = Archive.opendir_tar()
Dir.readdir()
print "\n"

print("Stop  ")