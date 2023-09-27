import rsa

(public_key, private_key) = rsa.newkeys(2048)

with open("file.txt", "rb") as f:
    data = f.read()

encrypted_data = rsa.encrypt(data, public_key)

with open("encrypted_file.txt", "wb") as f:
    f.write(encrypted_data)

with open("encrypted_file.txt", "rb") as f:
    encrypted_data = f.read()

decrypted_data = rsa.decrypt(encrypted_data, private_key)

print(decrypted_data)