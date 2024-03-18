class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        plaintext = plaintext.replace(" ", "").upper()

        num_columns = len(self.key)

        num_rows = -(-len(plaintext) // num_columns)  # Equivalent to math.ceil

        transposition_grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

        for i, char in enumerate(plaintext):
            row = i // num_columns
            col = i % num_columns
            transposition_grid[row][col] = char

        encrypted_message = ''
        for col_index in self.key:
            col_index -= 1  
            encrypted_message += ''.join(transposition_grid[row][col_index] for row in range(num_rows))

        return encrypted_message

    def decrypt(self, encrypted_message):
        num_columns = len(self.key)

        num_rows = len(encrypted_message) // num_columns

        transposition_grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

        col_index = 0
        for key_value in self.key:
            key_index = key_value - 1  # Adjust key values to start from 0
            for row_index in range(num_rows):
                transposition_grid[row_index][key_index] = encrypted_message[col_index]
                col_index += 1

        decrypted_message = ''
        for row in transposition_grid:
            decrypted_message += ''.join(row)

        return decrypted_message



key = [3, 1, 4, 2] 
transposition_cipher = TranspositionCipher(key)

plaintext_message = "This is a message for showing"
encrypted_message = transposition_cipher.encrypt(plaintext_message)
print("Plaintext:", plaintext_message)
print("Encrypted:", encrypted_message)

decrypted_message = transposition_cipher.decrypt(encrypted_message)
print("Decrypted:", decrypted_message)

