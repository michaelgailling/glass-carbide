from PySide2.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog


class LabeledInput(QFrame):
    def __init__(self, parent, label_text="", input_text=""):
        super(LabeledInput, self).__init__(parent)

        self.hBox = QHBoxLayout()
        self.label = QLabel(self)
        self.label.text(label_text)

        self.input = QLineEdit(self)
        self.input.text(input_text)

        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.input)

    def get_input_text(self):
        return self.input.text()

    def set_input_text(self, value):
        self.input.text(str(value))


class LabeledPathInput(QFrame):
    def __init__(self, parent, label_text="", input_text=""):
        super(LabeledPathInput, self).__init__(parent)

        self.hBox = QHBoxLayout()
        self.label = QLabel(self)
        self.label.text(label_text)

        self.input = QLineEdit(self)
        self.input.text(input_text)

        self.fileDialogButton = QPushButton("...")
        self.fileDialogButton.clicked(self.open_directory_dialog())

        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.input)

    def get_input_text(self):
        return self.input.text()

    def set_input_text(self, value):
        self.input.text(str(value))

    def open_directory_dialog(self):
        directory_dialog = QFileDialog()
        directory_path = directory_dialog.getExistingDirectory(self, "Select a Directory")
        self.set_input_text(directory_path)
