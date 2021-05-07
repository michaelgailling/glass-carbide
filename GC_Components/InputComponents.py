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
import os

from PySide2.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog


# Composite Text Input Elements
class LabeledInput(QFrame):
    """Labeled Input

        Summary:
            A class for an input box that includes:

            -Label to the left

        Attributes:
            label, input

        Methods:
            get_input_text, set_input_text

        Attributes
        ----------
            label : QLabel
                Text Label for Input Box
            input : QLineEdit
                Input Box for text entry

        Methods
        -------
            get_input_text(self)
                Return the text in the input box
            set_input_text(self, value : string)
                Sets the input box text
    """
    def __init__(self, parent, label_text="", input_text=""):
        super(LabeledInput, self).__init__(parent)

        self.label = QLabel(self, text=label_text)

        self.input = QLineEdit(self)
        self.input.setText(input_text)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.input)

        self.setLayout(self.hBox)

    def get_input_text(self):
        text = self.input.text()
        return text

    def set_input_text(self, value):
        self.input.setText(str(value))


class LabeledInputWithButton(QFrame):
    """Labeled Input with button

        Summary:
            A class for an input box that includes:

            -Label to the left

        Attributes:
            label, input

        Methods:
            get_input_text, set_input_text

        Attributes
        ----------
            label : QLabel
                Text Label for Input Box
            input : QLineEdit
                Input Box for text entry

        Methods
        -------
            get_input_text(self)
                Return the text in the input box
            set_input_text(self, value : string)
                Sets the input box text
    """
    def __init__(self, parent, label_text="", input_text="", button_text="", btn_enable=True):
        super(LabeledInputWithButton, self).__init__(parent)

        self.label = QLabel(self, text=label_text)

        self.input = QLineEdit(self)
        self.input.setText(input_text)

        self.button = QPushButton(button_text)
        self.button.setStyleSheet("background-color:#1000A0;color:white;padding:3px")
        self.button.setEnabled(btn_enable)
        self.button.setObjectName('browse')

        self.hBox = QHBoxLayout(self)
        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.input)
        self.hBox.addWidget(self.button)

        self.setLayout(self.hBox)

    def get_input_text(self):
        text = self.input.text()
        return text

    def set_input_text(self, value):
        self.input.setText(str(value))


class DirectoryInput(QFrame):
    """Directory Input

            Summary:
                A class for an input box that includes:

                -File dialog button to the right

            Attributes:
                input, fileDialogButton

            Methods:
                get_input_text, set_input_text, open_directory_dialog

            Attributes
            ----------
                fileDialogButton : QPushButton
                    A button that opens a file dialog
                input : QLineEdit
                    Input Box for text entry

            Methods
            -------
                get_input_text(self)
                    Return the text in the input box
                set_input_text(self, value : string)
                    Sets the input box text
                open_directory_dialog(self)
                    Opens the directory selection dialog
        """
    def __init__(self, parent, input_text="", read_only=False, btn_enable=True):
        super(DirectoryInput, self).__init__(parent)

        self.input = QLineEdit(self)
        self.input.setText(input_text)
        self.input.setReadOnly(read_only)

        self.fileDialogButton = QPushButton(self, text="...")
        self.fileDialogButton.clicked.connect(self.open_directory_dialog)
        self.fileDialogButton.setEnabled(btn_enable)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.input)
        self.hBox.addWidget(self.fileDialogButton)

        self.setLayout(self.hBox)

    def get_input_text(self):
        text = self.input.text()
        return text

    def set_input_text(self, value):
        self.input.setText(str(value))

    def open_directory_dialog(self):
        directory_dialog = QFileDialog()
        directory_path = directory_dialog.getExistingDirectory(self, "Select a Directory", self.get_input_text())
        if os.path.isdir(directory_path):
            self.set_input_text(directory_path)


