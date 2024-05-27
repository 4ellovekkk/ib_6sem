# from cryptography.hazmat.primitives.asymmetric import elgamal
import time
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from sympy.ntheory.generate import randprime
from Crypto.Util import number
from sympy import isprime, mod_inverse
import random
# RSA шифрование и расшифрование
def rsa_encrypt_decrypt(document):
    # Генерация ключей
    key = RSA.generate(2048)
    public_key = key.publickey()
    cipher_rsa = PKCS1_OAEP.new(public_key)

    # Зашифрование
    start_time = time.time()
    encrypted_document = cipher_rsa.encrypt(document.encode('utf-8'))
    encrypted_document_b64 = base64.b64encode(encrypted_document).decode('utf-8')
    encrypt_time = time.time() - start_time

    # Расшифрование
    start_time = time.time()
    decrypted_document = PKCS1_OAEP.new(key).decrypt(base64.b64decode(encrypted_document_b64.encode('utf-8')))
    decrypt_time = time.time() - start_time

    return encrypt_time, decrypt_time, decrypted_document.decode('utf-8')

# Эль-Гамаль шифрование и расшифрование
def elgamal_encrypt_decrypt(document):
    # Генерация параметров
    def generate_large_prime(bits):
        while True:
            candidate = number.getPrime(bits)
            if isprime(candidate):
                return candidate
    
    bits = 2048
    p = generate_large_prime(bits)
    g = 2
    x = random.randint(1, p-2)
    y = pow(g, x, p)

    # Генерация открытого и закрытого ключа
    public_key = (p, g, y)
    private_key = x

    # Зашифрование
    k = random.randint(1, p-2)
    a = pow(g, k, p)
    b = (pow(y, k, p) * int.from_bytes(document.encode('utf-8'), 'big')) % p

    start_time = time.time()
    encrypted_document = (a, b)
    encrypted_document_b64 = (base64.b64encode(a.to_bytes((a.bit_length() + 7) // 8, 'big')).decode('utf-8'),
                              base64.b64encode(b.to_bytes((b.bit_length() + 7) // 8, 'big')).decode('utf-8'))
    encrypt_time = time.time() - start_time

    # Расшифрование
    start_time = time.time()
    decrypted_int = (encrypted_document[1] * mod_inverse(pow(encrypted_document[0], private_key, p), p)) % p
    decrypted_document = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    decrypt_time = time.time() - start_time

    return encrypt_time, decrypt_time, decrypted_document

# Тестирование функций
document = "Hello, this is a test document for encryption and decryption!"

# RSA
rsa_encrypt_time, rsa_decrypt_time, rsa_decrypted_document = rsa_encrypt_decrypt(document)
print(f"RSA Encryption Time: {rsa_encrypt_time:.6f} s, Decryption Time: {rsa_decrypt_time:.6f} s")
print(f"RSA Decrypted Document: {rsa_decrypted_document}")

# ElGamal
elgamal_encrypt_time, elgamal_decrypt_time, elgamal_decrypted_document = elgamal_encrypt_decrypt(document)
print(f"ElGamal Encryption Time: {elgamal_encrypt_time:.6f} s, Decryption Time: {elgamal_decrypt_time:.6f} s")
print(f"ElGamal Decrypted Document: {elgamal_decrypted_document}")