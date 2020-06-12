from googletrans import Translator
from gtts import gTTS
import os
sentence ="I really hate you"
translator = Translator()
translated_sentence1 = translator.translate(sentence,src='en',dest='ko')
translated_sentence2 = translator.translate(sentence,src='en',dest='ja')
print(translated_sentence1)
print(translated_sentence2)

output = gTTS(text=str(translated_sentence2.text), lang='ja', slow=False)
output.save("output.mp3")
os.system("start output.mp3")




