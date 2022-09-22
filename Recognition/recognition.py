import speech_recognition as sr

r = sr.Recognizer()

# r.recognize_google()

word = sr.AudioFile(r'C:\Users\Hugo\speechRecognition\voiceRecording\recording1.wav')
with word as source:
    audio = r.record(source)

type(audio)

def reader():
    rec = r.recognize_google(audio)
    return rec

rec = r.recognize_google(audio)


# print(r.recognize_google(audio))