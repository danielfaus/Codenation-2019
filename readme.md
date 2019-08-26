# CODENATION Project 2019 - Caesar Cipher
Create a script program that requests the [**CODENATION**](https://www.codenation.dev) web site an
encrypted message, decrypt using **The Caesar Cipher** and posts the
message in a *JSON* file with hash calculated.

### Programming language choosed
I chose *Python* with the libraries *urllib3*, *json* and *hashlib*.
-   [**urllib3**](https://urllib3.readthedocs.io/en/latest/user-guide.html) to get and post methods.
-   [**json**](https://docs.python.org/3/library/json.html) to handle *JSON* files.
-   [**hashlib**](https://docs.python.org/3/library/hashlib.html) to calculate *hash*.

### Caesar Chiper
The Caesar cipher used replaces only the letters, keeping the numbers,
spaces, and punctuation. Using the ASCII table, replace the letters
with their correct position in the alphabet.

### Request and Post
When requesting the site, the script creates a JSON file with the
encrypted content and decryption key. Applying Caesar's Cipher, the
script decrypts the content and updates the JSON file, making it ready
for the post.

### Dependencies
The config.py file has three variables. Two are the URL for request and
post. The third is the individual token, which must be updated before
the script runs.

### Running
If all is right, the script requests create the JSON file, decrypts
the message and updates the file and sends it to the site.
