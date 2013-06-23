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
        #print "ouverture du fichier tar : "  + self.FileName
        self.open_tar()
        self.CurrentDir = ["/" , 1]
        self.listDir = [["/" , 1]]
        self.listFile = list()
        self.parseTar()  
         
    def open_tar(self):
        # Ouvre l'archive passer dans le constructeur
        self.f = open(self.FileName,"rb")
        
    def close_tar(self):
        # Ferme l'archive.
        self.f.close()

    def chdir_tar(self, path):
        # Changement de repertoire.
        # Verifier le chemin voulu existe

        if path[0:3] == "../" : 
            last =  self.CurrentDir[0].split('/')[-2] + '/'
            Find = self.CurrentDir[0].replace(last,'',1) 
            path = str(Find) + path[3:]
            
        
        if path[0:2] == "./" :
            path = self.CurrentDir[0] + path[2:]
          
        if path[0:1] != "/" :
            path = self.CurrentDir[0] + path

        
        for i in self.listDir : 
#print  "test : " + path + " = " + i[0]
            if path == i[0] : 
                self.CurrentDir = i
        
        
    def getpwd_tar(self):
        # retourne le nom du repertoire courant
        return self.CurrentDir
        
    def opendir_tar(self):
        # retourne un objet de la classe tardir
        Dir = TarDir([self.CurrentDir, self.listDir , self.listFile])
        return Dir
        
   # # Parcour tout le fichier tar ouvert et ordonne les donnees dans une liste
    def parseTar(self):
        print "................................................................................"
        print "Debut du parsage complet :" 
        data = self.f.read()
        currentLoc = 0
        self.nbr = 0 
            
        while currentLoc < len(data)-512*2 :  
            #Recuperation des informations de l'entete tar
            TarFileName = "/" + data[currentLoc:currentLoc+100].rstrip('\000')
            TarFileSize = str(int(data[currentLoc+124:currentLoc+136], 8))
            SizeOfFile = int(data[currentLoc+124:currentLoc+136], 8)
            Niveau = TarFileName.count("/")
            TarFileType = data[currentLoc+156:currentLoc+157]
            
            #Si un fichier est detecte il sera traite dans liste file
            if TarFileType == "0" :
                currentLoc += 512
                TarFileContent = data[currentLoc:currentLoc+int(TarFileSize)]
                save = 0
                self.listFile.append([TarFileName , Niveau+1 , TarFileContent, SizeOfFile , currentLoc] )
                
                #Jusqu'a ce que le fichier soit fini et que le bloc de 512 aussi
                while save < int(TarFileSize,10) :
                    currentLoc += 512
                    save += 512   
            
            #Si c'est un dossier on ajout a la liste des dossier puis on ce deplace d'un bloc
            else:
                self.listDir.append([TarFileName , Niveau])
                currentLoc += 512
            
        self.CurrentDir = self.listDir[0]

        print "ParseOK"
        #print self.listDir
        #print self.listFile
        print "................................................................................\n"
        return [self.listFile, self.listDir] 
    
######################################################################## 
