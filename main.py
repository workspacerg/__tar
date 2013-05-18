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

listRetour = Archive.parseTar();

#print "\n\nListeRetour : "
#print listRetour[1]
#print listRetour[0]

#print Archive.getpwd_tar()

print "test TarDiv :"
#print listRetour[1][4]
#print listRetour[1]
#print listRetour[0]

#DirTest = TarDir([listRetour[1][4], listRetour[1], listRetour[0]])
#DirTest.readdir()

Dir = Archive.opendir_tar()
Dir.readdir()


print("\n\nStop  ")