#NAME:K.SUJITHSAI
#USN:25BTRAD047
#COURSE:PYTHON
#BRANCH:CSE_AIDE_A
#DATE:31-07-2026
 Installing Python, Setting up VS Code / PyCharm, Jupyter Notebook
Installing Python and Setting Up VS Code (Simple)
Step 1: Install Python
1.	Go to Python Downloads.
2.	Download the latest Python version.
3.	Open the installer.
4.	Tick ✅ Add Python to PATH.
5.	Click Install Now.
6.	After installation, click Close.
Step 2: Check Python
1.	Open Command Prompt.
2.	Type:
3.	python --version
4.	If you see the Python version, it is installed successfully.
Step 3: Install VS Code
1.	Go to Visual Studio Code.
2.	Download and install VS Code.
3.	Open VS Code.
Step 4: Install Python Extension
1.	Click the Extensions icon.
2.	Search for Python.
3.	Install the Python extension by Microsoft.
Step 5: Write Your First Program
1.	Create a new file and save it as hello.py.
2.	Type:
3.	print("Hello, World!")
Step 6: Run the Program
•	Click the Run (▶) button or open the terminal and type:
•	python hello.py
Output:
Hello, World!






2: Write and execute a basic Python program.
print("hello world")
print("i am sujith royal")
output:
 





3: Programs using variables, operators, and input/output.
a = int(input("enter a number"))
b = int (input("enter another number"))
c = a+b
d = a*b
print(c)
print(d)
output:
 






4: Simple calculator and area calculation programs.
s = int(input("side of a sqaure"))
area = s * s
print("area of square:",area)


a = int(input("enter a number"))
b = int (input("enter another number"))
c = input("enter the operation u want to performe")
if c == "add":
    print (a + b)
if c == "sub" :
    print (a - b)
elif c == "mul":
    print (a * b)
else :
    print (a / b)
