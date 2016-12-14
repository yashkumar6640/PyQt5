import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout

class layout(QWidget):
	def __init__(self):
		super().__init__();
		self.initUI();

	def initUI(self):
		okbutton=QPushButton('Ok', self);
		cancelbutton=QPushButton('Cancel', self);

		hbox=QHBoxLayout();
		hbox.addStretch(1);
		hbox.addWidget(okbutton);
		hbox.addWidget(cancelbutton);

		vbox=QVBoxLayout();
		vbox.addStretch(1);
		vbox.addLayout(hbox);

		self.setLayout(vbox);

		self.setGeometry(300, 300, 300, 200);
		self.setWindowTitle("Layout");
		self.show();


if __name__ == '__main__':
	app=QApplication(sys.argv);
	l=layout();
	sys.exit(app.exec_());
