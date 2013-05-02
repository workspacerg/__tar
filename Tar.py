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
        self.f = open(self.FileName,"r")
        data = self.f.readline()
        print data 
        
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

    
######################################################################## 
