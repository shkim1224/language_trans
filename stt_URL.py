import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search kunsan: search portal]')
    print('speak now')
    audio = r3.listen(source)

if 'kunsan' in r2.recognize_google(audio):
    url = 'https://www.kunsan.ac.kr/'
    with sr.Microphone() as source:
        print('search your query')
        audio = r2.listen(source)
        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

