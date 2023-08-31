import tkinter as tk
from gtts import gTTS
def convert_text_to_speech():
    text = text_entry.get()
    if text.strip():
        tts = gTTS(text=text, lang='en')
        tts.save("aryan.mp3")
        status_label.config(text="Audio saved as aryan.mp3")
    else:
        status_label.config(text="Please enter text to convert.")

app = tk.Tk()
app.title("Text to Speech Converter")
text_label = tk.Label(app, text="Enter text:")
text_label.pack()
text_entry = tk.Entry(app, width=50)
text_entry.pack()
convert_button = tk.Button(app, text="Convert to Speech", command=convert_text_to_speech)
convert_button.pack()
status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()






