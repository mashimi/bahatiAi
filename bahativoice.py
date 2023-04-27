
import speech_recognition as sr
import pyttsx3
import openai
from elevenlabslib import ElevenLabsUser
from elevenlabslib import *

openai.api_key = "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"

engine = pyttsx3.init()
rate = engine.getProperty("rate")
voices = engine.getProperty('voices')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "Mashimi"
bot_name = "Bella"

while True:
    with mic as source:
        print("\n Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    print("no longer listening")

    try:
        user_input = r.recognize_google(audio, language="german")
    except:
        continue

    prompt = user_name+":"+user_input + "\n"+bot_name+":"
    conversation += prompt
    prompt = "Discuss about africa"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(
        user_name + ":", 1)[0].split(bot_name + ":", 1)[0]

    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()
