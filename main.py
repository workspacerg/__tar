#!/usr/bin/python

from Tar import Tar
from TarDir import TarDir
from TarFile import TarFile


print("Start : ")
Recup = ["",""]
#Creation d'un nouvelle objet tar

FileOpen = 0

#Debut de l'interpreteur de commande 
while Recup[0] != "Exit" :
    
    #Lors de la premiere ouverture 
    if FileOpen == 0 :
            clavier = raw_input("Tar & : ")
    else : 
        clavier = raw_input("Tar" + Archive.getpwd_tar()[0] + " &: ")
    
    #Recuperation des differents parametres separer par des " "
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
    
    elif Recup[0] == "cat" : 
        print ""
        File = Dir.fopen(Recup[1])
        File.read(File.Size)
    
    elif Recup[0] == "seek" :
        try:   
            TarFile.seek(int(Recup[1])  )
            try:
                 File
            except NameError:
                print "Aucun fichier ouvert" 

        except IndexError:
            print "Il manque un argument"
    
    elif Recup[0] == "Exit" :
        print "Merci"     
    
    else :
        print "Commande introuvable"

    print ""

print("Stop  ")
