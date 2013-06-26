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
        
    def readdir(self, _Param):
        # Liste le contenue
    

        for i in self.listDir :
            if i[1] == self.Niveau+1 and i[0].find(self.DirName) == 0: 
                print colored(i[0].split('/')[-2] + '/','green')
                temp = self.DirName+i[0].split('/')[-2] + '/'
                if _Param == 1 : 
                    #Recurcivite
                    for y in self.listDir :
                        if y[1] == self.Niveau+2 and y[0].find(self.DirName) == 0: 
                            print colored("  |  " + y[0].split('/')[-2] + '/','green')
                            
                            for z in self.listFile :
                                if z[1] == self.Niveau+2 and z[0].find(temp) == 0:
                                    print colored("  |  " + z[0].split('/')[-1], 'magenta')
                
                    
        for i in self.listFile :
            if i[1] == self.Niveau+1 and i[0].find(self.DirName) == 0:
                print colored(i[0].split('/')[-1], 'magenta')
           
                      
        
    def close(self):
        self.DirName    = null
        self.Niveau     = null
        self.listDir    = null
        self.listFile   = null
        
    def fopen(self, filename):
        # Ouvre le Fichier passer en parametre
        #print self.DirName + filename
        FindFile = 0 
        for i in self.listFile :
            if i[0] == self.DirName + filename :
                FindFile = 1
                File = TarFile(i)
                return File

    


        
             
######################################################################## 
