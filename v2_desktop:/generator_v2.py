import sys  # gives access to system-level parameters (needed for QApplication)
import random  # used to randomly choose characters for the password
import string  # contains useful predefined character sets

from PyQt5.QtWidgets import (  # import all required PyQt5 GUI components
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QLineEdit, QSlider, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt  # import Qt core constants (alignment, orientation,       etc.)

class PasswordGenerator(QWidget): # create a window class that inherits from QWidget
    def __init__(self):  # constructor that runs when the window is created
        super().__init__()  # initialize parent QWidget

        self.setWindowTitle("Password Generator") # set title of the window
        self.setFixedSize(450, 280)  # fix window size to specific width/height

        self.dark_mode = False  # variable for tracking theme state (light/dark)

        layout = QVBoxLayout()  # create a vertical layout for the interface
        layout.setSpacing(10)  # add space between widgets

        self.title = QLabel("🔒 Password Generator")  # create a title label
       
        self.title.setAlignment(Qt.AlignCenter)  # center align the title
        self.title.setStyleSheet("font-size: 22px; font-weight: bold;") # style title
        layout.addWidget(self.title)  # add title to layout

        self.password_field = QLineEdit()  # text field to display password
        self.password_field.setReadOnly(True)  # prevent user from typing inside it
        self.password_field.setStyleSheet(  # basic styling

        "font-size: 13px; padding: 3px; border: 2 solid #7f8c8d; border-radius: 8px;"
        )

        layout.addWidget(self.password_field)  # add password field to layout

        slider_layout = QHBoxLayout() # create horizontal layout for slider and label

        self.slider_label = QLabel("How Long: 12")  # label showing chosen length
        self.slider_label.setStyleSheet("font-size: 15px;")  # style the label
        slider_layout.addWidget(self.slider_label)  # add label to layout

        self.slider = QSlider(Qt.Horizontal)  # create horizontal slider widget
        self.slider.setRange(6, 50)  # slider min/max allowed values
        self.slider.setValue(12)  # default slider position
        self.slider.setMinimumHeight(30)  # visual size boost
        self.slider.valueChanged.connect(self.update_length_label)  # update label on change
        slider_layout.addWidget(self.slider)  # add slider to layout

        layout.addLayout(slider_layout)  # add slider layout to main layout

        self.generate_btn = QPushButton("Generate")  # button to generate password
        self.generate_btn.setStyleSheet(self.button_style())  # apply style
        self.generate_btn.clicked.connect(self.generate_password)  # bind to function
        layout.addWidget(self.generate_btn)  # add button to layout

        self.copy_btn = QPushButton("Copy")  # button to copy password
        self.copy_btn.setStyleSheet(self.button_style())  # apply style
        self.copy_btn.clicked.connect(self.copy_password)  # bind to function
        layout.addWidget(self.copy_btn)  # add button to layout

        self.theme_btn = QPushButton("Theme")  # button to toggle theme
      
        self.theme_btn.setStyleSheet(self.button_style())  # apply style
        self.theme_btn.clicked.connect(self.toggle_theme)  # bind to function
        layout.addWidget(self.theme_btn)  # add button to layout

        self.setLayout(layout)  # apply main layout to the window

        self.apply_theme()  # apply initial (light) theme on startup

    def update_length_label(self):  # updates displayed number when slider moves
        self.slider_label.setText(f"How Long: {self.slider.value()}") # update label

    def generate_password(self):  # function to generate a password
        length = self.slider.value()  # read the chosen password length
        chars = string.ascii_letters + string.digits + string.punctuation  # character set
        password = ''.join(random.choice(chars) for _ in range(length))  # generate              random pwd
        self.password_field.setText(password)  # display password in textbox

    def copy_password(self):  # copies the password to system clipboard
        password = self.password_field.text()  # get current password
        if not password:  # if empty, do nothing
            return
        QApplication.clipboard().setText(password)  # copy password

        msg = QMessageBox(self)  # create popup notification
        msg.setWindowTitle("Copied")  # popup title
        msg.setText("Your password is Copied!")  # popup message
        msg.setStandardButtons(QMessageBox.Ok)  # show OK button
        msg.setWindowModality(Qt.NonModal)  # allow interaction behind popup
        msg.setStyleSheet("QLabel{min-width:250px; text-align:center;}")  # style
        msg.show()  # display popup

    def toggle_theme(self):  # switches between dark/light mode
        self.dark_mode = not self.dark_mode  # invert the boolean value
        self.apply_theme()  # reapply theme settings

    def apply_theme(self):  # chooses and applies correct theme
        if self.dark_mode:  # dark theme activated
            self.setStyleSheet("""
               
                QWidget { background-color: #2c3e50; color: white; }
                QLineEdit { background-color: #34495e; color: white; border: 2px solid  #1abc9c; }
            """)
        else:  # light theme activated
            self.setStyleSheet("""
                QWidget { background-color: white; color: black; }
                QLineEdit { background-color: white; color: black; border: 2px solid #7f8c8d; }
            """)
        self.generate_btn.setStyleSheet(self.button_style())  # update button styles
        self.copy_btn.setStyleSheet(self.button_style())

        self.theme_btn.setStyleSheet(self.button_style())

    def button_style(self):  # returns style depending on theme
        if self.dark_mode:  # dark theme button style
            return """
                QPushButton {
                    background-color: #1abc9c;
                    color: black;
                    font-size: 16px;
                    padding: 4px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #16a085;
                }
            """
        else:  # light theme button style
            return """
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    font-size: 16px;
                    padding: 4px;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                
               }
               """

if __name__ == "__main__":  # main entry point of the program
    app = QApplication(sys.argv)  # create Qt application
    window = PasswordGenerator()  # create main window object
    window.show()  # display the window
    sys.exit(app.exec_())  # start the application event loop