import json
from decryption import Decryption
path = r"C:\Users\OJTVince\AppData\Local\garble\user_data.json"

with open(path, 'r') as f:
    words = json.load(f)
    # print(words)
    final_list_encryption = (f"{(words['final_list_encryption'])}")
    store_encrypted_int = (f"{(words['store_encrypted_int'])}")
    special_key_storage = (f"{(words['special_key_storage'])}")
    encrypted = (f"{(words['encrypted'])}")
    print(final_list_encryption)
    print(store_encrypted_int)
    print(special_key_storage)
    print(encrypted)

    # sol = Decryption(final_list_encryption, store_encrypted_int, special_key_storage, encrypted)
    # print(sol.final_decryption()) #need output
