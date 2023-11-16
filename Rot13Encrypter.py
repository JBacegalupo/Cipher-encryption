from sys import argv
def rot13(file):
    Capital = False
    CurrentChar = ""
    FinalString = ""
    alphanumericstring = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for index , lines in enumerate(file.readlines()):
        print(index)
        FinalString = ""
        for chars in lines:
            if not chars.isalnum():
                FinalString = FinalString + chars
                continue
            indexnum = alphanumericstring.find(chars)
            if alphanumericstring[indexnum].isupper(): Capital = True
            else: Capital = False
            if 52 - (indexnum + 13) < 0:
                currentChar = alphanumericstring[abs(52 - (indexnum + 13))]
            else:
                currentChar = alphanumericstring[indexnum + 13]
            if Capital:
                FinalString = FinalString + currentChar.upper()
            else:
                FinalString = FinalString + currentChar.lower()
    writetofile(FinalString)

def writetofile(EncryptedString):
    EncryptedString = str(EncryptedString)
    filepath = "P:\My Documents\Rot13Encyption.txt"
    encrpytedfile = open(filepath,"w")
    for line in EncryptedString:
        encrpytedfile.writelines(line)
    encrpytedfile.close()
def filehandler(filepath):
    try:
        f = open(filepath)
        return f
    except:
        print("filepath is not valid")
        exit()


if __name__ == '__main__':
    writetofile(rot13(filehandler(argv[1])))



