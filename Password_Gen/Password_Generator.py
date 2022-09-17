# Main Libraries
import random
import PySimpleGUI as sg
from playsound import playsound
import numpy as np

#%% Total Characters List
c_list = []
for i in np.arange(0,1e+05):
    c_list.append(int(i))


#%% Classes and Functions
class PassGen:
    def __init__(self):

        #--- Layout object ---#
        sg.theme('Dark') #-> More themes in <https://www.geeksforgeeks.org/themes-in-pysimplegui/>

        playsound('piano_intro.wav',block=False) #-> internal music

        layout = [
            [sg.Text('E-mail/Username',size=(15,1),font=('Arial',10,'bold'),justification='left'),
            sg.Input(key='user_id',size=(15,1))], #-> user id field

            [sg.Text('Password',size=(15,1),font=('Arial',10,'bold'),justification='left'),
            sg.Input(key='pw',size=(15,1))],      #-> password field

            [sg.Text('New Password Total Chars'), sg.Combo(values=c_list,
            key='total_chars', default_value=1, size=(3, 1))],

            [sg.Output(size=(45,10))],            #-> window dimensions
            [sg.Button('Encrypt Password')]       #-> generates password
        ]

        #--- Window Object ---#
        self.window = sg.Window('password Generator', layout)

    def start(self):

        #--- Events Loop ---#
        while True:
            events,val = self.window.read() #-> reads the values entered by user
            if events == sg.WINDOW_CLOSED:  #-> breaks iteration if the window is closed (stops getting values)
                sg.popup('Please, checkout the generated log file')
                break
            if events == 'Encrypt Password':
                new_pw = self.generate_password(val)
                print('Original Password -> ', val['pw'])
                print('\nNew Password -> ', new_pw)
                self.save_pw(new_pw, val)

    def generate_password(self,val):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=int(val['total_chars']))
        new_pass = ''.join(chars)
        return new_pass


    def save_pw(self, new_pw, val):
        file_name = 'logfile.txt'
        with open(file_name,'a',newline='') as file:
            file.write(f"Email/Username: {val['user_id']}\nOriginal Password: {val['pw']}\nEncrypted Password: {new_pw}")
        
        print(f"\nFile '{file_name}' saved successfully")

#%% Functions Callback

gen = PassGen()
gen.start()