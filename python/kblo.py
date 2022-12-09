import string
import sys
import json
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QHBoxLayout, QVBoxLayout
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
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keyboard Remapper")
        self.resize(400, 300)

        # Create labels and check boxes for each option
        letters_label = QLabel("Change letters:")
        self.letters_check = QCheckBox()

        numbers_label = QLabel("Change numbers:")
        self.numbers_check = QCheckBox()

        symbols_label = QLabel("Change symbols:")
        self.symbols_check = QCheckBox()

        shift_layer_label = QLabel("Change Shift Layer:")
        self.shift_layer_check = QCheckBox()

        shortcuts_label = QLabel("Change Shortcuts:")
        self.shortcuts_check = QCheckBox()

        # Add the labels and check boxes to the main window
        layout = QVBoxLayout()
        # Create a horizontal layout for the "Change letters" option
        letters_layout = QHBoxLayout()
        letters_layout.addWidget(letters_label)
        letters_layout.addWidget(self.letters_check)
        # Create a horizontal layout for the "Change numbers" option
        numbers_layout = QHBoxLayout()
        numbers_layout.addWidget(numbers_label)
        numbers_layout.addWidget(self.numbers_check)
        # Create a horizontal layout for the "Change symbols" option
        symbols_layout = QHBoxLayout()
        symbols_layout.addWidget(symbols_label)
        symbols_layout.addWidget(self.symbols_check)
        # Create a horizontal layout for the "Change Shift Layer" option
        shift_layer_layout = QHBoxLayout()
        shift_layer_layout.addWidget(shift_layer_label)
        shift_layer_layout.addWidget(self.shift_layer_check)
        # Create a horizontal layout for the "Change Shortcuts" option
        shortcuts_layout = QHBoxLayout()
        shortcuts_layout.addWidget(shortcuts_label)
        shortcuts_layout.addWidget(self.shortcuts_check)
        # Add the horizontal layouts to the main vertical layout
        layout.addLayout(letters_layout)
        layout.addLayout(numbers_layout)
        layout.addLayout(symbols_layout)
        layout.addLayout(shift_layer_layout)
        layout.addLayout(shortcuts_layout)
        self.setLayout(layout)
        
        # Connect the clicked signal to a function that updates the properties of the key objects
        self.letters_check.clicked.connect(lambda: update_key_properties(key_objects, self.letters_check.isChecked(), self.shift_layer_check.isChecked(), self.symbols_check.isChecked(), self.numbers_check.isChecked(), self.shortcuts_check.isChecked()))
        self.numbers_check.clicked.connect(lambda: update_key_properties(key_objects, self.letters_check.isChecked(), self.shift_layer_check.isChecked(), self.symbols_check.isChecked(), self.numbers_check.isChecked(), self.shortcuts_check.isChecked()))
        self.symbols_check.clicked.connect(lambda: update_key_properties(key_objects, self.letters_check.isChecked(), self.shift_layer_check.isChecked(), self.symbols_check.isChecked(), self.numbers_check.isChecked(), self.shortcuts_check.isChecked()))
        self.shift_layer_check.clicked.connect(lambda: update_key_properties(key_objects, self.letters_check.isChecked(), self.shift_layer_check.isChecked(), self.symbols_check.isChecked(), self.numbers_check.isChecked(), self.shortcuts_check.isChecked()))
        self.shortcuts_check.clicked.connect(lambda: update_key_properties(key_objects, self.letters_check.isChecked(), self.shift_layer_check.isChecked(), self.symbols_check.isChecked(), self.numbers_check.isChecked(), self.shortcuts_check.isChecked()))
        
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
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
