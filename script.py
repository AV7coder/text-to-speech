from gtts import gTTS
import os
text = input("""Enter the text you want to convert to speech:
""") # takes the input from user
title = input("Enter the file title: ")
file = gTTS(text) # makes the file
file.save(f'{title}.mp3')# saves the file
os.startfile(f'{title}.mp3') # opens the file
# yayyayay suuuuu
