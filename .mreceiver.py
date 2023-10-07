import socket
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import threading

def receive_file(save_dir, host, port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the host and port
        s.bind((host, port))

        # Listen for incoming connections
        s.listen(5)
        status_label.config(text=f"Listening on {host}:{port}...")

        while True:
            # Accept a connection from a client
            conn, addr = s.accept()
            status_label.config(text=f"Accepted connection from {addr}")

            # Receive the filename
            filename = conn.recv(1024).decode()
            file_path = os.path.join(save_dir, filename)

            # Receive and save the file data
            with open(file_path, 'wb') as file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file.write(data)
            status_label.config(text=f"File '{filename}' received and saved as '{file_path}'")
    except Exception as e:
        status_label.config(text=f"Error: {e}")
    finally:
        s.close()

def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        save_dir_entry.delete(0, tk.END)
        save_dir_entry.insert(0, directory_path)

def start_receiver():
    save_dir = save_dir_entry.get()
    host = host_entry.get()
    port_str = port_entry.get()

    if not os.path.isdir(save_dir):
        messagebox.showerror("Error", "Invalid save directory.")
        return

    if not host:
        messagebox.showerror("Error", "Host cannot be empty.")
        return

    if not port_str.isdigit():
        messagebox.showerror("Error", "Port must be a positive integer.")
        return

    port = int(port_str)

    receiver_thread = threading.Thread(target=receive_file, args=(save_dir, host, port))
    receiver_thread.daemon = True
    receiver_thread.start()

    status_label.config(text="Receiver started.")

# Create the main window
root = tk.Tk()
root.title("File Receiver")
root.geometry("400x400")  # Set the window size

# Dark theme
root.configure(bg="black")

# Green text color
text_color = "green"

# Create and arrange widgets
save_dir_label = tk.Label(root, text="Save Directory:", fg=text_color, bg="black")
save_dir_label.pack()

save_dir_entry = tk.Entry(root, width=50)
save_dir_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_directory, fg=text_color, bg="black", relief="flat")
browse_button.pack()

host_label = tk.Label(root, text="Host:", fg=text_color, bg="black")
host_label.pack()

host_entry = tk.Entry(root, width=50)
host_entry.pack()

port_label = tk.Label(root, text="Port:", fg=text_color, bg="black")
port_label.pack()

port_entry = tk.Entry(root, width=50)
port_entry.pack()

start_button = tk.Button(root, text="Start Receiver", command=start_receiver, fg=text_color, bg="black", relief="flat")
start_button.pack()

status_label = tk.Label(root, text="", fg="green", bg="black")
status_label.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit, fg=text_color, bg="black", relief="flat")
exit_button.pack()

# Center the window on the screen
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_x = (root.winfo_screenwidth() // 2) - (window_width // 2)
position_y = (root.winfo_screenheight() // 2) - (window_height // 2)
root.geometry("+{}+{}".format(position_x, position_y))

root.mainloop()
