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
import asyncio
import sys
from PySide2.QtGui import QColor, QIcon, Qt
from PySide2.QtWidgets import QFrame, QTableWidget, QVBoxLayout, QTableWidgetItem, QApplication, QWidget, QComboBox, \
    QCheckBox, QMenuBar, QAction, QHBoxLayout, QPushButton, QLabel


class MenuBar(QMenuBar):
    """MenuBar

            Summary:
                A class for an menu bar that includes:

                -

            Attributes:


            Methods:


            Attributes
            ----------
                label : QLabel
                    Text Label for Input Box
                 :


            Methods
            -------
                get_input_text(self)
                    Return the text in the input box
                (self, value : string)

        """

    def __init__(self, parent):
        super(MenuBar, self).__init__(parent)
        self.setStyleSheet("background-color: #E4F3F5")

        # File Menu
        self.file_menu = self.addMenu('File')
        # Open button
        self.open_button = QAction(QIcon('exit24.png'), 'Open', self)
        self.open_button.setShortcut('Ctrl+O')
        self.open_button.setStatusTip('Open')
        # New Button
        self.new_button = QAction(QIcon('exit24.png'), 'New', self)
        self.new_button.setShortcut('Ctrl+N')
        self.new_button.setStatusTip('New')
        # new_button.triggered.connect()
        # Save Button
        self.save_button = QAction(QIcon('exit24.png'), 'Save', self)
        self.save_button.setShortcut('Ctrl+S')
        self.save_button.setStatusTip('Save')
        # save_button.triggered.connect()
        # Exit Button
        self.exit_button = QAction(QIcon('exit24.png'), 'Exit', self)
        self.exit_button.setShortcut('Ctrl+Q')
        self.exit_button.setStatusTip('Exit application')
        self.exit_button.triggered.connect(self.topLevelWidget().close)
        # Add actions to file menu
        self.file_menu.addAction(self.new_button)
        self.file_menu.addAction(self.open_button)
        self.file_menu.addAction(self.save_button)
        self.file_menu.addAction(self.exit_button)


class MainButtons(QHBoxLayout):
    """Main Buttons in container

            Summary:
                A class for an menu bar that includes:

                -

            Attributes:


            Methods:


            Attributes
            ----------
                label : QLabel
                    Text Label for Input Box
                 :


            Methods
            -------
                get_input_text(self)
                    Return the text in the input box
                (self, value : string)

        """

    def __init__(self, parent):
        super(MainButtons, self).__init__(parent)

        # Spacer label
        self.statLbl = QLabel("")

        # Buttons
        self.continueBtn = QPushButton("Continue")
        self.continueBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);margin:1 23;padding:10;"
                                       "border:2px solid blue;border-radius:20px")

        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.setStyleSheet("margin:1 23;color:rgb(85,0,255); background-color:rgb(255,255,255);"
                                     "padding:10;border:2px solid blue;border-radius:20px")

        self.addWidget(self.statLbl)
        self.addWidget(self.statLbl)
        self.addWidget(self.cancelBtn)
        self.addWidget(self.continueBtn)
