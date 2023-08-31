#Example No. - +40721234567
import tkinter as tk
import phonenumbers
from phonenumbers import geocoder, carrier

def track_number():
    input_number = number_entry.get()

    try:
        phone_number = phonenumbers.parse(input_number, None)
    except phonenumbers.NumberParseException:
        result_label.config(text="Invalid phone number")
        return

    if not phonenumbers.is_valid_number(phone_number):
        result_label.config(text="Invalid phone number")
        return

    country = geocoder.description_for_number(phone_number, "en")
    carrier_name = carrier.name_for_number(phone_number, "en")

    result_text = f"Country: {country}\nCarrier: {carrier_name}"
    result_label.config(text=result_text)
app = tk.Tk()
app.title("Phone Number Tracker")
number_label = tk.Label(app, text="Enter phone number:")
number_label.pack()

number_entry = tk.Entry(app, width=30)
number_entry.pack()

track_button = tk.Button(app, text="Track Number", command=track_number)
track_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()



