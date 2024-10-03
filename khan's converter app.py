import tkinter as tk

def convert_to_binary():
    try:
        decimal = int(entry.get())
        binary = bin(decimal)[2:]  # Convert to binary and remove '0b'
        result_binary.config(text=f"Binary: {binary}")
    except ValueError:
        result_binary.config(text="Invalid input! Please enter an integer.")

def convert_to_hexadecimal():
    try:
        decimal = int(entry.get())
        hexadecimal = hex(decimal)[2:].upper()  # Convert to hex and remove '0x'
        result_hexadecimal.config(text=f"Hexadecimal: {hexadecimal}")
    except ValueError:
        result_hexadecimal.config(text="Invalid input! Please enter an integer.")
        
def convert_to_octal():
    try:
        decimal = int(entry.get())
        octal = oct(decimal)[2:]. upper()  #convert to oct and remove  '0o'
        result_octal.config(text=f"octal: {octal}")
    except ValueError:
        result_octal.config(text="Invalid input! Please enter an integer.")  
          
        
# Set up the main application window
root = tk.Tk()
root.title("Number Converter")

# Input field
entry = tk.Entry(root)
entry.pack(pady=15)

# Conversion buttons
button_binary = tk.Button(root, text="Convert to Binary", command=convert_to_binary)
button_binary.pack(pady=5)

button_hexadecimal = tk.Button(root, text="Convert to Hexadecimal", command=convert_to_hexadecimal)
button_hexadecimal.pack(pady=5)

button_octal = tk.Button(root, text="Convert to octal",  command=convert_to_octal)
button_octal.pack(pady=5)

# Result labels
result_binary = tk.Label(root, text="")
result_binary.pack(pady=5)

result_hexadecimal = tk.Label(root, text="")
result_hexadecimal.pack(pady=5)


result_octal = tk.Label(root, text ="")
result_octal.pack(pady=5)

# Run the app
root.mainloop()
