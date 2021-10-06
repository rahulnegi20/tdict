# Terminal Google Dictionary (online)

### Too Geeky(Lazy) to go (google/bing) meaning of the word?

Well, then this is the perfect script for you!

## Example

![t-dict](https://user-images.githubusercontent.com/48027382/136056588-3b66d661-7f1e-40c6-b018-a0c6d2bd2f81.png)

### Basic Requirements

* python3
* urllib
* yachalks


# How to use?

## For Windows

#### 1.) clone the repo

git clone https://github.com/SineshX/tdict.git
#### 2.) copy the path of project sub folder (dict)

![image](https://user-images.githubusercontent.com/48027382/136045502-7865539d-9543-4457-adb2-b3de76a1517c.png)

##### paste in path environment variable (see step 3 image)

##### paste in path of file (dict.py) in tdict.bat

![image](https://user-images.githubusercontent.com/48027382/136050307-8f4c3df2-0863-4eb5-9fd8-659a11e6ddb7.png)

#### 3.) Edit environment variable

##### add python in environment variable (hope already added)

##### add project folder in environment variable

![image](https://user-images.githubusercontent.com/48027382/136043016-6d7c4e01-d1df-4b2e-8c62-cad3f16e3215.png)

#### 4.) check with command  (in cmd)

```where.exe tdict```

> D:\Sinesh\Project\tdict\dict\tdict.bat

#### 5.) Run the script anywhere from the terminal by just calling tdict

##### it can take word as commandline argumrnt

![image](https://user-images.githubusercontent.com/48027382/136046030-b3c71b00-00be-4a26-80db-538a4db97502.png)

##### if commandline argument is not given it will ask user for word to be searched

![image](https://user-images.githubusercontent.com/48027382/136046407-1aec9c88-82d7-49ca-a801-868363f1c0b7.png)

###### explore other features :)


# For Linux

#### In order to run the script from terminal (anylocation)

> you need to provide path to tdict in your .bashrc file which is hidden by default, (Ctrl + H) to unhide the hidden files or vice-versa. now you need to edit that .bashrc file using any text editor and add this line on top

`PATH="$PATH:<path-to-dict-folder>"`
for example , in my case it is <br>
(/home/rahulnegi/projects/scripts/dict).

## Development

This script uses unofficial Google-Dictionary api (https://github.com/meetDeveloper/googleDictionaryAPI)

## Open for improvements/contributions!, issues and feature requests!

# Hacktoberfest2021

## I could use some help over :

- Better Text Formatting and design of the output. [here](https://github.com/rahulnegi20/tdict/issues/1)
- Add multi threading for synonyms and example

Thanks : )
