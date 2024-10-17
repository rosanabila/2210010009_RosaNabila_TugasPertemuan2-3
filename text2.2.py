import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
Window = sg.Window(title="profile",
                   layout=[[sg.Text("TEKNOLOGI INFORMASI",size=(25,1),justification="center")],
                           [sg.Text("TEKNOLOGI INFORMASI",size=(25,1),justification="left")]
                           [sg.Text("TEKNOLOGI INFORMASI",size=(25,1),justification="right")],
                           [sg.Text("TEKNOLOGI INFORMASI"+" ",size=(25,1),justification="center")],
                           [sg.Text("UNISKA MAB BANAJARMASIN", text_color="#FFCC00")]],
                           size=(400,250),
                           font=("Times", 18))
Window()
Window.close()