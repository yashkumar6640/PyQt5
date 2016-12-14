import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QToolTip
from PyQt5.QtCore import QCoreApplication

class Window(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();
	
	def initUI(self):
		button = QPushButton('Quit', self);
		button.resize(button.sizeHint());
		button.move(250, 200);
		button.setToolTip('This will force close your window');
		button.show();
		button.clicked.connect(QCoreApplication.instance().quit);
		self.setToolTip('This is a widget');	
		self.resize(500, 500)
		self.move(200, 150);
		self.setWindowTitle('Push Button');
		self.show();

	def closeEvent(self, event):
		reply=QMessageBox.question(self, 'Message', 'Are you sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No);
		if reply == QMessageBox.Yes:
			event.accept();
		else:
			event.ignore();




if __name__=='__main__':
	app=QApplication(sys.argv);
	w=Window();
	sys.exit(app.exec_());
