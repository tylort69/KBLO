import sys
import json
import os
import string
import csv
from PyQt5 import QtWidgets, QtGui, QtCore
# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

# Construct the file path for the file using the current working directory

json_file_path = os.path.join(cwd, "./json", 'defaultfingerlayout.json')
csv_file_path = os.path.join(cwd, "./csv", 'key_objects.csv')

# Open the file and read the JSON data
with open(json_file_path) as f:
    data = json.load(f)

# Get the list of keys from the data
keys = data['keys']

# Create a list to hold the key objects
key_objects = []

# The Hand class represents a hand with fingers
class Hand:
    def __init__(self, hand, thumb_finger, index_finger, middle_finger, ring_finger, pinky_finger):
        self.hand = hand
        self.thumb_finger = thumb_finger
        self.index_finger = index_finger
        self.middle_finger = middle_finger
        self.ring_finger = ring_finger
        self.pinky_finger = pinky_finger

    def get_hand(self):
        return self.hand

    def get_thumb_finger(self):
        return self.thumb_finger

    def get_index_finger(self):
        return self.index_finger

    def get_middle_finger(self):
        return self.middle_finger

    def get_ring_finger(self):
        return self.ring_finger

    def get_pinky_finger(self):
        return self.pinky_finger

# Create a hand object for the left hand
left_hand = Hand("left", "thumb", "index", "middle", "ring", "pinky")

# Create a hand object for the right hand
right_hand = Hand("right", "thumb", "index", "middle", "ring", "pinky")

# The Key class represents a single key on a keyboard
class Key:
    def __init__(self, character, default_value, default_shift_value, allowed_to_be_changed, is_changed, shift_allowed_to_be_changed, is_shift_changed, new_value, new_shift_value, hand_used, finger, key_position):
        self.character = character
        self.default_value = default_value
        self.default_shift_value = default_shift_value
        self.allowed_to_be_changed = allowed_to_be_changed
        self.is_changed = is_changed
        self.shift_allowed_to_be_changed = shift_allowed_to_be_changed
        self.is_shift_changed = is_shift_changed
        self.new_value = new_value
        self.new_shift_value = new_shift_value
        self.hand_used = hand_used
        self.finger = finger
        self.key_position = key_position

    def get_character(self):
        return self.character

    def get_default_value(self):
        return self.default_value

    def get_default_shift_value(self):
        return self.default_shift_value

    def get_allowed_to_be_changed(self):
        return self.allowed_to_be_changed

    def get_is_changed(self):
        return self.is_changed

    def get_shift_allowed_to_be_changed(self):
        return self.shift_allowed_to_be_changed

    def get_is_shift_changed(self):
        return self.is_shift_changed

    def get_new_value(self):
        return self.new_value

    def get_new_shift_value(self):
        return self.new_shift_value

    def get_hand_used(self):
        return self.hand_used

    def get_finger(self):
        return self.finger

    def get_key_position(self):
        return self.key_position

    def update_properties(self, character, default_value, default_shift_value, allowed_to_be_changed, is_changed, shift_allowed_to_be_changed, is_shift_changed, new_value, new_shift_value, hand_used, finger, key_position):
        self.character = character
        self.default_value = default_value
        self.default_shift_value = default_shift_value
        self.allowed_to_be_changed = allowed_to_be_changed
        self.is_changed = is_changed
        self.shift_allowed_to_be_changed = shift_allowed_to_be_changed
        self.is_shift_changed = is_shift_changed
        self.new_value = new_value
        self.new_shift_value = new_shift_value
        self.hand_used = hand_used
        self.finger = finger
        self.key_position = key_position

    def __str__(self):
        # Return a string representation of the key object
        return f"Character: {self.character}, Default value: {self.default_value}, Default shift value: {self.default_shift_value}, Allowed to be changed: {self.allowed_to_be_changed}, Is changed: {self.is_changed}, Shift allowed to be changed: {self.shift_allowed_to_be_changed}, Is shift changed: {self.is_shift_changed}, New value: {self.new_value}, New shift value: {self.new_shift_value}, Hand used: {self.hand_used}, Finger: {self.finger}, Key position: {self.key_position}"

# Generate a list of all characters on the keyboard
characters = [chr(i) for i in range(ord(' '), ord('~')+1)]

# Create a list to hold the key objects
key_objects = []

# Iterate over the list of keys
for key in keys:
    # Get the primary and shift values for the key
    primary = key['primary']
    if 'shift' in key:
        shift = key['shift']
    else:
        # Set the shift value to an empty string if it doesn't exist
        shift = ""

    # Get the finger used for the key
    finger = key['finger']

    # Determine the hand and finger to use for the key
    if finger == 1:
        hand = left_hand.hand
        finger = left_hand.pinky_finger
    elif finger == 2:
        hand = left_hand.hand
        finger = left_hand.ring_finger
    elif finger == 3:
        hand = left_hand.hand
        finger = left_hand.middle_finger
    elif finger == 4:
        hand = left_hand.hand
        finger = left_hand.index_finger
    elif finger == 5:
        hand = left_hand.hand
        finger = left_hand.thumb_finger
    elif finger == 6:
        hand = right_hand.hand
        finger = right_hand.thumb_finger
    elif finger == 7:
        hand = right_hand.hand
        finger = right_hand.index_finger
    elif finger == 8:
        hand = right_hand.hand
        finger = right_hand.middle_finger
    elif finger == 9:
        hand = right_hand.hand
        finger = right_hand.ring_finger
    elif finger == 10:
        hand = right_hand.hand
        finger = right_hand.pinky_finger

    # Create a key object
    key_obj = Key(primary, primary, shift, True, False, False, False, "", "", hand, finger, (0, 0))

    # Add the key object to the list
    key_objects.append(key_obj)

