
# coding: utf-8

# In[2]:


from Crypto.Cipher import AES
from Crypto import Random
import os
import json


# ### Encryption and decription function

# In[3]:


class encryption(object):
    
    #set variables
    def __init__(self, key):
        self.key = key
        #Preset the AES
        self.aes_mode = AES.MODE_CBC
        

    #Check security level
    def security_level(self):
        key_len = len(self.key)
        if key_len == 16:
            print("key length: 16 bytes")
            print("128-bit encryption")
        if key_len == 24:
            print("key length: 24 bytes")
            print("192-bit encryption")
        if key_len == 32:
            print("key length: 32 bytes")
            print("256-bit encryption")
        else:
            print("Invalid key")

    #Function encrypt data
    def encrypt(self, data):
        iv = Random.new().read(AES.block_size)
        obj = AES.new(self.key, self.aes_mode, iv)
        while True:
            #Ensure data length is a multitude of 16
            n = len(data)
            if n == 0:
                break
            elif n % 16 != 0:
                data += ' ' * (16 - n % 16) # <- padded with spaces
            #encrypt data
            encd = obj.encrypt(data)
            print("Encrypted data: \n%s" %encd)
            return (iv + encd)
            break

    #Function to decript data
    def decrypt(self, data):
        iv = data[:16]
        _data = data[16:]
        obj = AES.new(self.key, self.aes_mode, iv)
        #decrypt data
        ciphertext = obj.decrypt(_data)
        #remove padding at end of string
        ciphertext = ciphertext.strip()
        #decode from bytes to utf-8
        ciphertext = ciphertext.decode('utf-8')
        print("Decrypted data: \n%s" %ciphertext)
        return ciphertext


# ### Encryption key

# In[4]:


class secure_key(object):
    
    def __init__(self):
        self.key = "_OAjvI8J$skNGu/7F9PVJ7vuIgghwn$v"
        self.aes_mode = AES.MODE_CBC
    
    
    #Function to enccrypt key and store it as json
    def encrypt_key(self, key, filename):
        #Generate random public key
        iv = Random.new().read(AES.block_size)
        #Object to encrypt key
        obj = AES.new(self.key, self.aes_mode, iv)
        encrypted_key = obj.encrypt(key)
        encrypted_key = (iv + encrypted_key)
        #Save encrypted key to json file
        with open(filename, 'wb') as fp:
            fp.write(encrypted_key)
            fp.close()
        print("Key encrypted and stored as %s" %filename)
        
    def decrypt_key(self, filename):
        #Open read json file
        with open(filename, 'rb') as fp:
            data = fp.read()
            #retrieve public key
            iv = data[:16]
            #retrieve encrypted key
            key = data[16:]
            #Object to decrypt key
            obj = AES.new(self.key, self.aes_mode, iv)
            _key = obj.decrypt(key)
            fp.close()
            return _key

