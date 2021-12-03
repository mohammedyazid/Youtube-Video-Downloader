from pytube import YouTube
from Ui import Ui_MainWindow
from PyQt5 import QtWidgets
class methods():
    folderpath="/"
    def submitc(self):
        
        self.link = Ui_MainWindow.URL.toPlainText()
        self.yt = YouTube(self.link)
        
        views = str(self.yt.views)
        
        if(self.yt.length>60):
                lengthM = "% s" %(self.yt.length//60)

                lengthS = "% s" %(self.yt.length%60)
        else:
                lengthM = "% s" %0
                lengthS = "% s" %(self.yt.length%60)
        length = str(lengthM)
        twonum = "{:.2f}".format(self.yt.rating)
        rating = str(twonum)
        #Showing details
        Ui_MainWindow.title.setText(self.yt.title)
        Ui_MainWindow.views.setText(views +" views")
        Ui_MainWindow.length.setText(lengthM+":"+lengthS)
        Ui_MainWindow.rating.setText(rating)
        #Getting the highest resolution possible
        self.ys = self.yt.streams.get_highest_resolution()
    def downloadc(self):    
        #Starting download
        Ui_MainWindow.status.setText("Downloading...")
        self.ys.download(methods.folderpath)
        Ui_MainWindow.status.setText("Download completed!!")
    def topath(self):
        methods.folderpath = str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory"))
        Ui_MainWindow.patharea.setText(methods.folderpath)
    def clear(self):
            Ui_MainWindow.URL.setText("")
            Ui_MainWindow.title.setText("")   
            Ui_MainWindow.views.setText("") 
            Ui_MainWindow.length.setText("")  
            Ui_MainWindow.rating.setText("")             
