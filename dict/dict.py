 
import os
import sys
import urllib.request, urllib.parse, urllib.error
import json	 
print('++++++++++Terminal Based google-dictionary++++++++++\n')
title = input("Enter word to search: ")
flag = 0
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\START\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n')
print ("Word: ",title )

try :
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+title
    result = json.load(urllib.request.urlopen(url)) 
except :
    print('Connect to Internet!!', sys.exc_info()[0])
    os._exit(0)

def get_meaning(title):
    try :
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+title
        result = json.load(urllib.request.urlopen(url)) 
    except urllib.error.HTTPError as e: ResponseData = 'failed'
    except :
        print('Connect to Internet!!', sys.exc_info()[0])
        os._exit(0)
    try :

        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ MEANING of {} \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'.format(title))
        print(result[0]["meanings"][0]["definitions"][0]["definition"])
        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\END\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
    
    except :
        print('!!Error!! Please Check the Spelling!', sys.exc_info()[0])
        os._exit(0)

    return    
def get_synonyms(title):
    try :
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+title
        result = json.load(urllib.request.urlopen(url)) 
    except urllib.error.HTTPError as e: ResponseData = 'failed'
    except  :
        print('Connect to Internet!!', sys.exc_info()[0])
        os._exit(0)
    try :

        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ SYNONYMS of {} \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'.format(title))
        for x in range(3): 
            print(result[0]["meanings"][0]["definitions"][0]["synonyms"][x])

    except :
        print('!!Error!! ', sys.exc_info()[0])
        os._exit(0)

    return
def get_example(title):
    try :
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+title
        result = json.load(urllib.request.urlopen(url)) 
    except urllib.error.HTTPError as e: ResponseData = 'failed'
    except :
        print('Connect to Internet!!', sys.exc_info()[0])
        os._exit(0)
    try:

        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ EXAMPLE of {} \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'.format(title))
        print(result[0]["meanings"][0]["definitions"][0]["example"])    

    except :
        print('!!Error!! ', sys.exc_info()[0])
        os._exit(0)
    return

get_meaning(title)

while flag == 0:
    print('\n-----------------------------------')
    print(' ``Press 1 to get synonyms`` ')
    print(' ``Press 2 to get an example `` ')
    print(' ``Press 0 to search new word')
    print(' ``Press 9 to quit ``')
    print('-----------------------------------')
    try :
        char = int(input())
        if char == 1:
            get_synonyms(title)
        elif char == 2:
            get_example(title)    
        elif char == 0:
            title = input('Enter word to search :')    
            get_meaning(title)
            flag = 0
        elif char== 9 :
            print('See you soon!')
            flag = 1   
        else:
            print('Wrong key pressed')  
    except :
        print('INCORRECT KEY', sys.exc_info()[0]) 
        pass         
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\END\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n')   