# Define the update_key_properties() function
def update_key_properties(key_objects, value, update_shift, update_symbols, update_number, update_shortcuts):
    # Create a list to hold the updated key objects
    updated_keys = []

    # Iterate over the key objects
    for key in key_objects:
        # Update the properties for the key
        key.update_properties(key.character, key.default_value, key.default_shift_value, value, key.is_changed, update_shift, key.is_shift_changed, key.new_value, key.new_shift_value, key.hand_used, key.finger, key.key_position)

        # Print the updated key object
        print(key)

        # Add the updated key object to the list
        updated_keys.append(key)

    # Return the list of updated key objects
    return updated_keys
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Keyboard Configurator")
        self.setGeometry(100, 100, 600, 400)

        self.options = ["Change Letters", "Change Numbers", "Change Symbols", "Change Shift Layer", "Change Shortcuts"]
        self.selected_files = []

        self.options_group = QtWidgets.QGroupBox("Options")
        self.options_layout = QtWidgets.QVBoxLayout()
        for option in self.options:
            button = QtWidgets.QCheckBox(option)
            self.options_layout.addWidget(button)
        self.options_group.setLayout(self.options_layout)

        self.files_group = QtWidgets.QGroupBox("Files")
        self.files_layout = QtWidgets.QVBoxLayout()
        self.files_list = QtWidgets.QListWidget()
        self.files_layout.addWidget(self.files_list)
        self.select_button = QtWidgets.QPushButton("Select")
        self.select_button.clicked.connect(self.select_files)
        self.files_layout.addWidget(self.select_button)
        self.files_group.setLayout(self.files_layout)

        self.selected_group = QtWidgets.QGroupBox("Selected Data Sets")
        self.selected_layout = QtWidgets.QVBoxLayout()
        self.selected_list = QtWidgets.QListWidget()
        self.selected_layout.addWidget(self.selected_list)
        self.remove_button = QtWidgets.QPushButton("Remove")
        self.remove_button.clicked.connect(self.remove_files)
        self.selected_layout.addWidget(self.remove_button)
        self.selected_group.setLayout(self.selected_layout)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.button_layout = QtWidgets.QHBoxLayout()
        self.generate_button = QtWidgets.QPushButton("Generate")
        self.button_layout.addWidget(self.generate_button)
        self.view_button = QtWidgets.QPushButton("View")
        self.button_layout.addWidget(self.view_button)
        self.main_layout.addLayout(self.button_layout)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.options_group)
        layout.addWidget(self.files_group)
        layout.addWidget(self.selected_group)
        self.main_layout.addLayout(layout)

        widget = QtWidgets.QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

        directory = "./resources"
        for filename in os.listdir(directory):
            self.files_list.addItem(filename)

        self.options_group = QtWidgets.QGroupBox("Options")
        self.options_layout = QtWidgets.QVBoxLayout()
        self.checkboxes = []
        for option in self.options:
            button = QtWidgets.QCheckBox(option)
            button.clicked.connect(self.checkbox_clicked)
            self.options_layout.addWidget(button)
            self.checkboxes.append(button)
        self.options_group.setLayout(self.options_layout)

        # Connect the clicked signal to a function that updates the properties of the key objects
        self.options_layout.itemAt(0).clicked.connect(lambda: update_key_properties(key_objects, self.letters_check.isChecked(), self.shift_layer_check.isChecked(), self.symbols_check.isChecked(), self.numbers_check.isChecked(), self.shortcuts_check.isChecked()))
        self.numbers_check.clicked.connect(lambda: update_key_properties(key_objects, self.letters_check.isChecked(), self.shift_layer_check.isChecked(), self.symbols_check.isChecked(), self.numbers_check.isChecked(), self.shortcuts_check.isChecked()))
        self.symbols_check.clicked.connect(lambda: update_key_properties(key_objects, self.letters_check.isChecked(), self.shift_layer_check.isChecked(), self.symbols_check.isChecked(), self.numbers_check.isChecked(), self.shortcuts_check.isChecked()))
        self.shift_layer_check.clicked.connect(lambda: update_key_properties(key_objects, self.letters_check.isChecked(), self.shift_layer_check.isChecked(), self.symbols_check.isChecked(), self.numbers_check.isChecked(), self.shortcuts_check.isChecked()))
        self.shortcuts_check.clicked.connect(lambda: update_key_properties(key_objects, self.letters_check.isChecked(), self.shift_layer_check.isChecked(), self.symbols_check.isChecked(), self.numbers_check.isChecked(), self.shortcuts_check.isChecked()))
        
        



    def select_files(self):
        selected_files = [item.text() for item in self.files_list.selectedItems()]
        for filename in selected_files:
            self.selected_list.addItem(filename)
            self.selected_files.append(filename)

    def remove_files(self):
        selected_items = self.selected_list.selectedItems()
        for item in selected_items:
            filename = item.text()
            self.selected_files.remove(filename)
            self.selected_list.takeItem(self.selected_list.row(item))
   
        
# Open a file for writing
with open(csv_file_path, 'w') as csvfile:
    # Create a writer object
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['character', 'default_value', 'default_shift_value', 'allowed_to_be_changed', 'is_changed', 'shift_allowed_to_be_changed', 'is_shift_changed', 'new_value', 'new_shift_value', 'hand_used', 'finger', 'key_position'])

    # Iterate over the list of key objects
    for key in key_objects:
        # Write a row for each key object
        writer.writerow([key.get_character(), key.get_default_value(), key.get_default_shift_value(), key.get_allowed_to_be_changed(), key.get_is_changed(), key.get_shift_allowed_to_be_changed(), key.get_is_shift_changed(), key.get_new_value(), key.get_new_shift_value(), key.get_hand_used(), key.get_finger(), key.get_key_position()])
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
