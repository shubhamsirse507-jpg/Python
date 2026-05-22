import tkinter as tk
from tkinter import messagebox
import time

# IP Database
a = "192.168.0.1"
b = "192.168.0.3"
c = "192.168.1.34"

# Security Codes
A = "465111"
B = "465110"
C = "205601"

# Function for IP Detection
def detect_ip():
    ip = ip_entry.get()

    result_label.config(text="Locating IP.....")
    window.update()
    time.sleep(2)

    if ip == a:
        result_label.config(text=f"{a}\nIP Located at Pune")

    elif ip == b:
        result_label.config(text=f"{b}\nIP Located at Mumbai")

    elif ip == c:
        result_label.config(text=f"{c}\nIP Located at Chikhali")

    else:
        result_label.config(text="IP is not found in any location")


# Function for Security Code
def lock_phone():
    sq = code_entry.get()

    if sq == A:
        messagebox.showinfo("Phone Lock", f"Phone is Locked {A}")

    elif sq == B:
        messagebox.showinfo("Phone Lock", f"Phone is Locked {B}")

    elif sq == C:
        messagebox.showinfo("Phone Lock", f"Phone is Locked {C}")

    else:
        messagebox.showerror("Error", "Enter Correct Security Code")


# Main Window
window = tk.Tk()
window.title("Simple IP Detector")
window.geometry("400x350")
window.config(bg="lightblue")

# Title
title = tk.Label(
    window,
    text="IP Location & Phone Lock",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
title.pack(pady=10)

# IP Section
ip_label = tk.Label(window, text="Enter IP Address:", bg="lightblue")
ip_label.pack()

ip_entry = tk.Entry(window, width=30)
ip_entry.pack(pady=5)

ip_button = tk.Button(
    window,
    text="Detect Location",
    command=detect_ip,
    bg="green",
    fg="white"
)
ip_button.pack(pady=10)

result_label = tk.Label(window, text="", bg="lightblue", font=("Arial", 11))
result_label.pack(pady=10)

# Security Code Section
code_label = tk.Label(window, text="Enter Security Code:", bg="lightblue")
code_label.pack()

code_entry = tk.Entry(window, width=30, show="*")
code_entry.pack(pady=5)

lock_button = tk.Button(
    window,
    text="Lock Phone",
    command=lock_phone,
    bg="red",
    fg="white"
)
lock_button.pack(pady=15)

# Run Window
window.mainloop()