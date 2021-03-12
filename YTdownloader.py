import PySimpleGUI as sg
import pytube


class TelaPython:
    def __init__(self):
        # Layout
        sg.theme('DarkBlack1')   # Add a touch of color
        layout = [
            [sg.Image(r'C:\Users\milla\Pictures\youtube.png', size=(500,60))],
            [sg.Text('Link do video:',size=(50, 1), justification='center', font=("Calibri",15))],
            [sg.Input(size=(73,1),key='link')],
            [sg.Text('Somente audio?',size=(31,1), justification='right', font=("Calibri",13)),
            sg.Radio('Sim','formato',key='audio', font=("Calibri",13))],
            [sg.Text()],
            [sg.Text(size=(13,1)), 
            sg.Button('Download',tooltip='Click to download',size=(15, 1), font=("Calibri",12)), 
            sg.Button('Cancel',size=(15, 1),font=("Calibri",12))]
        ]

        # Janela
        self.janela = sg.Window("YouTube Downloader").layout(layout) # adicionei o self

    def Iniciar(self):

        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            link = self.values['link']   # Aqui vai as keys
            audio = self.values['audio'] 

            if self.button == sg.WIN_CLOSED or self.button == 'Cancel': # if user closes window or clicks cancel
                break
            
            if self.button == 'Download':
                if audio:
                    youtube = pytube.YouTube(link)
                    video = youtube.streams.get_audio_only()
                    video.download()

                else:
                    youtube = pytube.YouTube(link)
                    video = youtube.streams.get_highest_resolution()
                    video.download()

            sg.popup('Download completo!')

tela = TelaPython()
tela.Iniciar()
