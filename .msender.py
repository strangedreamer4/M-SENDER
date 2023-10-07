import socket
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def send_file(receiver_host, receiver_port, file_path):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the receiver
        s.connect((receiver_host, receiver_port))
        
        # Send the filename
        filename = os.path.basename(file_path)
        s.send(filename.encode())
        
        # Send the file data
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                s.send(data)
        
        messagebox.showinfo("Success", f"File '{filename}' sent successfully to {receiver_host}:{receiver_port}")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
    finally:
        s.close()

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)

def send_file_to_receiver():
    receiver_host = receiver_host_entry.get()
    receiver_port_str = receiver_port_entry.get()
    file_path = file_path_entry.get()

    if not receiver_host:
        messagebox.showerror("Error", "Receiver Host cannot be empty.")
        return

    if not receiver_port_str.isdigit():
        messagebox.showerror("Error", "Receiver Port must be a positive integer.")
        return

    receiver_port = int(receiver_port_str)

    if not os.path.isfile(file_path):
        messagebox.showerror("Error", "Invalid file path.")
        return

    send_file(receiver_host, receiver_port, file_path)

# Create the main window for the sender
root = tk.Tk()
root.title("File Sender")

# Dark theme
root.configure(bg="black")

# Green text color
text_color = "green"

# Create and arrange widgets for sender
receiver_host_label = tk.Label(root, text="Receiver Host:", fg=text_color, bg="black")
receiver_host_label.pack()

receiver_host_entry = tk.Entry(root, width=50)
receiver_host_entry.pack()

receiver_port_label = tk.Label(root, text="Receiver Port:", fg=text_color, bg="black")
receiver_port_label.pack()

receiver_port_entry = tk.Entry(root, width=50)
receiver_port_entry.pack()

file_path_label = tk.Label(root, text="Select File to Send:", fg=text_color, bg="black")
file_path_label.pack()

file_path_entry = tk.Entry(root, width=50)
file_path_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file, fg=text_color, bg="black", relief="flat")
browse_button.pack()

send_button = tk.Button(root, text="Send File", command=send_file_to_receiver, fg=text_color, bg="black", relief="flat")
send_button.pack()

root.mainloop()

