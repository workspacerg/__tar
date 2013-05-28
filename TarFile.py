########################################################################
class TarFile:
    
    #----------------------------------------------------------------------
    #
    #
    #----------------------------------------------------------------------
    
    def __init__(self, _Param):
        """Constructor"""
        self.FileName = _Param[0]
        self.File = _Param[2]
        self.read(230)
        #print "je suis la"
        
        
    def read(self, size):
        #Lecture de size octet dans le fichier, return str
        print "Lecture du fichier " + self.FileName 
        print self.File
        
    def close(self):
        #Ferme le fichier
        print("TODO")

    def seek(self, offset, whence=0):
        #place en position offset le pointeur courant
        print("TODO")
    
######################################################################## 