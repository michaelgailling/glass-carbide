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


# Composite Text Input Elements
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


class DirectoryInput(QFrame):
    def __init__(self, parent, input_text=""):
        super(DirectoryInput, self).__init__(parent)

        self.input = QLineEdit(self)
        self.input.text = input_text

        self.fileDialogButton = QPushButton(self, text="...")
        self.fileDialogButton.clicked.connect(self.open_directory_dialog)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.input)
        self.hBox.addWidget(self.fileDialogButton)

        self.setLayout(self.hBox)

    def get_input_text(self):
        return self.input.text

    def set_input_text(self, value):
        self.input.setText(str(value))

    def open_directory_dialog(self):
        directory_dialog = QFileDialog()
        directory_path = directory_dialog.getExistingDirectory(self, "Select a Directory")
        self.set_input_text(directory_path)


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
        return self.input.text

    def set_input_text(self, value):
        self.input.setText(str(value))

    def open_directory_dialog(self):
        directory_dialog = QFileDialog()
        directory_path = directory_dialog.getExistingDirectory(self, "Select a Directory")
        self.set_input_text(directory_path)


class FileInput(QFrame):
    def __init__(self, parent, file_type="", input_text=""):
        super(FileInput, self).__init__(parent)

        self.file_type = file_type

        self.input = QLineEdit(self)
        self.input.text = input_text

        self.fileDialogButton = QPushButton("...")
        self.fileDialogButton.clicked.connect(self.open_file_dialog)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.input)
        self.hBox.addWidget(self.fileDialogButton)

        self.setLayout(self.hBox)

    def get_input_text(self):
        return self.input.text

    def set_input_text(self, value):
        self.input.setText(str(value))

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        if self.file_type:
            file_path = file_dialog.getOpenFileName(self, "Select File", filter=self.file_type)
        else:
            file_path = file_dialog.getOpenFileName(self, "Select File")

        self.set_input_text(file_path[0])


class LabeledFileInput(QFrame):
    def __init__(self, parent, label_text="", file_type="", input_text=""):
        super(LabeledFileInput, self).__init__(parent)

        self.file_type = file_type

        self.label = QLabel(self, text=label_text)

        self.input = QLineEdit(self)
        self.input.text = input_text

        self.fileDialogButton = QPushButton("...")
        self.fileDialogButton.clicked.connect(self.open_file_dialog)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.input)
        self.hBox.addWidget(self.fileDialogButton)

        self.setLayout(self.hBox)

    def get_input_text(self):
        return self.input.text

    def set_input_text(self, value):
        self.input.setText(str(value))

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        if self.file_type:
            file_path = file_dialog.getOpenFileName(self, "Select File", filter=self.file_type)
        else:
            file_path = file_dialog.getOpenFileName(self, "Select File")

        self.set_input_text(file_path[0])

