import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from qt_material import apply_stylesheet
from Add_user import AnotherWindow
from retrive_data import UserDataWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 300, 300)  # Set window size

        # Apply the Qt Material theme (choose a theme from the available options)
        apply_stylesheet(self, theme='dark_teal.xml')

        # Create buttons
        button_add_user = QPushButton("Add User", self)
        button_add_user.setGeometry(50, 50, 200, 40)
        button_add_user.clicked.connect(self.open_new_window) # Connect the clicked signal to the slot method

        button_connect_call = QPushButton("Connect Call", self)
        button_connect_call.setGeometry(50, 100, 200, 40)
        button_connect_call.clicked.connect(self.open_new_window_1)

        button_retrieve_data = QPushButton("Retrieve Data", self)
        button_retrieve_data.setGeometry(50, 150, 200, 40)

        button_about = QPushButton("About", self)
        button_about.setGeometry(50, 200, 200, 40)

        button_exit = QPushButton("Exit", self)
        button_exit.setGeometry(50, 250, 200, 40)
        button_exit.clicked.connect(self.close)  # Close the application when clicked

        self.new_window = AnotherWindow() # Create an instance of the new window class
        self.new_window_1 = UserDataWidget()
    def open_new_window(self):
        # This method is the slot that will show the new window when the add user button is clicked
        self.new_window.show() # Show the new window
        # self.hide() # Optionally, you can hide the main window
        # self.close() # Optionally, you can close the main window
    def open_new_window_1(self):
        # This method is the slot that will show the new window when the add user button is clicked
        self.new_window_1.show() # Show the new window
        # self.hide() # Optionally, you can hide the main window
        # self.close() # Optionally, you can close the main window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
