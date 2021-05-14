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


