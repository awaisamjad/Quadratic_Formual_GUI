import PySimpleGUI as sg
import math 
sg.theme('DarkTeal')
width = 300
height = width * 9/16
layout=[
    [sg.Text("Enter value for a:"), sg.Input(key='INPUT_A')],
    [sg.Text("Enter value for b:"), sg.Input(key='INPUT_B')],
    [sg.Text("Enter value for c:"), sg.Input(key='INPUT_C')],
    [sg.Button("Calculate")],
    [sg.Text("", size=(0, 1), key='ROOT1')],
    [sg.Text("", size=(0, 1), key='ROOT2')],
    [sg.Button("Exit")]
]

margins=(width, height)
window = sg.Window(title="Quadratic Equation Solver",layout = layout, margins = margins)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Calculate":
        a = int(values["INPUT_A"])
        b = int(values["INPUT_B"])
        c = int(values["INPUT_C"])
        discriminant = b * b - 4 * a * c 
        sqrt_val = math.sqrt(abs(discriminant)) 
        
        if discriminant > 0: 
            root1 = ((-b + sqrt_val)/(2 * a)) 
            root2 = ((-b - sqrt_val)/(2 * a)) 
            window["ROOT1"].update(value = f"Root 1: {root1}")
            window["ROOT2"].update(value = f"Root 2: {root2}")
        
        elif discriminant == 0:  
            result = -b / (2 * a)
            window["ROOT1"].update(value = result) 

        else: 
            root1 = (- b / (2 * a), " + i", sqrt_val)
            root2 = (- b / (2 * a), " + i", sqrt_val)
            window["ROOT1"].update(value = f"Root 1: {root1}")
            window["ROOT2"].update(value = f"Root 2: {root2}")

window.close()

