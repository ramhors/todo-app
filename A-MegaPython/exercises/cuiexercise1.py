import PySimpleGUI as gu

label1 = gu.Text("Enter feet: ")
input1 = gu.Input()

label2 = gu.Text("Enter inches:  ")
input2 = gu.Input()

button1 = gu.Button("Convert")

window = gu.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [button1]])

window.read()
window.close()
