# Program Name : text2hex
# Programmer   : The Alpha
# Credits      : Iranpython.blog.ir
# Version      : 0.91(Beta Version)
# Linted By    : Pyflakes
# Info         : text2hex is a simple tool that uses to convert strings to hex.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import binascii

class TextToHex(QDialog):
	def __init__(self):
		QDialog.__init__(self)

		self.setWindowTitle("Text2Hex")

		layout = QGridLayout()

		self.label_cp = QLabel("<b><code><h3>pystudent copyright</h3></code></b>")

		label_text = QLabel("<b><code><h3>Text :</h3></code></b>")
		self.line_edit_text = QLineEdit()

		label_hex = QLabel("<b><code><h3>Hex :</h3></code></b>")
		self.line_edit_hex = QLineEdit()
		self.line_edit_hex.setReadOnly(True)

		self.convert_button = QPushButton("Convert")
		self.exit_button = QPushButton("Exit")

		layout.addWidget(label_text, 0, 0)
		layout.addWidget(self.line_edit_text, 0, 1)
		layout.addWidget(label_hex, 1, 0)
		layout.addWidget(self.line_edit_hex, 1, 1)
		layout.addWidget(self.convert_button, 2, 0)
		layout.addWidget(self.label_cp, 2, 1)
		layout.addWidget(self.exit_button, 2, 2)

		self.convert_button.clicked.connect(self.convertor)
		self.exit_button.clicked.connect(self.close)
		self.setLayout(layout)


	def convertor(self):
		data = self.line_edit_text.text()
		hex_text = binascii.hexlify(bytes(data, 'utf-8'))
		hex_text = str(hex_text)
		hex_text = hex_text.replace("b'", "")
		hex_text = hex_text.replace("'", "")
		hex_text = "0x"+hex_text
		self.line_edit_hex.setText(hex_text)
		if hex_text == "0x":
			self.line_edit_hex.setText("")

app = QApplication(sys.argv)
dialog = TextToHex()
dialog.show()
app.exec_()
