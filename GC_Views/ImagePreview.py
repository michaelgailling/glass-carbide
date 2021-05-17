from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QFrame, QLabel, QVBoxLayout


class ImagePreView(QFrame):
    """Image Preview

                    Summary:
                        A class for {Type} that includes:

                        -{Description} to the {Location eg left}

                    Attributes:
                        label, {AttributeName}

                    Methods:
                        get_input_text, {MethodName}

                    Attributes
                    ----------
                        label : QLabel
                            Text Label for Input Box
                        {AttributeName} : {AttributeClass}
                            {Property} for {Type}

                    Methods
                    -------
                        get_input_text(self)
                            Return the text in the input box
                        {MethodName}({Parameters})
                            {Functionality}
                """
    def __init__(self, parent=None):
        super(ImagePreView, self).__init__(parent)

        self.logo = QLabel(self)
        pixmap = QPixmap('octo.png')
        self.logo.setPixmap(pixmap)

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.logo)
        self.setLayout(self.main_layout)