import tkinter as tk
import subprocess

def launch_sender():
    subprocess.Popen(["python", ".msender.py"])

def launch_receiver():
    subprocess.Popen(["python", ".mreceiver.py"])

# Create the main window for the launcher with a dark theme and green text color
root = tk.Tk()
root.title("File Transfer Launcher")
root.geometry("400x200")  # Set the window size

# Dark theme
root.configure(bg="black")

# Green text color
text_color = "green"

# Create and arrange widgets for launcher
sender_button = tk.Button(root, text="Launch Sender", command=launch_sender, fg=text_color, bg="black", relief="flat")
sender_button.pack(pady=20)  # Add padding between the buttons

receiver_button = tk.Button(root, text="Launch Receiver", command=launch_receiver, fg=text_color, bg="black", relief="flat")
receiver_button.pack(pady=20)  # Add padding between the buttons

root.mainloop()
