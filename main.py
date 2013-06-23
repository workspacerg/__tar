#!/usr/bin/python

from Tar import Tar
from TarDir import TarDir
from TarFile import TarFile
from termcolor import colored


print("Start : ")
Recup = ["",""]
#Creation d'un nouvelle objet tar

FileOpen = 0

#Debut de l'interpreteur de commande 
while Recup[0] != "Exit" :
    
    try:
        #Lors de la premiere ouverture 
        if FileOpen == 0 :
                clavier = raw_input("Tar & : ")
        else : 
            clavier = raw_input("Tar" + Archive.getpwd_tar()[0] + " &: ")
        
        #Recuperation des differents parametres separer par des " "
        Recup = clavier.split()
        if Recup[0] == "opentar" :
            try : 
                if Recup[1].split(".")[-1] != "tar":
                    print colored("Le fichier ouvert n'est pas un fichier tar",'red')
                elif FileOpen == 1 :
                    print colored("Un fichier tar est deja en cour de lecture.",'red')
                else :
                    Archive = Tar(Recup[1])
                    print "test : "
                    print Recup[1].split(".")[-1]
                    Dir = Archive.opendir_tar()
                    FileOpen = 1
            except IndexError:
                print colored("Pas de fichier en parametre", 'yellow')        
            
        elif FileOpen == 0 :
            print colored("Aucun Fichier tar ouvert",'yellow')  
        
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
                print colored("Il manque un argument",'yellow')
        
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
                    print colored("Aucun fichier ouvert","red")

            except IndexError:
                print colored("Il manque un argument",'yellow')
        
        elif Recup[0] == "Exit" | Recup[0] == "exit":
            print "Merci" 

        
        else :
            print colored("Commande introuvable",'red')

        print ""

    except IndexError:
        print colored("Aucune comande",'white','on_red')
        Recup = " "
    except KeyboardInterrupt:
        print colored("\nUne combinaison clavier impose la fermeture du script",'white','on_red')
        raise SystemExit(0)


print("Stop  ")
