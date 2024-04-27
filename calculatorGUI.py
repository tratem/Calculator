#iphone calculator GUI
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from calculator_source import CalculatorOperations as CO

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()    
        self.setWindowTitle("iPhone Calculator")
        self.setGeometry(50, 50, 320, 520)        
        self.setupUi()

    def setupUi(self):
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: black;")
        self.setCentralWidget(central_widget)

        calculator_layout = QVBoxLayout()
        main_layout = QHBoxLayout()
        numbers_layout = QVBoxLayout()
        operations_layout = QVBoxLayout()

        first_row_layout = QHBoxLayout()
        fifth_row_layout = QHBoxLayout()

        self.current_calculations = QLineEdit()
        self.current_calculations.setFixedHeight(80)
        self.current_calculations.setStyleSheet("background-color: black; color: white; font: bold 60px;")
        calculator_layout.addWidget(self.current_calculations)

        first_row_list = ["AC", "neg", "%"]
        for j in first_row_list:
            button = self.create_button(j)
            button.setStyleSheet("border-radius: 40px; background-color: #D3D3D3; color: white; font: bold 22px;")
            button.clicked.connect(self.handle_button_click)
            first_row_layout.addWidget(button)

        numbers_layout.addLayout(first_row_layout)

        for i in range(3):
            numbers_row_layout = QHBoxLayout()
            for j in range(7, 10):
                button = self.create_button(str(j - 3 * i))
                button.clicked.connect(self.handle_button_click)
                numbers_row_layout.addWidget(button)
            numbers_layout.addLayout(numbers_row_layout)

        zero_button = self.create_button("0")
        zero_button.setFixedWidth(170)
        zero_button.clicked.connect(self.handle_button_click)
        comma_button = self.create_button(",")
        comma_button.clicked.connect(self.handle_button_click)

        fifth_row_layout.addWidget(zero_button)
        fifth_row_layout.addWidget(comma_button)

        numbers_layout.addLayout(fifth_row_layout)

        operations_list = ["/", "x", "-", "+", "="]

        for operation in operations_list:
            button = self.create_button(operation)
            button.setStyleSheet("border-radius: 40px; background-color: orange; color: white; font: bold 22px;")
            button.clicked.connect(self.handle_button_click)
            operations_layout.addWidget(button)

        main_layout.addLayout(numbers_layout)
        main_layout.addLayout(operations_layout)
        calculator_layout.addLayout(main_layout)
        central_widget.setLayout(calculator_layout)

    def create_button(self, button_label):
        button = QPushButton(f"{button_label}")
        button.setFixedWidth(80)
        button.setFixedHeight(80)
        button.setStyleSheet("border-radius: 40px; background-color: gray; color: white; font: bold 22px;")
        return button
    
    def handle_button_click(self):
        button = self.sender()
        current_text = self.current_calculations.text()
        button_text = button.text()

        if button_text == "AC":
            self.current_calculations.clear()
        elif button_text == "=":
            self.handle_operations()
        else:
            if button_text == "neg" and current_text:
                if current_text.startswith('-'):
                    self.current_calculations.setText(current_text[1:])
                else:
                    self.current_calculations.setText('-' + current_text)
            else:
                self.current_calculations.setText(current_text + button_text)

    def handle_operations(self):
        current_text = self.current_calculations.text()
        second_number = False
        x = 0
        y = 0
        operation = "+"
        for value in current_text: 
            if value.isdigit() and second_number == False:
                x = x * 10 + int(value)
            elif value.isdigit() and second_number == True:
                y = y * 10 + int(value)
            elif value in ["/", "x", "-", "+"]:
                operation = value
                second_number = True
        if ("%" in current_text):
            self.current_calculations.setText(str(CO.percentile(x, y, operation)))
        elif operation == "+":
            self.current_calculations.setText(str(CO.addition(x, y)))
        elif operation == "-":
            self.current_calculations.setText(str(CO.subtraction(x, y)))
        elif operation == "*" or operation == "x":
            self.current_calculations.setText(str(CO.multiplication(x, y)))
        elif operation == "/":
            self.current_calculations.setText(str(CO.division(x, y)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())