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


from PySide2.QtWidgets import QFrame, QVBoxLayout

from GC_Components.InputComponents import LabeledDirectoryInput


class ExistingDirectoryView(QFrame):
    """Existing Directory View

                    Summary:
                        A class for {Type} that includes:

                        -{Description}

                    Attributes:
                        main_layout, directoryPath

                    Methods:
                        None

                    Attributes
                    ----------
                        main_layout : QVBoxLayout
                            Vertical Layout
                        directoryPath : LabeledDirectoryInput
                            !!! {Property} for {Type}

                    Methods
                    -------
                        None
                """
    def __init__(self, parent=None):
        """Constructor:
                    Initialize Existing Directory View

                    Parameters:
                        self
                        parent : QFrame
                    Returns:
                        None
                """
        super(ExistingDirectoryView, self).__init__(parent)

        self.directoryPath = LabeledDirectoryInput(self, label_text="Select Root Folder: ")

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.directoryPath)
        self.setLayout(self.main_layout)
        self.setStyleSheet('LabeledDirectoryInput{border:none}')
