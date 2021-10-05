# Terminal Google Dictionary (online)

### Too Geeky(Lazy) to go (google/bing) meaning of the word?

Well, then this is the perfect script for you!

## Example

![t-dict](https://user-images.githubusercontent.com/36270407/128837743-5c76d4fd-a3eb-4cc4-95ab-6f7dab7c2415.png)

## How to use?

Download or clone this repository (https://github.com/rahulnegi20/tdict.git)
and then check requirements.txt i have mentioned the procedure with steps.

Just type the word and get the meaning of the word in your terminal.
you can search for synonyms and example too!

### Basic Requirements

* python3

### For Linux

#### In order to run the script from terminal (anylocation)

> you need to provide path to tdict in your .bashrc file which is hidden by default, (Ctrl + H) to unhide the hidden files or vice-versa. now you need to edit that .bashrc file using any text editor and add this line on top

`PATH="$PATH:<path-to-dict-folder>"`
for example , in my case it is <br>
(/home/rahulnegi/projects/scripts/dict).

### For Windows

1.) Go to windows branch ,and clone the repo

 <image >

2.) Edit environment variable
    - add python in environment variable (hope already added)
    - add project folder in environment variable
      <image >
    - check with command  (in cmd)
``` where.exe tdict ```
> D:\Sinesh\Project\tdict\dict\tdict.bat


 3.) Run the script anywhere from the terminal by just calling tdict
    - it can take word as commandline argumrnt 
    <image >
    - if commandline argument is not given it will ask user for word to be searched 
    <image >


## Development

This script uses unofficial Google-Dictionary api (https://github.com/meetDeveloper/googleDictionaryAPI)

## Open for improvements/contributions!, issues and feature requests!

# Hacktoberfest2021

## I could use some help over :

- Better Text Formatting and design of the output. [here](https://github.com/rahulnegi20/tdict/issues/1)
- Add multi threading for synonyms and example 

Thanks : )
