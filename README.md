# 🧮 Python Calculator App

A simple and flexible calculator built with Python.  
This project demonstrates the use of *args for handling multiple arguments and function-based operations such as *addition, subtraction, multiplication, and division*.

---

## 🚀 Features

- Perform basic arithmetic operations:
  - ➕ Addition  
  - ➖ Subtraction  
  - ✖ Multiplication  
  - ➗ Division  
- Uses *args to accept multiple numeric inputs.  
- Beginner-friendly and well-commented code.  
- Easily extendable — you can add more operations like modulus, exponentiation, etc.

---

## 🧩 Code Overview

```python
def calculator(operation, *args):
    if not args:
        print('No digits provided')
    if operation == 'add':
        result = sum(args)
    elif operation == 'subtract':
        result = args[0]
        for number in args[1:]:
            result -= number
    elif operation == 'multiply':
        result = 1
        for number in args:
            result *= number
    elif operation == 'divide':
        result = args[0]
        for number in args[1:]:
            result /= number
    return result


# 🧠 Example Usage

print(calculator('add', 2, 4, 6))        # ➜ 12
print(calculator('subtract', 10, 3, 2))  # ➜ 5
print(calculator('multiply', 2, 4, 4))   # ➜ 32
print(calculator('divide', 16, 4, 2))    # ➜ 2



⚙️ How to Run

Clone this repository:

git clone https://github.com/0sinach1/calculator_python.git


Move into the project directory:

cd calculator_python


Run the script:

python scripts.py





📚 Concepts Used

Functions and Parameters

*args (Variable-length arguments)

Conditional logic (if, elif, else)

Loops (for loops for iteration)

##💡 Future Improvements

Add input validation.

Create a command-line interface (CLI) version.

Build a GUI version using tkinter or PyQt.

Extend with scientific operations (square root, power, etc).

👨‍💻 Author

Ifeanyi Elvis Osinachi
📍 Student & Data Enthusiast
💼 GitHub