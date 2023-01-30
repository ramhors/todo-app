import PySimpleGUI as ps
from converter import convert

label1 = ps.Text("Enter feet: ")
input1 = ps.Input(key='feet')
label2 = ps.Text("Enter inches: ")
input2 = ps.Input(key='inches')
convertBtn = ps.Button("Convert")
output_label = ps.Text("", key="output")

window = ps.Window("Conversion", layout=[[label1, input1],
                                         [label2, input2],
                                         [convertBtn, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()