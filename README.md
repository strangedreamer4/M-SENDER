# M-SENDER

**Tool Name**: `msender`

**Description**:
`msender` is a user-friendly file transfer tool designed to simplify the process of sending files from one computer to another over a network. With a straightforward graphical user interface (GUI), `msender` eliminates the need for complex command-line operations, making file sharing effortless and accessible for users of all levels of technical expertise.

**Key Features**:

1. **Intuitive GUI**: `msender` offers a user-friendly graphical interface, making it easy for users to send files without the need for extensive technical knowledge.

2. **Flexible Host Configuration**: Users can specify the receiver's host address (e.g., IP address or hostname) to target the destination computer.

3. **Custom Port Selection**: You can choose the port through which files will be sent, providing flexibility to work within your network's configuration.

4. **File Selection**: `msender` allows you to select files for transmission using a built-in file browser. Simply click the "Browse" button to choose the file you want to send.

5. **Real-time Status Updates**: The tool provides real-time status updates, informing you about the progress of the file transfer, including successful completion or any encountered errors.

6. **Error Handling**: If any issues occur during the file transfer process, `msender` will display error messages to help you diagnose and resolve problems promptly.

**Usage**:

1. Launch `msender` by running the `python3 msender.py` script.
2. Input the receiver's host address in the "Receiver Host" field. This can be an IP address or hostname.
3. Specify the receiver's listening port in the "Receiver Port" field.
4. Click the "Browse" button to select the file you wish to send.
5. Initiate the file transfer by clicking the "Send File" button.
6. Monitor the status updates in the GUI to track the progress of the transfer.

**Use Cases**:

- Sharing documents, images, and other files between computers within a local network.
- Sending files securely to a remote server.
- Collaborative work, enabling team members to exchange project-related files easily.
- Backing up important data by transferring files to a remote storage location.

**Note**:
- Ensure that both the sender and receiver computers are on the same network or can communicate over the specified network configuration.
- Verify that the receiver computer has the appropriate receiver tool (e.g., `mreceiver`) running to accept incoming files from `msender`.
