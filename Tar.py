########################################################################
class Tar:
    
    #----------------------------------------------------------------------
    #Class Tar contenant les methode de manipulation des fichiers tar
    #----------------------------------------------------------------------
    
    def __init__(self, _Param):
        """Constructor"""
        self.FileName = _Param
        print(self.FileName)
        self.open_tar()
        
    def open_tar(self):
        # Ouvre le fichier passer dans le constructeur
        self.f = open(self.FileName,"rb")
        
    def close_tar(self):
        # Ferme l'archive.
        self.f.close()

    def chdir_tar(self, path):
        # Changement de repertoire.
        print("TODO")
    
    def getpwd_tar(self):
        # retourne le nom du repertoire courant
        print("TODO")
        
    def opendir_tar(self):
        # retourne un objet de la classe tardir
        print("TODO")

    def isFileOrDir(self, _FileType):
        print "TestFileOrDir : " + _FileType
        
        IsDir = "5"                                                 #Test Pseudo Enumeration
        IsFile = "0"
                
        if _FileType == IsFile :                                  #Test du typage de fichier
            print("Is a File")
        elif _FileType == IsDir:
            print("Is a directory")
        else:
            print("Unknow")        
        
    
    def parseTar(self):
        print "Debut du parsage complet : \n" 
        data = self.f.read()
        currentLoc = 0
        
        TarFileName = data[currentLoc:currentLoc+100]
        print "Nom :" + TarFileName
        TarFileSize = str(int(data[currentLoc+124:currentLoc+136], 8))
        print "Size: " + TarFileSize
        TarFileType = data[currentLoc+156:currentLoc+157]
        print "Type is :" + TarFileType
        self.isFileOrDir(TarFileType)
        
        currentLoc += 512
        
        TarFileName = data[currentLoc:currentLoc+100]
        print "Nom :" + TarFileName
        TarFileSize = str(int(data[currentLoc+124:currentLoc+136], 8))
        print "Size: " + TarFileSize
        TarFileType = data[currentLoc+156:currentLoc+157]
        print "Type is :" + TarFileType
        self.isFileOrDir(TarFileType)    
        
        currentLoc += 512
        
        TarFileName = data[currentLoc:currentLoc+100]
        print "Nom :" + TarFileName
        TarFileSize = str(int(data[currentLoc+124:currentLoc+136], 8))
        print "Size: " + TarFileSize
        TarFileType = data[currentLoc+156:currentLoc+157]
        print "Type is :" + TarFileType
        self.isFileOrDir(TarFileType)    
        
        currentLoc += 512
        
        #Lecture de fichier
        
        TarFileContent = data[currentLoc:currentLoc+int(TarFileSize)]
        print "Content : " + TarFileContent
        save = 0
        while save < int(TarFileSize,10) :
            currentLoc += 512
            save += 512
            
        TarFileName = data[currentLoc:currentLoc+100]
        print "Nom :" + TarFileName
        TarFileSize = str(int(data[currentLoc+124:currentLoc+136], 8))
        print "Size: " + TarFileSize
        TarFileType = data[currentLoc+156:currentLoc+157]
        print "Type is :" + TarFileType
        self.isFileOrDir(TarFileType)          
            
        currentLoc += 512
                
                #Lecture de fichier
                
        TarFileContent = data[currentLoc:currentLoc+int(TarFileSize)]
        print "Content : " + TarFileContent
        save = 0
        while save < int(TarFileSize,10) :
            currentLoc += 512
            save += 512 
        
        TarFileName = data[currentLoc:currentLoc+100]
        print "Nom :" + TarFileName
        TarFileSize = str(int(data[currentLoc+124:currentLoc+136], 8))
        print "Size: " + TarFileSize
        TarFileType = data[currentLoc+156:currentLoc+157]
        print "Type is :" + TarFileType
        self.isFileOrDir(TarFileType)            
        
        
        print("Fin du parsage complet\n")
        

    
######################################################################## 
