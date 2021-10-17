import ssl
import urllib
import json
import os
try:
    from IPython.core.display import display, HTML
except:
    os.system('pip install IPython')


ssl._create_default_https_context = ssl._create_unverified_context


class Dictonary:
    '''Pass the word inside the Dictonary and get the meaning along with example and audio pronaunciation
    Dictonary('happy')
    '>>> ------------------------------------'
    ''>>> meaning: inclined to use a specified thing excessively or at random.'
    '>>> ------------------------------------'
    '>>> example: they tended to be grenade-happy'
    '''

    def __init__(self, word):
        self.word = word
        BASE_URL = 'http://api.dictionaryapi.dev/api/v2/entries/en_US/'
        self.url = BASE_URL + word

        try:
            response = json.load(urllib.request.urlopen(self.url))
            response = response[-1]
        except Exception as e:
            print(e)

        try:
            self.phonetic = response['phonetic']
        except:
            self.phonetic = 'None'
        try:
            self.origin = response['origin']
        except:
            self.origin = 'None'
        try:
            self.meaning = response['meanings'][-1]['definitions'][-1]['definition']
        except:
            self.meaning = 'None'
        try:
            self.example = response['meanings'][-1]['definitions'][-1]['example']
        except:
            self.example = 'None'
        try:
            self.audio_url = 'https:' + response['phonetics'][-1]['audio']
        except:
            self.audio_url = 'None'

        print('------------------------------------')
        print(f'meaning: {self.meaning}')
        print('------------------------------------')
        print(f'example: {self.example}')
        try:
            self.show_audio_with_controls()
        except:
            pass
        print('-------- Use class instance for more methods like word origin, phonetic, etc. --------')
        print('-------- Please close the instance after-use to delete saved mp3 file ---------')

    def show_audio_with_controls(self):
        urllib.request.urlretrieve(self.audio_url, f'{self.word}.mp3')
        display(HTML("<audio controls><source src={}.mp3 type='audio/mpeg'></audio>".format(self.word)))

    def close(self):

        mp3_file = f'{self.word}.mp3'

        try:
            os.remove(mp3_file)
        except OSError as e:
            pass

    @staticmethod
    def credit():
        print('--------------------------------------------------')
        print('| Created on: 16th October 2021 by Aditya Rajgor |')
        print('| Inspired from: @rahulnegi20 github repository  |')
        print('| Author: Aditya Rajgor                          |')
        print('| Open for contribution                          |')
        print('--------------------------------------------------')

        pass

