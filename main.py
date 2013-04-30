from Tar import Tar
from TarDir import TarDir
from TarFile import TarFile

    
###########################################################################
# Debut des test RomainG
# Ca peut servir pour voir vite fais coment ca marche, mais nllement du code final xD
# Je me en forme mercredi dans les bons fichier.
###########################################################################

print("Start : ")



mon_fichier = open("TestFile.tar", "rb")                    #Ouverture du fichier en mode Binaire
data = mon_fichier.read()                                   #Recuperation des données en mode normal
mon_fichier.close()                                         #Fermeture des fichiers

print("Lecture de data : ")                                 #Affichage
print data                                                  #---------

print("\nLecture en hÈxadecimal ")
data_hex = data.encode("hex")                               #Copy des donnée en hexadecimal 
print data_hex                                              #Affichage

TarFileName = data_hex[0:200]                               #Recuperation Des informations en fonction de la structure de l'entete tar
tarFileType = data_hex[2360:2362]

print(TarFileName)
print(tarFileType)

IsDir = "5"                                                 #Test Pseudo Enumeration
IsDir = IsDir.encode("hex")
IsFile = "0"
IsFile = IsFile.encode("hex")



if tarFileType == IsFile :                                  #Test du typage de fichier
    print("{} Is a File".format(data[:10]))
elif tarFileType == IsDir:
    print("{} Is a directory" .format(data[:10]))
else:
    print("Unknow")


print("Taille de larchive: ")                               #Affichage de la taille total du fichier 
print(len(data_hex))

#SplitTest = data.split()
#print(SplitTest[1])

# Fin des test RomainG

