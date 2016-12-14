import sys
from PyQt5.QtWidgets import QWidget, QApplication

class Window(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();
	
	def initUI(self):
		self.resize(500, 500)
		self.move(200, 150);
		self.setWindowTitle('Simple_Window');
		self.show();



if __name__=='__main__':
	app=QApplication(sys.argv);
	w=Window();
	sys.exit(app.exec_());
