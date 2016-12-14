import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
	def __init__(self):
		super().__init__();
		self.initUI();

	def initUI(self):
		self.statusBar().showMessage('Ready');
		self.setGeometry(500, 500, 500, 500);
		self.setWindowTitle('Status Bar');
		self.show();

if __name__=='__main__':
	app=QApplication(sys.argv);
	w=Window();
	sys.exit(app.exec_());
