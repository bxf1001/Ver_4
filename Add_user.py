import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox
from qt_material import apply_stylesheet

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add User")
        self.setGeometry(100, 100, 300, 200)

        # Create input fields
        self.user_id_input = QLineEdit(self)
        self.value1_input = QLineEdit(self)
        self.value2_input = QLineEdit(self)
        self.value3_input = QLineEdit(self)

        # Create labels
        self.user_id_label = QLabel("User ID:", self)
        self.value1_label = QLabel("No1:", self)
        self.value2_label = QLabel("No2:", self)
        self.value3_label = QLabel("No3:", self)

        # Create submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.store_data) # Connect the clicked signal to the method

        # Apply Material theme
        apply_stylesheet(self, theme='dark_teal.xml')

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.user_id_label)
        layout.addWidget(self.user_id_input)
        layout.addWidget(self.value1_label)
        layout.addWidget(self.value1_input)
        layout.addWidget(self.value2_label)
        layout.addWidget(self.value2_input)
        layout.addWidget(self.value3_label)
        layout.addWidget(self.value3_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def store_data(self):
        # This method will store the data from the input fields into a JSON file and close the window
        data = {} # Create an empty dictionary to store the data
        data["user_id"] = self.user_id_input.text() # Get the text from the user id input field and store it in the dictionary
        data["value1"] = self.value1_input.text() # Get the text from the value1 input field and store it in the dictionary
        data["value2"] = self.value2_input.text() # Get the text from the value2 input field and store it in the dictionary
        data["value3"] = self.value3_input.text() # Get the text from the value3 input field and store it in the dictionary

        # Check if the data file exists
        file_name = "data.json"
        if os.path.exists(file_name):
            # Read the existing data from the file
            with open(file_name, "r") as f:
                existing_data = json.load(f)
            # Check if the user id is already in the file
            if data["user_id"] in existing_data:
                # Create a warning message box
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("User already exists")
                msg.setText("The user ID you entered already exists in the data file. Please enter a different user ID.")
                msg.setStandardButtons(QMessageBox.Ok)
                # Show the message box and wait for the user to click the button
                msg.exec_()
                # Return from the method without writing the data or closing the window
                return
        else:
            # Create an empty dictionary for the existing data
            existing_data = {}

        # Add the new data to the existing data
        existing_data[data["user_id"]] = data

        # Write the updated data to the file
        with open(file_name, "w") as f:
            json.dump(existing_data, f, indent=4)

        # Close the window
        self.close()
