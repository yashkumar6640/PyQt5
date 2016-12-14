import sys
from PyQt5.QtWidgets import QApplication, qApp, QMainWindow, QAction, QTextEdit, QMessageBox;
from PyQt5.QtGui import QIcon;

class Window(QMainWindow):
	def __init__(self):
		super().__init__();
		self.initUI();

	def initUI(self):
		textEdit=QTextEdit();
		self.setCentralWidget(textEdit);
	
		exitAction=QAction(QIcon('resource-configpng.png'), '&Exit', self);
		exitAction.setShortcut('Ctrl+Q');
		exitAction.triggered.connect(qApp.quit);

		menubar=self.menuBar();
		filemenu=menubar.addMenu('&File');
		filemenu.addAction(exitAction);

		self.toolbar=self.addToolBar('Exit');
		self.toolbar.addAction(exitAction);

		self.setGeometry(300, 300, 300, 200);
		self.setWindowTitle('Toolbar');
		self.show();

	def closeEvent(self, event):
		reply=QMessageBox.question(self, 'Message', 'Are you sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes);
		if reply==QMessageBox.Yes:
			event.accept();
		else:
			event.ignore();


if __name__=='__main__':
	app=QApplication(sys.argv);
	w=Window();
	sys.exit(app.exec_());
