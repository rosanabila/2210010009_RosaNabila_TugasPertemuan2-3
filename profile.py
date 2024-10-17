import PySimpleGUI as sg

sg.theme_text_color('#66CDAA')
texts = [
    [sg.Text("SELAMAT DATANG DI KELAS 5O",font=("Arial",20,"italic","bold","underline"))],
    [sg.Text("NPM : 2210010009")],
    [sg.Text("Nama : Rosa Nabila")],
    [sg.Text("Kelas : TI 5O Reguler")],
    [sg.Text("Matkul : Pemrograman Visual 3")]
]

window = sg.Window(title='Latihan Pertama', layout=texts, size=(400, 200), font=("Times", 10))
window()
window.close()