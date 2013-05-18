from TarDir import TarDir
from TarFile import TarFile

########################################################################
class Tar:
    
    #----------------------------------------------------------------------
    #Class Tar contenant les methode de manipulation des fichiers tar
    #----------------------------------------------------------------------
    
    def __init__(self, _Param):
        """Constructor"""
        self.FileName = _Param
        print "ouverture du fichier tar : "  + self.FileName
        self.open_tar()
        self.CurrentDir = ["/" , 0]
        self.listDir = [["/" , 0]]
        self.listFile = list()
         
        
    def open_tar(self):
        # Ouvre l'archive passer dans le constructeur
        self.f = open(self.FileName,"rb")
        
    def close_tar(self):
        # Ferme l'archive.
        self.f.close()

    def chdir_tar(self, path):
        # Changement de repertoire.
        
        print("TODO")
        # Verifier le chemin voulu existe
        # Changer le repertoire courrant
        # Envoye l'objet dir courrant
        
        
    
    def getpwd_tar(self):
        # retourne le nom du repertoire courant
        return self.CurrentDir
        
    def opendir_tar(self):
        # retourne un objet de la classe tardir
        print "\nopendir_tar() : "
        Dir = TarDir([self.CurrentDir, self.listDir , self.listFile])
        return Dir


       
        
    
    def parseTar(self):
        print "................................................................................"
        print "Debut du parsage complet :" 
        data = self.f.read()
        currentLoc = 0
        self.nbr = 0 
        
       
        
        while currentLoc < len(data)-512*2 :  
            TarFileName = data[currentLoc:currentLoc+100].rstrip('\000')
            
            #print "Nom :" + TarFileName
            TarFileSize = str(int(data[currentLoc+124:currentLoc+136], 8))
            #print "Size: " + TarFileSize
            Niveau = TarFileName.count("/")
            #print "Niveau : " + str(Niveau)
            TarFileType = data[currentLoc+156:currentLoc+157]
            #print "Type is :" + TarFileType
            #self.isFileOrDir(TarFileType)  
            
            
            if TarFileType == "0" :
                self.listFile.append([TarFileName , Niveau+1])
                currentLoc += 512
                TarFileContent = data[currentLoc:currentLoc+int(TarFileSize)]
                #print "Content : \n" + TarFileContent
                save = 0
                
                while save < int(TarFileSize,10) :
                    currentLoc += 512
                    save += 512   
                    
            else:
                self.listDir.append([TarFileName , Niveau])
                currentLoc += 512
                     
        self.close_tar()
        
        self.CurrentDir = self.listDir[0]
        """
        print   self.listDir
        print   self.listFile
        
 
        print "\n\nAffiche que les Dossiers dans le dossier FIND et Niveu+1"
        
        self.CurrentDir = self.listDir[0]
        
        NiveauUp = 1
        print "Dossier :"
        for i in self.listDir :
            if i[1] == NiveauUp and i[0].find("/") == 0  : 
                print i[0]
            if NiveauUp == 1 and i[1] == NiveauUp : 
                print i[0]            
        
        print "Fichier : "
        for y in self.listFile :
            if y[1] == NiveauUp and y[0].find("Dir/") == 0  :
                print y[0]
            if NiveauUp == 1 and y[1] == NiveauUp : 
                print y[0] 
        """ 
        print "ParseOK"
        print "................................................................................\n"
        return [self.listFile, self.listDir] 
    
######################################################################## 
