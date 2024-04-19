#import sys
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QImage, QPixmap
#from PyQt5.QtCore import Qt
#import fitz,locale,os
#
#class PDFViewer(QMainWindow):
#    def __init__(self,nome):
#        super().__init__()
#
#        
#
#        self.initUI(nome)
#
#    
#
#    def initUI(self,nome):
#        self.setWindowTitle('PDF Viewer')
#        #self.setGeometry(100, 100, 800, 600)
#
#        def caminho_absoluto_desktop():
#            idioma_sistema = locale.getdefaultlocale()[0].lower()
#
#            if "pt" in idioma_sistema:
#                return os.path.join(os.path.expanduser("~"), "Desktop")
#            else:
#                return os.path.join(os.path.expanduser("~"), "Desktop")
#
#        caminho_desktop = caminho_absoluto_desktop()
#        
#        desktop = QDesktopWidget()
#        screenRect = desktop.screenGeometry()
#        windowRect = self.geometry()
#
#        x = (screenRect.width() - windowRect.width()) // 2
#        y = (screenRect.height() - windowRect.height()) // 2
#
#        # Define a posição da janela
#        self.move(x, y)
#
#        self.central_widget = QWidget(self)
#        self.setCentralWidget(self.central_widget)
#
#        self.layout = QVBoxLayout(self.central_widget)
#
#        self.image_label = QLabel(self)
#        self.layout.addWidget(self.image_label)
#
#        self.open_button = QPushButton(' PDF', self)
#        self.layout.addWidget(self.open_button)
#
#        
#        file_name = caminho_desktop+"/"+nome
#
#        if file_name:
#            self.displayPDF(file_name)
#
#    
#
#    def displayPDF(self, file_name):
#        doc = fitz.open(file_name)
#        page = doc.load_page(0)  # Load the first page (index 0)
#
#        image = page.get_pixmap()
#        img = QImage(image.samples, image.width, image.height, image.stride, QImage.Format_RGB888)
#
#        pixmap = QPixmap.fromImage(img)
#        self.image_label.setPixmap(pixmap)
#
#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    viewer = PDFViewer()
#    viewer.show()
#    sys.exit(app.exec_())
#