#!/usr/bin/python3

import os
import sys
import datetime
import argparse
import pyAesCrypt
import getpass

parser.add_argument('-o', '--option', type=str, required=True, help="encrypt/decrypt")
parser.add_argument('-f', '--file', type=str, required=True, help='file path')
parser.add_argument('-b', '--buffer', type=int, required=False, help='define buffer size (by default 64)')
parser.add_argument

arg = parser.parse_args()


# --------------------------------------------------------------------------------------------------------
def encryptor(filename, password, bufferSize):      # recieves array of filenames and encrypt them
    try:
        pyAesCrypt.encryptFile(filename, filename + ".aes", password, bufferSize)
        print("encrypting...")

    except FileNotFoundError:
        print("file not found")
        sys.exit()

    except:
        print("Error encrypting file :(")
        if os.path.exists(filename + ".aes"):
            os.remove(filename + ".aes")
        sys.exit()

# --------------------------------------------------------------------------------------------------------
def decryptor(filename, password, bufferSize):
    try:
        output_name = filename.split(".aes")
        pyAesCrypt.decryptFile(filename, output_name[0], password, bufferSize)
        print("decrypting...")
    
    except ValueError:
        print("Password not valid or file is corrupted")
        sys.exit()

    except OSError:
        print("File not found")
        sys.exit()
    except:
        print("Error decrypting file :(")
        if os.path.exists(filename.split(".aes")):
            os.remove(filename.split(".aes"))
        sys.exit()

# -------------------------------------------------------------------------------------------------------
def getFileSize(filename):
    try:
        return os.stat(filename).st_size
    except:
        print("Couldn't get file size :( ")
        sys.exit()

# -------------------------------------------------------------------------------------------------------
def printEncryptOutput(filename):
    print(" ")
    print(f'File {filename} succesfully encrypted (' + str(datetime.datetime.now()) + ")" ) 
    print(" ")
    print(f'   Output File --> {filename}'+ ".aes")
    print("   File Size --> " + str(getFileSize(filename + ".aes")) + " bytes")
    print(" ")

# -------------------------------------------------------------------------------------------------------
def printDecryptOutput(filename):
    output_name = filename.split(".aes")
    print(" ")
    print(f'File {filename}' +  ' succesfully decrypted (' + str(datetime.datetime.now()) + ")")
    print(" ")
    print("  Output File --> " + str(output_name[0]))
    print("  File Size --> " +  str(getFileSize(filename)) + " bytes")
    print(" ")

# -------------------------------------------------------------------------------------------------------
def main():


    if arg.buffer == None:
        arg.buffer = 64
   
    file_path = os.path.split(arg.file)
    actual_path = os.getcwd()
    
    print(" ")
    password = getpass.getpass(prompt='Enter password to encrypt (no echo): ')
    
    if arg.option == "encrypt" or arg.option == "Encrypt":
        os.chdir(file_path[0])    
        encryptor(file_path[1], password, arg.buffer)
        printEncryptOutput(file_path[1])

    elif arg.option == "decrypt" or arg.option == "Decrypt":
        os.chdir(file_path[0])
        decryptor(file_path[1], password, arg.buffer)
        printDecryptOutput(file_path[1])

    else:
        print("bad arguments")
        sys.exit()

# ------- Calling main --------

try:
    main()

except KeyboardInterrupt:
    sys.exit()

