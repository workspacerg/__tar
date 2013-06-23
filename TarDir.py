from TarFile import TarFile
from termcolor import colored

########################################################################
class TarDir:
    
    def __init__(self, _Param):
        """Constructor"""
        self.DirName    = _Param[0][0]
        self.Niveau     = _Param[0][1]
        self.listDir    = _Param[1]
        self.listFile   = _Param[2]
        
    def readdir(self):
        # Liste le contenue
    
        for i in self.listDir :
            #A regarder de plus pres
            if i[1] == self.Niveau+1 and i[0].find(self.DirName) == 0: 
                print colored(i[0].split('/')[-2] + '/','green')
            if self.Niveau+1 == 2 and i[1] == self.Niveau+1: 
                #print i[0].split('/')[-2] + '/'             
                print ""
                
        for i in self.listFile :
            if i[1] == self.Niveau+1 and i[0].find(self.DirName) == 0:
                print colored(i[0].split('/')[-1], 'magenta')
            if self.Niveau+1 == 2 and i[1] == self.Niveau+1 : 
                print "print i[0].split('/')[-1]"            
        
    def close(self):
        self.DirName    = null
        self.Niveau     = null
        self.listDir    = null
        self.listFile   = null
        
    def fopen(self, filename):
        # Ouvre le Fichier passer en parametre
        print self.DirName + filename 
        for i in self.listFile :
            if i[0] == self.DirName + filename :
                File = TarFile(i)
                return File
             
######################################################################## 
