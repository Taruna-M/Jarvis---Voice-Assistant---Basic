import speech_recognition as sr
import os
import subprocess
import re

r = sr.Recognizer()
mic = sr.Microphone()


def say(text):
    subprocess.call(['say', text])


path = '/Applications'
apps = os.listdir(path)
voice_commands = {}

for app in apps:
    voice_command = 'open ' + app.split('.app')[0]
    sys_command = 'open ' + path +'/%s' %app.replace(' ','\ ')
    voice_commands[voice_command] = sys_command
    
def search_voice_commands(query):
    query_re = re.compile(re.escape(query), re.IGNORECASE)
    for voice_command, sys_command in voice_commands.items():
        if query_re.search(voice_command):
            print(f"Jarvis: executing {sys_command}")
            return sys_command
    return None

def execute_command(query):
    print(f"User: {query}")
    if query.lower() == 'goodbye':
        say("Goodbye!")
        exit()
    else:
        try:
            sys_command = search_voice_commands(query)
            if sys_command:
                result = subprocess.run(sys_command, shell=True)
                if result.returncode != 0:
                    raise Exception(f"Error executing command: {sys_command}")
            else:
                raise Exception("No matching command found")
        except Exception as e:
            print(f"An error occurred: {e}")


def activate(phrase='jarvis'):
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                return True
            else:
                return False
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand your audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except sr.WaitTimeoutError:
        print("Waiting too long for speech input")
    except Exception as e:
        print("An error occurred: {0}".format(e))

while True:
    try:
        if activate():
            prompt = "What can I do for you?"
            say(prompt)
            print(f"Jarvis: {prompt}\n")
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                transcript = r.recognize_google(audio)
                execute_command(transcript)
    except Exception as e:
        print(f"Error: {e}")