class LabeledDirectoryInput(QFrame):
    """Labeled Directory Input

            Summary:
                A class for an input box that includes:

                -Label to the left

                -File dialog button to the right

            Attributes:
                label, input, fileDialogButton

            Methods:
                get_input_text, set_input_text, open_directory_dialog

            Attributes
            ----------
                label : QLabel
                    Text Label for Input Box
                fileDialogButton : QPushButton
                    A button that opens a file dialog
                input : QLineEdit
                    Input Box for text entry

            Methods
            -------
                get_input_text(self)
                    Return the text in the input box
                set_input_text(self, value : string)
                    Sets the input box text
                open_directory_dialog(self)
                    Opens the directory selection dialog
        """
    def __init__(self, parent, label_text="", input_text="", read_only=False, btn_enable=True):
        super(LabeledDirectoryInput, self).__init__(parent)

        self.label = QLabel(self, text=label_text)

        self.input = QLineEdit(self)
        self.input.setText(input_text)
        self.input.setReadOnly(read_only)

        self.fileDialogButton = QPushButton(self, text="Browse")
        self.fileDialogButton.setStyleSheet("background-color:#1000A0;color:white;padding:3px")
        self.fileDialogButton.clicked.connect(self.open_directory_dialog)
        self.fileDialogButton.setEnabled(btn_enable)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.input)
        self.hBox.addWidget(self.fileDialogButton)

        self.setLayout(self.hBox)

    def get_input_text(self):
        text = self.input.text()
        return text

    def set_input_text(self, value):
        self.input.setText(str(value))

    def open_directory_dialog(self):
        directory_dialog = QFileDialog()
        directory_path = directory_dialog.getExistingDirectory(self, "Select a Directory", self.get_input_text())
        if os.path.isdir(directory_path):
            self.set_input_text(directory_path)


class FileInput(QFrame):
    """File Input

        Summary:
            A class for an input box that includes:

            -File dialog button to the right

        Attributes:
            input, fileDialogButton

        Methods:
            get_input_text, set_input_text, open_file_dialog

        Attributes
        ----------
            fileDialogButton : QPushButton
                A button that opens a file dialog
            input : QLineEdit
                Input Box for text entry

        Methods
        -------
            get_input_text(self)
                Return the text in the input box
            set_input_text(self, value : string)
                Sets the input box text
            open_file_dialog(self)
                Opens the file selection dialog
    """
    def __init__(self, parent, file_type="", input_text="", read_only=False, btn_enable=True):
        super(FileInput, self).__init__(parent)

        self.file_type = file_type

        self.input = QLineEdit(self)
        self.input.setText(input_text)
        self.input.setReadOnly(read_only)

        self.fileDialogButton = QPushButton("...")
        self.fileDialogButton.clicked.connect(self.open_file_dialog)
        self.fileDialogButton.setEnabled(btn_enable)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.input)
        self.hBox.addWidget(self.fileDialogButton)

        self.setLayout(self.hBox)

    def get_input_text(self):
        text = self.input.text()
        return text

    def set_input_text(self, value):
        self.input.setText(str(value))

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        if self.file_type:
            file_path = file_dialog.getOpenFileName(self, "Select File", self.get_input_text(), filter=self.file_type)
        else:
            file_path = file_dialog.getOpenFileName(self, "Select File")

        if os.path.isfile(file_path[0]):
            self.set_input_text(file_path[0])


class LabeledFileInput(QFrame):
    """Labeled File Input

        Summary:
            A class for an input box that includes:

            -Label to the left

            -File dialog button to the right

        Attributes:
            label, input, fileDialogButton

        Methods:
            get_input_text, set_input_text, open_file_dialog

        Attributes
        ----------
            label : QLabel
                Text Label for Input Box
            fileDialogButton : QPushButton
                A button that opens a file dialog
            input : QLineEdit
                Input Box for text entry

        Methods
        -------
            get_input_text(self)
                Return the text in the input box
            set_input_text(self, value : string)
                Sets the input box text
            open_file_dialog(self)
                Opens the file selection dialog
    """
    def __init__(self, parent, label_text="", file_type="", input_text="", read_only=False, btn_enable=True):
        super(LabeledFileInput, self).__init__(parent)

        self.file_type = file_type

        self.label = QLabel(self, text=label_text)

        self.input = QLineEdit(self)
        self.input.setText(input_text)
        self.input.setReadOnly(read_only)

        self.fileDialogButton = QPushButton(label_text)
        self.fileDialogButton.setStyleSheet("background-color:#1000A0;color:white;")
        self.fileDialogButton.clicked.connect(self.open_file_dialog)
        self.fileDialogButton.setEnabled(btn_enable)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.input)
        self.hBox.addWidget(self.fileDialogButton)

        self.setLayout(self.hBox)

    def get_input_text(self):
        text = self.input.text()
        return text

    def set_input_text(self, value):
        self.input.setText(str(value))

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        if self.file_type:
            file_path = file_dialog.getOpenFileName(self, "Select File", self.get_input_text(), filter=self.file_type)
        else:
            file_path = file_dialog.getOpenFileName(self, "Select File")
        if os.path.isfile(file_path[0]):
            self.set_input_text(file_path[0])
