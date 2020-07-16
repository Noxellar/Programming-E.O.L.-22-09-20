"""
    * A program to create vignere cipher text out of a plain text document
    * Also decodes vignere cipher text with given keyword
"""

import string as string


class encode_decode():
    def __init__(self, code_type, key, count, text_file, cipher_file):
        self.key = key
        self.count = count

        if code_type == "encode":
            self.encode()
        else:
            self.decode()

    def encode(self):
        self.cipher_text = []

        for i in text_file:
            for l in i:
                if l in string.ascii_letters:
                    if l in string.ascii_lowercase:
                        self.letter_index = string.ascii_lowercase.index(l)
                        self.cipher_index = string.ascii_lowercase.index(
                            key[self.count])
                        for n in range(self.cipher_index):
                            if self.letter_index + 1 > 25:
                                self.letter_index = 0
                            else:
                                self.letter_index += 1
                        self.cipher_text.append(
                            string.ascii_lowercase[self.letter_index])
                    elif l in string.ascii_uppercase:
                        self.letter_index = string.ascii_uppercase.index(l)
                        self.cipher_index = string.ascii_lowercase.index(
                            key[self.count])
                        for n in range(self.cipher_index):
                            if self.letter_index + 1 > 25:
                                self.letter_index = 0
                            else:
                                self.letter_index += 1
                        self.cipher_text.append(
                            string.ascii_uppercase[self.letter_index])
                    if self.count + 1 > len(key) - 1:
                        self.count = 0
                    else:
                        self.count += 1
                else:
                    self.cipher_text.append(l)

        self.cipher_string = "".join(self.cipher_text)
        cipher_file.write(self.cipher_string)
        cipher_file.close()
        text_file.close()

    def decode(self):
        self.decode_text = []

        for i in cipher_file:
            for l in i:
                if l in string.ascii_letters:
                    if l in string.ascii_lowercase:
                        self.letter_index = string.ascii_lowercase.index(l)
                        self.decode_index = string.ascii_lowercase.index(
                            key[self.count])
                        for n in range(self.decode_index):
                            if self.letter_index - 1 < 0:
                                self.letter_index = 25
                            else:
                                self.letter_index -= 1
                        self.decode_text.append(
                            string.ascii_lowercase[self.letter_index])
                    elif l in string.ascii_uppercase:
                        self.letter_index = string.ascii_uppercase.index(l)
                        self.decode_index = string.ascii_lowercase.index(
                            key[self.count])
                        for n in range(self.decode_index):
                            if self.letter_index - 1 < 0:
                                self.letter_index = 25
                            else:
                                self.letter_index -= 1
                        self.decode_text.append(
                            string.ascii_uppercase[self.letter_index])
                    if self.count + 1 > len(key) - 1:
                        self.count = 0
                    else:
                        self.count += 1
                else:
                    self.decode_text.append(l)

        self.decode_string = "".join(self.decode_text)
        text_file.write(self.decode_string)
        text_file.close()
        cipher_file.close()


if __name__ == "__main__":
    code_type = input("Encode or Decode? [encode|decode]: ")

    while True:
        if code_type in ["encode", "decode"]:
            key = input("Key: ")
            key = key.lower()
            for i in key:
                if i not in string.ascii_letters:
                    key = key[:key.index(i)] + key[key.index(i) + 1:]

            count = 0

            if code_type == "encode":
                text_file = open(
                    "/home/harryl/Desktop/Programming/Python/Vignere Cipher/text.txt", "r")
                cipher_file = open(
                    "/home/harryl/Desktop/Programming/Python/Vignere Cipher/cipher.txt", "w")
            elif code_type == "decode":
                text_file = open(
                    "/home/harryl/Desktop/Programming/Python/Vignere Cipher/text.txt", "w")
                cipher_file = open(
                    "/home/harryl/Desktop/Programming/Python/Vignere Cipher/cipher.txt", "r")

            encode_decode = encode_decode(
                code_type, key, count, text_file, cipher_file)

            break
        else:
            code_type = input("Please enter valid choice. [encode|decode]: ")
