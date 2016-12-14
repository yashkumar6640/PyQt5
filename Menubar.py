import sys;
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon;

class Window(QMainWindow):
	def __init__(self):
		super().__init__();
		self.initUI();

	def initUI(self):
		exitAction=QAction(QIcon('exit.png'), '&Exit', self);
		exitAction.setShortcut('Ctrl+Q');
		exitAction.setStatusTip('Exit Application');
		exitAction.triggered.connect(qApp.quit);


		self.statusBar();

		menubar=self.menuBar();
		fileMenu=menubar.addMenu('&File');
		fileMenu.addAction(exitAction);

		self.setGeometry(300, 300, 300, 200);
		self.setWindowTitle("Menubar");
		self.show();



if __name__=='__main__':
	app=QApplication(sys.argv);
	w=Window();
	sys.exit(app.exec_());