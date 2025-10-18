import tkinter as tk

# Function to convert inches to centimeters
def convert_to_cm():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{inches} inches = {centimeters:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Create main window
window = tk.Tk()
window.title("Inches to Centimeters Converter")
window.geometry("350x200")
window.configure(bg="#f0f8ff")  # Light blue background

# Heading
heading = tk.Label(window, text="Length Converter", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#003366")
heading.pack(pady=10)

# Input label and entry
input_frame = tk.Frame(window, bg="#f0f8ff")
input_frame.pack(pady=5)

tk.Label(input_frame, text="Enter length in inches:", bg="#f0f8ff").pack(side="left")
entry = tk.Entry(input_frame, width=15)
entry.pack(side="left", padx=10)

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_to_cm,
                           bg="#4CAF50", fg="white", activebackground="#45a049")
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
result_label.pack(pady=10)

# Run the application
window.mainloop()

