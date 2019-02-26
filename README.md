Author: Edwin Aramburo
Date: 2/25/19


*This program will decrypt your sha1 hash and tell you what your password,
if the password is not in the database then the text Password not in database
will appear*

Make sure the PASSWORD_LIST LOCATION is correct, it should be something like:
/Users/User_name/Downloads/file_name


To decrypt a normal sha1 hash run the python script in terminal, by inputing:
python "file_location" hash null

To decrypt a salted sha1 hash run the python script in terminal, by inputing:
python "file_location" salt_term salt_hash

** There will be a time delay in between the decryption of the salt and the
salted_hash so that the user can see the results briefly

import hashlib:
is a library to encrypt string using hashlib.sha1 line 46, 95

import sys:
allows the arguments to get passed on the terminal and variables we assigned to
each argument line 34,35

import time:
Used to keep track of time when the decryption is happening line 52
Allows the time delay that was discussed earlier in the document line 84