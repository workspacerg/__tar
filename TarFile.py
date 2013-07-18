from termcolor import colored

########################################################################
class TarFile:
    
    #variable static pour placer le curseur courant
    

    def __init__(self, _Param):
        """Constructor"""
        self.FileName   = _Param[0]
        self.name       = _Param[0].split("/")[-1]
        self.Data       = _Param[2]
        self.Size       = _Param[3]
        self.offset     = 0
        
    def read(self, size):
        if self.offset > size :
            print colored("Le curseur courant est en fin de fichier", 'white','on_cyan' )
        else :
            print self.Data[self.offset:size]

    def seek(self, offset, whence=0):
        self.offset     = offset

    def readpart(self, size, start, end):
        
        if int(start)> size :
            print colored("Le fichier est trop petit pour votre requette", 'white','on_cyan' )
        else :
            print self.Data[int(start):int(end)]
    
    def close(self):
        self.FileName   = ""
        self.Data       = ""
        self.Size       = 0;
        self.offset     = 0;    

    def getFileName(self) :
        return self.FileName 

######################################################################## 
