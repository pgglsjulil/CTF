methods = ['md5', 'sha256', 'sha3_256', 'sha3_512', 'sha3_384', 'sha1', 'sha384', 'sha3_224', 'sha512', 'sha224']

def try_hash_methods(hash_value, possible_value):
    for method in methods:
        for value in possible_value:
            x = value
            value = chr(value)

def decrypt_message():
    possible_value = range(255)
    reversed_value = try_hash_methods()



def main():
    encrypted = eval(open("encrypted_memory.txt", "r")).read()
    message = []

    # for enc in encrypted:
        # char = 