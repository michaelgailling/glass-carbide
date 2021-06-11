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
from PySide2.QtWidgets import QFrame, QMenuBar, QAction, QHBoxLayout, QPushButton, QLabel


class MenuBar(QMenuBar):
    """MenuBar

            Summary:
                A class for an menu bar that includes:

                -File menu with Open, New, Save & Exit actions

            Attributes:
                file_menu, open_button, new_button, save_button, exit_button

            Methods:
                None

            Attributes
            ----------
                file_menu : QMenuBar
                    Menu Bar with File option
                open_button : QAction
                    Open option in Menu Bar, under File
                new_button : QAction
                    New option in Menu Bar, under File
                save_button : QAction
                    Save option in Menu Bar, under File
                exit_button : QAction
                    Exit option in Menu Bar, under File

            Methods
            -------
                Nonw
        """

    def __init__(self, parent):
        """
            Constructs all the necessary attributes for the MenuBar object.

            Parameters
            ----------
                self
                parent : QMenuBar
        """
        super(MenuBar, self).__init__(parent)
        self.setStyleSheet("background-color: #e6e6e6")

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
    """Main Buttons in an HBox

            Summary:
                A class for MainButtons that includes:

                -Continue & Back buttons in a horizontal layout

            Attributes:
                statLbl, continueBtn, cancelBtn

            Methods:
                None

            Attributes
            ----------
                statLbl : QLabel
                    Blank Label for spacing
                continueBtn : QPushButton
                    Pushbutton to continue to next step/tab
                cancelBtn : QPushButton
                    Pushbutton to go back to previous step/tab

            Methods
            -------
                None
        """

    def __init__(self, parent):
        """Constructor:
            Constructs all the necessary attributes for the Main Buttons container object.

            Parameters
            ----------
                self
                parent : QHboxLayout
        """
        super(MainButtons, self).__init__(parent)

        # Spacer label
        self.statLbl = QLabel("")

        # Buttons
        self.continueBtn = QPushButton("Continue")
        self.continueBtn.setStyleSheet("background-color:#1000A0; color:rgb(255,255,255);margin:1 23;padding:10;"
                                       "border:2px solid #1000A0;border-radius:20px")

        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.setStyleSheet("margin:1 23;color:#1000A0; background-color:rgb(255,255,255);"
                                     "padding:10;border:2px solid #1000A0;border-radius:20px")

        self.addWidget(self.statLbl)
        self.addWidget(self.statLbl)
        self.addWidget(self.cancelBtn)
        self.addWidget(self.continueBtn)


class MainNavButtons(QFrame):
    """Main Navigation Buttons

            Summary:
                A class for MainNavButtons that includes:

                -Continue & Back buttons in a horizontal layout

            Attributes:
                layout, statLbl, continueBtn, cancelBtn

            Methods:
                None

            Attributes
            ----------
                layout : QHBoxLayout
                    Horizontal main layout
                statLbl : QLabel
                    Blank Label for spacing
                continueBtn : QPushButton
                    Pushbutton to continue to next step/tab
                cancelBtn : QPushButton
                    Pushbutton to go back to previous step/tab

            Methods
            -------
                None
        """

    def __init__(self, parent=None):
        """Constructor:
            Constructs all the necessary attributes for the MainNavBar object.

            Parameters
            ----------
                self
                parent : QFrame
        """
        super(MainNavButtons, self).__init__(parent)

        self.layout = QHBoxLayout()

        # Spacer label
        self.statLbl = QLabel("")

        # Buttons
        self.continueBtn = QPushButton("Continue")
        self.continueBtn.setStyleSheet("background-color:#1000A0; color:rgb(255,255,255);margin:1 23;padding:10;"
                                       "border:2px solid #1000A0;border-radius:20px")

        self.backBtn = QPushButton("Back")
        self.backBtn.setStyleSheet("margin:1 23;color:#1000A0; background-color:rgb(255,255,255);padding:10;"
                                   "border:2px solid #1000A0;border-radius:20px")

        self.layout.addWidget(self.statLbl)
        self.layout.addWidget(self.statLbl)
        self.layout.addWidget(self.backBtn)
        self.layout.addWidget(self.continueBtn)

        self.setLayout(self.layout)
