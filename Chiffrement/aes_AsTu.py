Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@astoumbengue
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


boppreh
/
aes
forked from bozhu/AES-Python
3
1371
 Code Issues 3 Pull requests 0 Actions Projects 0 Security Insights
Refactor new block cipher modes

 master (#2)
@boppreh
boppreh committed on 20 Oct 2019
1 parent c9f3132 commit 9a3296fa43c8f4023e510902dfb2c4dce0573940
Showing  with 19 additions and 35 deletions.
 54  aes.py 
@@ -136,8 +136,8 @@ def xor_bytes(a, b):

def inc_bytes(a):
    Returns a new byte array with the value increment by 1 """
    out = [v for v in a]
    for i in range(len(out)-1, -1, -1):
    out = list(a)
    for i in reversed(range(len(out))):
        if out[i] == 0xFF:
            out[i] = 0
        else:
@@ -166,8 +166,12 @@ def unpad(plaintext):
    assert all(p == padding_len for p in padding)
    return message

def split_blocks(message, block_size=16):
        assert len(message) % block_size == 0
        return [message[i:i+16] for i in range(0, len(message), block_size)]

class AES(object):

class AES:
    """
    Class for AES-128 encryption with CBC mode and PKCS#7.
@@ -274,9 +278,7 @@ def encrypt_cbc(self, plaintext, iv):

        blocks = []
        previous = iv
        # Splits in 16-byte parts.
        for i in range(0, len(plaintext), 16):
            plaintext_block = plaintext[i:i+16]
        for plaintext_block in split_blocks(plaintext):
            # CBC mode encrypt: encrypt(plaintext_block XOR previous)
            block = self.encrypt_block(xor_bytes(plaintext_block, previous))
            blocks.append(block)
@@ -293,9 +295,7 @@ def decrypt_cbc(self, ciphertext, iv):

        blocks = []
        previous = iv
        # Splits in 16-byte parts.
        for i in range(0, len(ciphertext), 16):
            ciphertext_block = ciphertext[i:i+16]
        for ciphertext_block in split_blocks(ciphertext):
            # CBC mode decrypt: previous XOR decrypt(ciphertext)
            blocks.append(xor_bytes(previous, self.decrypt_block(ciphertext_block)))
            previous = ciphertext_block
@@ -313,10 +313,8 @@ def encrypt_pcbc(self, plaintext, iv):

        blocks = []
        prev_ciphertext = iv
        prev_plaintext = bytes([0x00] * 16)
        # Splits in 16-byte parts.
        for i in range(0, len(plaintext), 16):
            plaintext_block = plaintext[i:i+16]
        prev_plaintext = bytes(16)
        for plaintext_block in split_blocks(plaintext):
            # PCBC mode encrypt: encrypt(plaintext_block XOR (prev_ciphertext XOR prev_plaintext))
            ciphertext_block = self.encrypt_block(xor_bytes(plaintext_block, xor_bytes(prev_ciphertext, prev_plaintext)))
            blocks.append(ciphertext_block)
@@ -334,10 +332,8 @@ def decrypt_pcbc(self, ciphertext, iv):

        blocks = []
        prev_ciphertext = iv
        prev_plaintext = bytes([0x00] * 16)
        # Splits in 16-byte parts.
        for i in range(0, len(ciphertext), 16):
            ciphertext_block = ciphertext[i:i+16]
        prev_plaintext = bytes(16)
        for ciphertext_block in split_blocks(ciphertext):
            # PCBC mode decrypt: (prev_plaintext XOR prev_ciphertext) XOR decrypt(ciphertext_block)
            plaintext_block = xor_bytes(xor_bytes(prev_ciphertext, prev_plaintext), self.decrypt_block(ciphertext_block))
            blocks.append(plaintext_block)
@@ -357,9 +353,7 @@ def encrypt_cfb(self, plaintext, iv):

        blocks = []
        prev_ciphertext = iv
        # Splits in 16-byte parts.
        for i in range(0, len(plaintext), 16):
            plaintext_block = plaintext[i:i+16]
        for plaintext_block in split_blocks(plaintext):
            # CFB mode encrypt: plaintext_block XOR encrypt(prev_ciphertext)
            ciphertext_block = xor_bytes(plaintext_block, self.encrypt_block(prev_ciphertext))
            blocks.append(ciphertext_block)
@@ -376,9 +370,7 @@ def decrypt_cfb(self, ciphertext, iv):

        blocks = []
        prev_ciphertext = iv
        # Splits in 16-byte parts.
        for i in range(0, len(ciphertext), 16):
            ciphertext_block = ciphertext[i:i+16]
        for ciphertext_block in split_blocks(ciphertext):
            # CFB mode decrypt: ciphertext XOR decrypt(prev_ciphertext)
            plaintext_block = xor_bytes(ciphertext_block, self.decrypt_block(prev_ciphertext))
            blocks.append(plaintext_block)
@@ -397,9 +389,7 @@ def encrypt_ofb(self, plaintext, iv):

        blocks = []
        previous = iv
        # Splits in 16-byte parts.
        for i in range(0, len(plaintext), 16):
            plaintext_block = plaintext[i:i+16]
        for plaintext_block in split_blocks(plaintext):
            # OFB mode encrypt: plaintext_block XOR encrypt(previous)
            block = self.encrypt_block(previous)
            ciphertext_block = xor_bytes(plaintext_block, block)
@@ -417,9 +407,7 @@ def decrypt_ofb(self, ciphertext, iv):

        blocks = []
        previous = iv
        # Splits in 16-byte parts.
        for i in range(0, len(ciphertext), 16):
            ciphertext_block = ciphertext[i:i+16]
        for ciphertext_block in split_blocks(ciphertext):
            # OFB mode decrypt: ciphertext XOR decrypt(previous)
            block = self.decrypt_block(previous)
            plaintext_block = xor_bytes(ciphertext_block, block)
@@ -439,9 +427,7 @@ def encrypt_ctr(self, plaintext, iv):

        blocks = []
        nonce = iv
        # Splits in 16-byte parts.
        for i in range(0, len(plaintext), 16):
            plaintext_block = plaintext[i:i+16]
        for plaintext_block in split_blocks(plaintext):
            # CTR mode encrypt: plaintext_block XOR encrypt(nonce)
            block = xor_bytes(plaintext_block, self.encrypt_block(nonce))
            blocks.append(block)
@@ -458,9 +444,7 @@ def decrypt_ctr(self, ciphertext, iv):

        blocks = []
        nonce = iv
        # Splits in 16-byte parts.
        for i in range(0, len(ciphertext), 16):
            ciphertext_block = ciphertext[i:i+16]
        for ciphertext_block in split_blocks(ciphertext):
            # CTR mode decrypt: ciphertext XOR decrypt(nonce)
            block = xor_bytes(ciphertext_block, self.decrypt_block(nonce))
            blocks.append(block)
0 comments on commit 9a3296f
@astoumbengue
 
 
Leave a comment

Attach files by dragging & dropping, selecting or pasting them.
 
 You’re not receiving notifications from this thread.
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
