__author__ = "Daniel Faustino"
__copyright__ = "Copyright 2019, Codenation Project 2019"
__credits__ = ["Daniel Faustino"]
__license__ = "GPL"
__version__ = "0.8.1"
__maintainer__ = "Daniel Faustino"
__email__ = "daniel.fsantos@protonmail.com"
__status__ = "dev"

# import request and post url and token from another file
from config import  url_post, url_request, token
# importing libraries
import urllib3                                              # library to HTTP request
import json                                                 # library to JSON handles
import hashlib                                              # library to hash SHA1

# starting PoolManages to handles connections
http = urllib3.PoolManager()

# starting request
request_get = http.request(
    'GET',
    url_request + token)

'''
converting request to JSON
'''
# converting to dict type
request_dict = json.loads(request_get.data)
print(json.dumps(request_dict, indent=2))                   # printing (optional)
print('\n')                                                 # jumping one line (optional)

'''
creating a JSON file
'''
answer = open('answer', 'w')                                # creating a file
answer.write(json.dumps(request_dict, indent=2))             # writing in file
answer.close()  # closing file

'''
applying the Caesar Cipher
'''
encrypted = request_dict['cifrado']                         # get the message
encrypted = encrypted.lower()                               # making message lower case
key_value = request_dict['numero_casas']                    # get key
decrypted = ''                                              # it's get the decrypted message

# decrypt the message
for symbol in encrypted:                                    # for each char in message
    if symbol.isalpha():                                    # if char is a letter
        ascii_code = ord(symbol)                            # get the ASCII position
        ascii_code -= key_value                             # get de decrypetd position

        if ascii_code > ord('z'):                           # if letter is out lower alphabet
            ascii_code -= 26                                # positioning in lower alphabet
        elif ascii_code < ord('a'):                         # if letter is out lower alphabet
            ascii_code += 26                                # positioning in lower alphabet

        decrypted += chr(ascii_code)                        # decrypt each letter
    else:
        decrypted += symbol                                 # remain number, point and space

print('Decrypted Message: ', decrypted)                     # print message (optional)
print('\n')                                                 # jump one line (optional)

'''
geting SHA1 in decrypted message
'''
# get hash
resume = hashlib.sha1(decrypted.encode()).hexdigest()
print('HASH: ', resume)                                     # priting (optional)
print('\n')                                                 # jump one line (optional)

# update the value in JSON dict
request_dict['decifrado'] = decrypted                       # change value
request_dict['resumo_criptografico'] = resume               # chance value
answer = open('answer.json', 'w')                           # open file to write
answer.write(json.dumps(request_dict, indent=2))            # updating the file
answer.close()                                              # closing the file

print(json.dumps(request_dict, indent=2))                   # printing the updated file
print('\n')                                                 # jumping one line

# post the file
with open('answer.json') as answer:
    file_data = answer.read()

request_post = http.request(
    'POST',
    url_post + token,
    fields={
        'answer': ('answer.json', file_data)
    }
)

print(request_post.status)
print(json.loads(request_post.data))
