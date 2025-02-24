import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import cv2
import os

# Global variables to store file paths
cover_image_path = ""
encrypted_image_path = ""

def load_cover_image():
    global cover_image_path
    cover_image_path = filedialog.askopenfilename(
        title="Select Cover Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if cover_image_path:
        cover_label.config(text=os.path.basename(cover_image_path))
    else:
        cover_label.config(text="No file selected")

def load_encrypted_image():
    global encrypted_image_path
    encrypted_image_path = filedialog.askopenfilename(
        title="Select Encrypted Image",
        filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")]
    )
    if encrypted_image_path:
        encrypted_label.config(text=os.path.basename(encrypted_image_path))
    else:
        encrypted_label.config(text="No file selected")

def encrypt_message():
    if not cover_image_path:
        messagebox.showerror("Error", "Please load a cover image!")
        return
    msg = enc_message_entry.get()
    password = enc_password_entry.get()
    if not msg:
        messagebox.showerror("Error", "Please enter a secret message!")
        return
    if not password:
        messagebox.showerror("Error", "Please enter an encryption passcode!")
        return

    # Load the cover image
    img = cv2.imread(cover_image_path)
    if img is None:
        messagebox.showerror("Error", "Failed to load the cover image!")
        return

    # Save encryption passcode
    with open("pass.txt", "w") as f:
        f.write(password)

    # Embed message with null terminator
    n, m, z = 0, 0, 0
    for char in msg + '\0':  # Add null terminator
        if n >= img.shape[0] or m >= img.shape[1]:
            messagebox.showerror("Error", "Message too long for image!")
            return
        img[n, m, z] = ord(char)
        n += 1
        m += 1
        z = (z + 1) % 3

    # Save encrypted image
    cv2.imwrite("encryptedImage.png", img)
    messagebox.showinfo("Success", "Secret message embedded into image and saved as 'encryptedImage.png'.")

def decrypt_message():
    if not encrypted_image_path:
        messagebox.showerror("Error", "Please load an encrypted image!")
        return
    password_input = dec_password_entry.get()
    
    try:
        with open("pass.txt", "r") as f:
            correct_pass = f.read().strip()
    except Exception as e:
        messagebox.showerror("Error", "Password file not found!")
        return

    if password_input != correct_pass:
        messagebox.showerror("Error", "Incorrect passcode. Access denied!")
        return

    # Load encrypted image
    img = cv2.imread(encrypted_image_path)
    if img is None:
        messagebox.showerror("Error", "Failed to load encrypted image!")
        return

    # Extract message until null terminator
    message = ""
    n, m, z = 0, 0, 0
    while True:
        if n >= img.shape[0] or m >= img.shape[1]:
            break
        char = chr(img[n, m, z])
        if char == '\0':
            break
        message += char
        n += 1
        m += 1
        z = (z + 1) % 3

    dec_text.delete(1.0, tk.END)
    dec_text.insert(tk.END, message)

# Create main window with modern theme
root = tk.Tk()
root.title("3D Steganography Suite")
root.geometry("800x600")
root.configure(bg='#2E2E2E')

style = ttk.Style()
style.theme_use('clam')

# Configure colors and styles
style.configure('TFrame', background='#2E2E2E')
style.configure('TLabelframe', background='#3A3A3A', foreground='white')
style.configure('TLabelframe.Label', background='#3A3A3A', foreground='white')
style.configure('TLabel', background='#3A3A3A', foreground='white')
style.configure('TButton', background='#0078D4', foreground='white', 
                font=('Segoe UI', 10, 'bold'), borderwidth=0)
style.map('TButton', 
          background=[('active', '#005A9E'), ('pressed', '#004B87')])

# Main container
main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20, fill='both', expand=True)

# Cover Image Section
cover_frame = ttk.Labelframe(main_frame, text=" Cover Image (Encryption) ")
cover_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

btn_load_cover = ttk.Button(cover_frame, text="📁 Load Cover Image", command=load_cover_image)
btn_load_cover.grid(row=0, column=0, padx=10, pady=10)

cover_label = ttk.Label(cover_frame, text="No file selected", foreground='#CCCCCC')
cover_label.grid(row=0, column=1, padx=10, pady=10)

# Encryption Section
enc_frame = ttk.Labelframe(main_frame, text=" Encryption Settings ")
enc_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

ttk.Label(enc_frame, text="Secret Message:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
enc_message_entry = ttk.Entry(enc_frame, width=40)
enc_message_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(enc_frame, text="Passcode:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
enc_password_entry = ttk.Entry(enc_frame, width=40, show="•")
enc_password_entry.grid(row=1, column=1, padx=10, pady=5)

btn_encrypt = ttk.Button(enc_frame, text="🔒 Encrypt Message", command=encrypt_message)
btn_encrypt.grid(row=2, column=0, columnspan=2, pady=10)

# Encrypted Image Section
encrypted_frame = ttk.Labelframe(main_frame, text=" Encrypted Image (Decryption) ")
encrypted_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

btn_load_encrypted = ttk.Button(encrypted_frame, text="📁 Load Encrypted Image", command=load_encrypted_image)
btn_load_encrypted.grid(row=0, column=0, padx=10, pady=10)

encrypted_label = ttk.Label(encrypted_frame, text="No file selected", foreground='#CCCCCC')
encrypted_label.grid(row=0, column=1, padx=10, pady=10)

# Decryption Section
dec_frame = ttk.Labelframe(main_frame, text=" Decryption Settings ")
dec_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

ttk.Label(dec_frame, text="Passcode:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
dec_password_entry = ttk.Entry(dec_frame, width=40, show="•")
dec_password_entry.grid(row=0, column=1, padx=10, pady=5)

btn_decrypt = ttk.Button(dec_frame, text="🔓 Decrypt Message", command=decrypt_message)
btn_decrypt.grid(row=1, column=0, columnspan=2, pady=10)

ttk.Label(dec_frame, text="Decrypted Message:").grid(row=2, column=0, padx=10, pady=5, sticky='ne')
dec_text = scrolledtext.ScrolledText(dec_frame, width=40, height=5, bg='#404040', fg='white')
dec_text.grid(row=2, column=1, padx=10, pady=10)

# Configure grid column weights
for child in main_frame.winfo_children():
    child.grid_configure(padx=10, pady=5)
main_frame.columnconfigure(0, weight=1)

root.mainloop()