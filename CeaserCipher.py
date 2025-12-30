from random import randint  # For generating random shift values
import pandas as pd  # For handling records in a DataFrame
import os # For checking file existence

file_path = "Projects\\CeaserCipher\\records.csv"

if os.path.exists(file_path): # Load existing records if file exists
    df = pd.read_csv(file_path)
else: # Initialize empty DataFrame if no file exists
    df = pd.DataFrame(columns=['orignaltext', 'encryptedtext', 'shift'])

def encrypt(text, shift):
    # Encrypt the text using Caesar cipher with the given shift
    global df
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)  # Encrypt uppercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)  # Encrypt lowercase letters
        else:
            result += char # Non-alphabetic characters remain unchanged

    new_row = {'orignaltext': text, 'encryptedtext': result, 'shift': shift}
    df.loc[len(df)] = new_row # Append new record to DataFrame
    df.to_csv(file_path, index=False) # Save DataFrame to CSV

    return result

def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65) # Decrypt uppercase letters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97) # Decrypt lowercase letters
        else:
            result += char  

    return result

def choice_check(choice):
    if choice == 1:
        text = input("Enter text to encrypt: ")
        shift = randint(1, 25)
        print("Encryption Successful!\nEncrypted text:", encrypt(text, shift))
    elif choice == 2:
        print("There are", len(df), "records available.") # Show available records
        for i in range(len(df)):
            print(f"{i+1}. {df.loc[i, 'encryptedtext']}")
        record_choice = int(input("Select a record number to decrypt: ")) - 1
        if 0 <= record_choice < len(df):
            encrypted_text = df.loc[record_choice, 'encryptedtext'] # Get encrypted text from selected record
            shift = df.loc[record_choice, 'shift']
            print("Decryption Successful!\nDecrypted text:", decrypt(encrypted_text, shift)) # Decrypt using stored shift value
        else:
            print("Invalid record number.")
    elif choice == 0:
        df.to_csv(file_path, index=False) # Save DataFrame to CSV
        print("Thank you for using the Ceaser Cipher program. Goodbye!")
        exit()
    
def main():
    choice = -1
    while choice != 0 : # Main loop
        print("""Make a choice:
1. Encrypt
2. Decrypt
0. Exit""")
        try:
            choice = int(input("Enter your choice: "))
            print("\n\n")
            if choice in [0, 1, 2]:
                choice_check(choice)
            else:
                print("Invalid choice. Please choose 0, 1, or 2.")    
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__" :
    main()
    

