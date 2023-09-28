import rsa

def encrypt_file(public_key, file_name):
    with open(file_name, "rb") as f:
        data = f.read()

    encrypted_data = rsa.encrypt(data, public_key)

    with open(file_name + ".enc", "wb") as f:
        f.write(encrypted_data)

def decrypt_file(private_key, file_name):
    with open(file_name, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = rsa.decrypt(encrypted_data, private_key)

    with open(file_name + ".dec", "wb") as f:
        f.write(decrypted_data)

public_key = rsa.PublicKey.load_from_file("public.pem")
private_key = rsa.PrivateKey.load_from_file("private.pem")

encrypt_file(public_key, "file.txt")
decrypt_file(private_key, "file.txt.enc")