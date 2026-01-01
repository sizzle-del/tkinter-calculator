🧮 Calculator App (Python Tkinter)

A simple GUI-based calculator application built using Python and Tkinter.
This calculator supports basic arithmetic operations like addition, subtraction, multiplication, and division, along with error handling for invalid expressions and division by zero.

📌 Features

Graphical User Interface using Tkinter
Supports:

Addition (+)
Subtraction (−)
Multiplication (×)
Division (÷)
Clear (C) button to reset the input

Real-time display of input and results
Error handling using message boxes:
Division by zero
Invalid expressions

🛠️ Technologies Used

Python 3
Tkinter (Python standard GUI library)

📂 Project Structure
calculator/
│
├── calculator.py   # Main Python file
├── README.md       # Project documentation

▶️ How to Run the Project

Make sure Python 3 is installed on your system
Check by running:

python --version

Clone this repository:
git clone https://github.com/siz-del/tkinter-calculator.git

Navigate to the project folder:
cd calculator-tkinter

Run the application:
python calculator.py

🖥️ Application Preview

The calculator window includes:
A display screen at the top
Number buttons (0–9)
Operator buttons (+, −, ×, ÷)

Clear (C) and Equals (=) buttons

⚠️ Error Handling

Division by Zero
Displays an error message using messagebox.showerror()

Invalid Expression
Handles incorrect input safely without crashing the program

📘 Concepts Used

Tkinter widgets (Tk, Label, Button, Frame)
StringVar for dynamic display updates
Event handling using button callbacks
Global variables
Python eval() for expression evaluation
Exception handling (try, except)

🚀 Future Improvements (Optional)

Add decimal point support
Add keyboard input support
Improve UI styling
Replace eval() with a safer expression parser
Add scientific calculator functions

👨‍💻 Author

Akshat Sharma
BCA Student
📌 Learning Python, GUI Development & Software Fundamentals

📄 License
This project is for educational purposes and is free to use or modify.
