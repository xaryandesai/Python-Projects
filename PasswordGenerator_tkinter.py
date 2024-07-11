import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_special_chars = special_chars_var.get()
    use_lowercase_chars = lowercase_chars_var.get()
    use_uppercase_chars = uppercase_chars_var.get()
    use_numbers = numbers_var.get()
    characters = ''
    if use_special_chars:
        characters += string.punctuation
    if use_lowercase_chars:
        characters += string.ascii_lowercase
    if use_uppercase_chars:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if not characters:
        result_label.config(text="Please select at least one character type.")
        return
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Generated Password: " + password)
    
app = tk.Tk()
app.title("Password Generator")

length_label = tk.Label(app, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(app)
length_entry.pack()

special_chars_var = tk.IntVar()
special_chars_check = tk.Checkbutton(app, text="Use Special Characters", variable=special_chars_var)
special_chars_check.pack()

lowercase_chars_var = tk.IntVar()
lowercase_chars_check = tk.Checkbutton(app, text="Use Lowercase Characters", variable=lowercase_chars_var)
lowercase_chars_check.pack()
uppercase_chars_var = tk.IntVar()
uppercase_chars_check = tk.Checkbutton(app, text="Use Uppercase Characters", variable=uppercase_chars_var)
uppercase_chars_check.pack()

numbers_var = tk.IntVar()
numbers_check = tk.Checkbutton(app, text="Use Numbers", variable=numbers_var)
numbers_check.pack()
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack()
result_label = tk.Label(app, text="")
result_label.pack()
app.mainloop()
