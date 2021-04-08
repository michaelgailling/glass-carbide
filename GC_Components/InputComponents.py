# Project Name:
# Glass Carbide
#
# By:
# Michael Gailling
# &&
# Mustafa Butt
#
# Organization:
# WIMTACH
#


from PySide2.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog


class LabeledInput(QFrame):
    def __init__(self, parent, label_text="", input_text=""):
        super(LabeledInput, self).__init__(parent)

        self.label = QLabel(self, text=label_text)

        self.input = QLineEdit(self)
        self.input.text = input_text

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.input)

    def get_input_text(self):
        return self.input.text

    def set_input_text(self, value):
        self.input.setText(str(value))


class LabeledDirectoryInput(QFrame):
    def __init__(self, parent, label_text="", input_text=""):
        super(LabeledDirectoryInput, self).__init__(parent)

        self.label = QLabel(self, text=label_text)

        self.input = QLineEdit(self)
        self.input.text = input_text

        self.fileDialogButton = QPushButton(self, text="...")
        self.fileDialogButton.clicked.connect(self.open_directory_dialog)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.input)
        self.hBox.addWidget(self.fileDialogButton)

        self.setLayout(self.hBox)

    def get_input_text(self):
        return self.input.text()

    def set_input_text(self, value):
        self.input.setText(str(value))

    def open_directory_dialog(self):
        directory_dialog = QFileDialog()
        directory_path = directory_dialog.getExistingDirectory(self, "Select a Directory")
        self.set_input_text(directory_path)


class LabeledFileInput(QFrame):
    def __init__(self, parent, label_text="", input_text=""):
        super(LabeledFileInput, self).__init__(parent)

        self.label = QLabel(self, text=label_text)

        self.input = QLineEdit(self)
        self.input.text = input_text

        self.fileDialogButton = QPushButton("...")
        self.fileDialogButton.clicked.connect(self.open_file_dialog)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.input)
        self.hBox.addWidget(self.fileDialogButton)

    def get_input_text(self):
        return self.input.text()

    def set_input_text(self, value):
        self.input.setText(str(value))

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName(self, "Select File")
        self.set_input_text(file_path)

