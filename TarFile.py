from termcolor import colored

########################################################################
class TarFile:
    
    #variable static pour placer le curseur courant
    offset = 0

    def __init__(self, _Param):
        """Constructor"""
        self.FileName   = _Param[0]
        self.Data       = _Param[2]
        self.Size       = _Param[3]
        
    def read(self, size):
        if TarFile.offset > size :
            print colored("Le curseur courant est en fin de fichier", 'white','on_cyan' )
        else :
            print self.Data[TarFile.offset:size]

    def seek(offset, whence=0):
        TarFile.offset = offset
    #Declaration d'une methode static de offset
    seek = staticmethod(seek)
    
    def close(self):
        self.FileName   = ""
        self.Data       = ""
        self.Size       = 0;
        offset          = 0;     

######################################################################## 
