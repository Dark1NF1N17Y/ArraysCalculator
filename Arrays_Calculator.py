#Pre Settings
import tkinter
from tkinter import messagebox
import numpy
arr1 , arr2 = numpy.empty((2,2)) , numpy.empty((2,2))
calculator_window = tkinter.Tk()
calculator_window.title("Arrays Calculator")

#Operations
def array2x2_add():
    #Array1 Sort
    arr1[0,0] , arr1[0,1] = array1_entry11.get() , array1_entry12.get()
    arr1[1,0] , arr1[1,1] = array1_entry21.get() , array1_entry22.get()
    #Array 2 Sort
    arr2[0,0] , arr2[0,1] = array2_entry11.get() , array2_entry12.get()
    arr2[1,0] , arr2[1,1] = array2_entry21.get() , array2_entry22.get()
    #Operation && Print
    arr3 = numpy.add(arr1,arr2)
    messagebox.showinfo("Result" , f"{arr3[0,0] , arr3[0,1]}\n{arr3[1,0] , arr3[1,1]}")

def array2x2_subtract():
    #Array1 Sort
    arr1[0,0] , arr1[0,1] = array1_entry11.get() , array1_entry12.get()
    arr1[1,0] , arr1[1,1] = array1_entry21.get() , array1_entry22.get()
    #Array 2 Sort
    arr2[0,0] , arr2[0,1] = array2_entry11.get() , array2_entry12.get()
    arr2[1,0] , arr2[1,1] = array2_entry21.get() , array2_entry22.get()
    #Operation && Print
    arr3 = numpy.subtract(arr1,arr2)
    messagebox.showinfo("Result" , f"{arr3[0,0] , arr3[0,1]}\n{arr3[1,0] , arr3[1,1]}")

def array2x2_multiply():
    #Array1 Sort
    arr1[0,0] , arr1[0,1] = array1_entry11.get() , array1_entry12.get()
    arr1[1,0] , arr1[1,1] = array1_entry21.get() , array1_entry22.get()
    #Array 2 Sort
    arr2[0,0] , arr2[0,1] = array2_entry11.get() , array2_entry12.get()
    arr2[1,0] , arr2[1,1] = array2_entry21.get() , array2_entry22.get()
    #Operation && Print
    arr3 = numpy.empty((2,2))
    arr3[0,0] = (arr1[0,0]*arr2[0,0])+(arr1[0,1]*arr2[1,0])
    arr3[0,1] = (arr1[0,0]*arr2[0,1])+(arr1[0,1]*arr2[1,1])
    arr3[1,0] = (arr1[1,0]*arr2[0,0])+(arr1[1,1]*arr2[1,0])
    arr3[1,1] = (arr1[1,0]*arr2[0,1])+(arr1[1,1]*arr2[1,1])
    messagebox.showinfo("Result" , f"{arr3[0,0] , arr3[0,1]}\n{arr3[1,0] , arr3[1,1]}")

def array2x2_inverse():
    #Array1 Sort
    arr1[0,0] , arr1[0,1] = array1_entry11.get() , array1_entry12.get()
    arr1[1,0] , arr1[1,1] = array1_entry21.get() , array1_entry22.get()
    #Array 2 Sort
    arr2[0,0] , arr2[0,1] = 0 , 0
    arr2[1,0] , arr2[1,1] = 0 , 0
    #Operation && Print
    arr3 = numpy.empty((2,2))
    if ((arr1[0,0]*arr1[1,1])-(arr1[1,0]*arr1[0,1])) == 0 :
        messagebox.showinfo("Error" , f"Array Can't Be Inversed")
        return
    arr3[0,0] = (1/((arr1[0,0]*arr1[1,1])-(arr1[1,0]*arr1[0,1])))*(arr1[1,1])
    arr3[0,1] = (1/((arr1[0,0]*arr1[1,1])-(arr1[1,0]*arr1[0,1])))*(0-arr1[0,1])
    arr3[1,0] = (1/((arr1[0,0]*arr1[1,1])-(arr1[1,0]*arr1[0,1])))*(0-arr1[1,0])
    arr3[1,1] = (1/((arr1[0,0]*arr1[1,1])-(arr1[1,0]*arr1[0,1])))*(arr1[0,0])
    messagebox.showinfo("Result" , f"{arr3[0,0] , arr3[0,1]}\n{arr3[1,0] , arr3[1,1]}")

def operation():
    if operation_entry.get() == "+":
        array2x2_add()
    elif operation_entry.get() == "-":
        array2x2_subtract()
    elif operation_entry.get() == "*":
        array2x2_multiply()
    elif operation_entry.get() == "/":
        array2x2_inverse()
    else:
       messagebox.showinfo("Error" , f"Operation {operation_entry.get()} Not Defined!") 

#Array1 Input Display
array1_frame = tkinter.Frame(calculator_window, bg='lightgray', padx=20, pady=20)
array1_frame.pack(side=tkinter.LEFT , fill=tkinter.Y, padx=(10 , 5))
array1_text = tkinter.Label(array1_frame, text="Array 1").pack()
array1_entry11 = tkinter.Entry(array1_frame , justify='center')
array1_entry11.pack(pady=(7 , 7))
array1_entry12 = tkinter.Entry(array1_frame , justify='center')
array1_entry12.pack(pady=(7 , 7))
array1_entry21 = tkinter.Entry(array1_frame , justify='center')
array1_entry21.pack(pady=(7 , 7))
array1_entry22 = tkinter.Entry(array1_frame , justify='center')
array1_entry22.pack(pady=(7 , 7))

#Operation Input Display
operation_frame = tkinter.Frame(calculator_window, bg='lightgray' , padx=20 , pady=20)
operation_frame.pack(side=tkinter.LEFT, fill=tkinter.X , expand=True , padx=(10, 5))
operation_text = tkinter.Label(operation_frame , text="Operation (+ , - , * , /)")
operation_text.pack(pady=(7 , 7))
operation_entry = tkinter.Entry(operation_frame , justify='center')
operation_entry.pack(pady=(7 , 7))

#Array2 Input Display
array2_frame = tkinter.Frame(calculator_window , bg='lightgray' , padx=20 , pady=20)
array2_frame.pack(side=tkinter.RIGHT , fill=tkinter.Y , padx=(10 , 5))
array2_text = tkinter.Label(array2_frame , text="Array 2")
array2_text.pack(pady=(7 , 7))
array2_entry11 = tkinter.Entry(array2_frame , justify='center')
array2_entry11.pack(pady=(7 , 7))
array2_entry12 = tkinter.Entry(array2_frame , justify='center')
array2_entry12.pack(pady=(7 , 7))
array2_entry21 = tkinter.Entry(array2_frame , justify='center')
array2_entry21.pack(pady=(7 , 7))
array2_entry22 = tkinter.Entry(array2_frame , justify='center')
array2_entry22.pack(side=tkinter.RIGHT , pady=(7 , 7))

#Calculator Window
resultbutton = tkinter.Button(operation_frame, text="Result" , command=operation).pack()
calculator_window.mainloop()
