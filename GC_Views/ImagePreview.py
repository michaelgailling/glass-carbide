from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QFrame, QLabel, QVBoxLayout


class ImagePreView(QFrame):
    """Image Preview

        Summary:
            A class for Viewing Images that includes:

            -Pixmap in a label in a vertical layout

        Attributes:
            logo, main_layout, pixmap

        Methods:
            None

        Attributes
        ----------
            main_layout : QVBoxLayout
             Vertical main layout
            logo : QLabel
                Label for storing logo pixmap
            pixmap : QPixmap
                Pixmap for logo

        Methods
        -------
            None
    """
    def __init__(self, parent=None):
        """Constructor:
            Initialize Image Preview View

            Parameters:
                self
                parent : QFrame
            Returns:
                None
        """
        super(ImagePreView, self).__init__(parent)

        self.logo = QLabel(self)
        pixmap = QPixmap('octo.png')
        self.logo.setPixmap(pixmap)

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.logo)
        self.setLayout(self.main_layout)