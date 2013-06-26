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
                    print colored("Le fichier ouvert n'est pas un fichier tar",'white','on_red')
                elif FileOpen == 1 :
                    print colored("Un fichier tar est deja en cour de lecture.",'white','on_red')
                else :
                    Archive = Tar(Recup[1])
                    print "test : "
                    print Recup[1].split(".")[-1]
                    Dir = Archive.opendir_tar()
                    FileOpen = 1
            except IndexError:
                print colored("Pas de fichier en parametre", 'white','on_red')        
            
        elif FileOpen == 0 :
            print colored("Aucun Fichier tar ouvert",'white','on_cyan')  
        
        elif Recup[0] == "pwd" : 
            print  Archive.getpwd_tar()[0]
        
        elif Recup[0] == "ls" : 
            try : 
                
                if Recup[1] == "-r" : 
                    Dir.readdir(1)
                else: 
                    print colored("Option inconnue",'white','on_cyan') 
                    Dir.readdir(0)
                    
            except IndexError:
                Dir.readdir(0)
              
        
        elif Recup[0] == "cd" :
            try:
                Archive.chdir_tar(Recup[1])
                #print "Current File :" + str(Archive.getpwd_tar()[0])
                Dir = Archive.opendir_tar()  
            except IndexError:
                print colored("Il manque un argument",'white','on_cyan')
        
        elif Recup[0] == "cat" : 
            try : 
                try : 
                    
                    if (Recup[1].split("/")[-1]) == OLDNAME :
                        File.read(File.Size)
                    
                    else : 
                        File = Dir.fopen(Recup[1])
                        OLDNAME = Recup[1].split("/")[-1]
                        File.read(File.Size)
                    

                except NameError:
                    File = Dir.fopen(Recup[1])  
                    OLDNAME = Recup[1].split("/")[-1]                      
                    File.read(File.Size)

            except AttributeError:
                print colored("Aucun fichier de ce nom dans le repertoire",'white','on_cyan')
            

        elif Recup[0] == "seek" :
            try:   
               
                try:
                     File.seek(int(Recup[1]))
                except ( NameError , AttributeError ) :
                    print colored("Aucun fichier ouvert",'white','on_cyan')


            except IndexError:
                print colored("Il manque un argument",'white','on_red')
        
        elif Recup[0] == "closetar" :
            print "Merci" 
            raise SystemExit(0)
        else :
            print colored("Commande introuvable", 'white','on_cyan')

        print ""

    except IndexError:
        print colored("Aucune comande",'white','on_red')
        Recup = " "
    except KeyboardInterrupt:
        print colored("\nUne combinaison clavier impose la fermeture du script",'white','on_red')
        raise SystemExit(0)


print("Stop  ")
