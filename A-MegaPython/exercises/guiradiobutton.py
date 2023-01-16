import PySimpleGUI as gs

label = gs.Text("What are dolphins?")
option1 = gs.Radio("Amphibians", group_id="question1")
option2 = gs.Radio("Fish", group_id="question1")
option3 = gs.Radio("Mamals", group_id="question1")
option4 = gs.Radio("Birds", group_id="question1")

window = gs.Window("File Compressor",
                   layout=[[label],
                           [option1],
                           [option2],
                           [option3],
                           [option4]])

window.read()
window.close()