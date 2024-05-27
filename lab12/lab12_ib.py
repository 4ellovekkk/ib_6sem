import time
import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from concurrent.futures import ThreadPoolExecutor
from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
from ecdsa import SigningKey, NIST192p

def rsa_generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def rsa_sign_message(private_key, message):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def rsa_verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False
    

def elgamal_generate_keys():
    key = ElGamal.generate(2048, get_random_bytes)
    return key, key.publickey()

def elgamal_sign_message(private_key, message):
    h = int.from_bytes(hashlib.sha256(message).digest(), byteorder='big')
    k = private_key.random_element()
    signature = private_key.sign(h, k)
    return signature

def elgamal_verify_signature(public_key, message, signature):
    h = int.from_bytes(hashlib.sha256(message).digest(), byteorder='big')
    return public_key.verify(h, signature)

def schnorr_generate_keys():
    sk = SigningKey.generate(curve=NIST192p)
    vk = sk.verifying_key
    return sk, vk

def schnorr_sign_message(private_key, message):
    return private_key.sign(message)

def schnorr_verify_signature(public_key, message, signature):
    return public_key.verify(signature, message)

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

def key_exchange_simulation():
    message = b"Sample message for signing"

    with ThreadPoolExecutor() as executor:
        rsa_future = executor.submit(rsa_generate_keys)
        elgamal_future = executor.submit(elgamal_generate_keys)
        schnorr_future = executor.submit(schnorr_generate_keys)

        rsa_private, rsa_public = rsa_future.result()
        elgamal_private, elgamal_public = elgamal_future.result()
        schnorr_private, schnorr_public = schnorr_future.result()

        rsa_signature, rsa_time = measure_time(rsa_sign_message, rsa_private, message)
        rsa_verification_result, rsa_verify_time = measure_time(rsa_verify_signature, rsa_public, message, rsa_signature)

        elgamal_signature, elgamal_time = measure_time(elgamal_sign_message, elgamal_private, message)
        elgamal_verification_result, elgamal_verify_time = measure_time(elgamal_verify_signature, elgamal_public, message, elgamal_signature)

        schnorr_signature, schnorr_time = measure_time(schnorr_sign_message, schnorr_private, message)
        schnorr_verification_result, schnorr_verify_time = measure_time(schnorr_verify_signature, schnorr_public, message, schnorr_signature)

        print(f"RSA: sign time {rsa_time}, verify time {rsa_verify_time}")
        print(f"ElGamal: sign time {elgamal_time}, verify time {elgamal_verify_time}")
        print(f"Schnorr: sign time {schnorr_time}, verify time {schnorr_verify_time}")

key_exchange_simulation()
