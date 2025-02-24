# 🖼️ **Steganography Tool: Hide Secrets in Images**  

Welcome to the **Steganography Tool**! This Python-based application lets you hide secret messages inside images and retrieve them later—all while keeping your data safe and secure. Whether you're a privacy enthusiast, a student, or just someone who loves cool tech, this tool is for you.  

---

## ✨ **Features**  

### **What Can You Do?**  
- **Hide Messages:** Embed text messages into any image without visibly altering it.  
- **Retrieve Secrets:** Extract hidden messages using a secure passcode.  
- **User-Friendly Interface:** A simple Tkinter-based GUI makes the process easy and intuitive.  
- **Cross-Platform:** Works on Windows, macOS, and Linux.  

### **How It Works**  
- **Encryption:**  
  - Each character of your message is converted to its ASCII value.  
  - The values are embedded into the image pixels using a diagonal embedding method.  
  - The modified image is saved as a lossless PNG file.  
- **Decryption:**  
  - The program reads the pixel values and reconstructs the hidden message.  
  - A passcode ensures only authorized users can access the message.  

---

## 🛠️ **Installation**  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/Soumya-Charan/Stegnography.git
   cd Stegnography
   ```

2. **Install Dependencies:**  
   Make sure you have Python 3.x installed. Then, install the required libraries:  
   ```bash
   pip install opencv-python
   ```

3. **Run the Application:**  
   - For the **GUI version**, run:  
     ```bash
     python stego_gui.py
     ```  
   - For the **command-line version**, use:  
     ```bash
     python encryption.py  # To hide a message
     python decryption.py  # To extract a message
     ```

---

## 🖼️ **Screenshots**  

Here’s a sneak peek of the application in action:  

![Capture](https://github.com/user-attachments/assets/3fd74423-c945-4983-9c5f-f17d397e0b8e)


---

## 🚀 **How to Use**  

### **Using the GUI**  
1. **Encrypt a Message:**  
   - Click "Load Cover Image" to select an image.  
   - Enter your secret message and a passcode.  
   - Click "Encrypt" to save the modified image.  

2. **Decrypt a Message:**  
   - Click "Load Encrypted Image" to select the modified image.  
   - Enter the passcode.  
   - Click "Decrypt" to reveal the hidden message.  

### **Using the Command Line**  
- **Encryption:**  
  - Run `encryption.py`.  
  - Follow the prompts to enter your message and passcode.  
  - The program will save the encrypted image as `encryptedImage.png`.  

- **Decryption:**  
  - Run `decryption.py`.  
  - Enter the passcode when prompted.  
  - The program will display the hidden message.  

---

## ⚠️ **Important Notes**  
- **Image Size:** Longer messages require larger images. If the message is too long, it may not fit!  
- **File Format:** Always use PNG images for encryption to avoid data loss.  
- **Password Security:** Keep your passcode safe—it’s the key to unlocking your message!  

---

## 🤝 **Contributing**  

Love this project? Want to make it even better? Here’s how you can help:  
- **Report Bugs:** Open an issue on GitHub.  
- **Suggest Features:** Share your ideas for new features or improvements.  
- **Submit Code:** Fork the repository, make your changes, and submit a pull request.  

---

**Happy Hiding!** 😉  

