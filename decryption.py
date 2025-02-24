import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")
if img is None:
    print("Encrypted image not found!")
    exit()

# Retrieve stored password
try:
    with open("pass.txt", "r") as f:
        correct_pass = f.read().strip()
except FileNotFoundError:
    print("Password file not found!")
    exit()

# Verify password
pas = input("Enter passcode for Decryption: ")
if pas != correct_pass:
    print("Incorrect passcode. Access denied!")
    exit()

# Extract message with null terminator
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

print("Decrypted message:", message)