########################################################################
class TarDir:
    
    #----------------------------------------------------------------------
    #
    #
    #----------------------------------------------------------------------
    
    def __init__(self, _Param):
        """Constructor"""
        self.DirName = _Param[0][0]
        self.Niveau = _Param[0][1]
        #print "Dossier ouvert : "
        #print self.DirName
        #print self.Niveau
        self.listDir = _Param[1]
        self.listFile = _Param[2]
        
        
    def readdir(self):
        # Liste le contenue
        #print "Contenue du dossier : "
        
        for i in self.listDir :
            if i[1] == self.Niveau+1 and i[0].find(self.DirName) == 0: 
                print i[0].split('/')[-2] + '/'
            if self.Niveau+1 == 2 and i[1] == self.Niveau+1: 
                #print i[0].split('/')[-2] + '/'             
                print ""
                
        for i in self.listFile :
            if i[1] == self.Niveau+1 and i[0].find(self.DirName) == 0:
                print i[0].split('/')[-1]
            if self.Niveau+1 == 2 and i[1] == self.Niveau+1 : 
                print "print i[0].split('/')[-1]"            
        
    
    def close(self):
        # Ferme le dir
        print("TODO")
        
        

    def fopen(self, filename):
        # Ouvre le Fichier passer en parametre
        print("TODO")
    
######################################################################## 

