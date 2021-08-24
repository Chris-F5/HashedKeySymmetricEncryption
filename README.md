# Hashed Key Symmetric Encryption

Encrypts and decrypts files.

⚠ WARNING  ⚠: I can not guarantee that this encryption algorithm is cryptographically secure. Use at your own risk!

## Limitations
* If the attacker knows some bits of the plaintext file. They could modify an encrypted version of that file so that when its decrypted, the corrosponding bits of the decrypted file can be whatever the attacker wants them to be.
* The exact size of the plaintext file can be determined from the encrypted file.

## How it works

The user defined password is used to generate a key that is the same length as the input file. This is done by first hashing the password with SHA256 to get the first 256 bits of the key. Then, if the key is still to short, an SHA256 sum is calculated with the result of the previous hash as its input. The result of the new hash is appended to the generated bits. Once the key is longer than or equal to the length of the input file, excess bytes are removed from the key to make it the same size as the input file. Then the key is xored with the input file to produce the output file.

## Example
First lets create a plaintext file
```
[user@host test]$ echo "My secret plaintext" > plaintext.txt
```
Now we will encrypt this file with the password "pass123" and delete the plaintext file
```
[user@host test]$ python3 hkse.py plaintext.txt encrypted.hkse
Password: pass123
[user@host test]$ rm plaintext.txt 
```
If you view the encrypted file with `cat encrypted.hkse `, you will see that is looks like just a bunch of random bytes.

The encrypted file can be decrypted like so:
```
[user@host test]$ python3 hkse.py encrypted.hkse decrypted.txt
Password: pass123
[user@host test]$ cat decrypted.txt 
My secret plaintext
```

If the password is incorrect, the output file will conatin garbage.

Also note that the process of encrypting is the same as decrypting. This is because the algorithm is entirely symmetric.