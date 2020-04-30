# -*- coding: utf-8 -*-


import speech_recognition as sr

#obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("say something")
        audio = r.listen(source)
        print('got it!Now to recognize it....')
        #recognize speech  using google
        try:
            print("You said\n"+r.recognize_google(audio))
            print("\nAudio successfully recorded! check the directory")
        
        except Exception as e:
            print(e)
            
        #code of wav file
        with open("microphone.results.wav","wb") as f:
            f.write(audio.get_wav_data())
            
        with open("microphone.results.aiff","wb") as f:
            f.write(audio.get_aiff_data())
            
        with open("microphone.results.flac","wb") as f:
            f.write(audio.get_flac_data())