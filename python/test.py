# Import the necessary modules from PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPalette, QColor

# Create a subclass of the QWidget class
class MyWidget(QWidget):
    def __init__(self):
        # Initialize the widget and set its properties
        super().__init__()
        self.setWindowTitle("My Widget")
        self.resize(400, 300)

        # Set the widget's palette to a charcoal grey and deeper blue color scheme
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#2C2F33"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#D6D8DC"))
        palette.setColor(QPalette.ColorRole.Button, QColor("#373940"))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor("#D6D8DC"))
        self.setPalette(palette)

        # Create a button on the widget
        button = QPushButton("Click me", self)
        button.resize(100, 50)
        button.move(150, 100)

        # Set the color of the button text to white
        button.setForegroundRole(QPalette.ColorRole.ButtonText)

        # Connect the button's clicked signal to a callback function
        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        # Print a message when the button is clicked
        print("Button was clicked")

# Create an instance of the QApplication class
app = QApplication([])

# Create an instance of the MyWidget class
widget = MyWidget()

# Show the widget on the screen
widget.show()

# Start the event loop
app.exec_()
