import os
import sys
import urllib.request, urllib.parse, urllib.error
import json
# for colors 
from yachalk import chalk


# flex XD
print(chalk.blue("_"*6+ "Terminal Based Dictionary"+"_"*6),end="\n"*2)

# taking word from user / commandline 
if len(sys.argv) != 2:
    # sys.exit(1)
    title = input(chalk.blue("\nPlease input word to search : "))
else:
    title = sys.argv[1]


# API stuff

# **************  get_Meaning   ************* #

def get_meaning(title):
    
    print(chalk.blue("Searching for : "+ chalk.white.bold(title)))
    print(chalk.magenta.dim("_"*36))
    try :
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+title
        result = json.load(urllib.request.urlopen(url)) 
    except urllib.error.HTTPError as e: ResponseData = 'failed'
    except :
        print(chalk.red('Please Connect to Internet!! and try again :)'), sys.exc_info()[0])
        os._exit(0)
    try :
        print(chalk.green_bright("\nMEANING : "),end="")

        print(chalk.cyan(result[0]["meanings"][0]["definitions"][0]["definition"]))
    
    except :
        print(chalk.red(f'\n!!Error!! Please Check the Spelling! : {title}'), sys.exc_info()[0])
        os._exit(0)

    return    


# **************  get_Synonyms   ************* #

def get_synonyms(title):
    try :
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+title
        result = json.load(urllib.request.urlopen(url)) 
    except urllib.error.HTTPError as e: ResponseData = 'failed'
    except  :
        print('Please Connect to Internet!! and try again :)', sys.exc_info()[0])
        os._exit(0)
    try :

        print(chalk.magenta(f"SYNONYMS of {title} : "),end="")
        for x in range(3): 
            print(chalk.cyan(result[0]["meanings"][0]["definitions"][0]["synonyms"][x]))

    except :
        print('!!Error!! ', sys.exc_info()[0])
        os._exit(0)

    return


# **************  get_Example   ************* #

def get_example(title):
    try :
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+title
        result = json.load(urllib.request.urlopen(url)) 
    except urllib.error.HTTPError as e: ResponseData = 'failed'
    except :
        print('Please Connect to Internet!! and try again :)', sys.exc_info()[0])
        os._exit(0)
    try:
        print(chalk.magenta(f"Example of {title} : "),end="")
        print(chalk.cyan(result[0]["meanings"][0]["definitions"][0]["example"]))    

    except :
        print('!!Error!! ', sys.exc_info()[0])
        os._exit(0)
    return



# *******************Main*********************** #

flag = 0

get_meaning(title)

while flag == 0:
    print()
    print( chalk.italic.magenta.dim("_"*8 + "Wanna Search more ?"+ "_"*8))
    print()
    print(chalk.blue.dim(f'# Press 1 to get synonyms of {title} \
            \n# Press 2 to get an example of {title} \
            \n# Press 3 to search another Word! '))
    # print(' ``Press 4 to get an antonyms (opposite words)`` ')
    print(chalk.yellow(' ``Press 0 to quit``'))
    print()
    print(chalk.underline.magenta.dim('Please choose your option :'),end=" ")
    try :
        char = int(input())
        if char== 0 :
            flag = 1
            break   
        elif char == 1:
            get_synonyms(title)
        elif char == 2:
            get_example(title)    
        elif char == 3:
            title = input(chalk.blue("\nPlease input word to search : "))
            get_meaning(title)   
        else:
            print('Wrong key pressed')  
    except :
        print('INCORRECT KEY', sys.exc_info()[0]) 

# End of program 
print(f'     {chalk.dim("See you soon ,By :)")}',end = "\n\n")



# extras
# colors ref : https://github.com/bluenote10/yachalk/blob/master/yachalk/chalk_factory.py
# whole code ref : https://github.com/rahulnegi20/tdict/blob/main/dict/dict.py