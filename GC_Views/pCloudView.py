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

from GC_Components.InputComponents import LabeledInputWithButton


class PCloudView(QFrame):
    """PCloud View

                    Summary:
                        A class for {Type} that includes:

                        -{Description} to the {Location eg left}

                    Attributes:
                        main_layout, pCloudPath

                    Methods:
                        None

                    Attributes
                    ----------
                        main_layout : QVBoxLayout
                        pCloudPath : LabeledInputWithButton
                            Labeled Input With Button for pCloud link

                    Methods
                    -------
                        None
                """
    def __init__(self, parent=None):
        """Constructor:
                                    Initialize pCloud View

                                    Parameters:
                                        self
                                        parent : QFrame
                                    Returns:
                                        None
                                """
        super(PCloudView, self).__init__(parent)

        self.pCloudPath = LabeledInputWithButton(self, label_text="Public Shared Link: ", button_text="Open")

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.pCloudPath)
        self.setLayout(self.main_layout)
        self.setStyleSheet('border:none')
        self.topLevelWidget().setStyleSheet('QFrame{border:none} '
                                            'LabeledInputWithButton::QLineEdit{border:1px solid #1000A0}')


