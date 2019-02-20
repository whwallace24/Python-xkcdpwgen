import sys, getopt
import sqlite3, random

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def BuildPassword(words, caps, symbs, nums, lines):
    ret = ""
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "~", ".", ":", ";"]
    for i in range(words):
        n = random.randint(0, len(lines))
        word = lines[n]
        if "-" not in word and "&" not in word and "." not in word and "\'" not in word and " " not in word \
                and not hasNumbers(word):
            if caps == 0:
                ret += word.lower()
            elif caps > 0:
                word = word[0].capitalize() + word[1:]
                ret += word
                caps -= 1
            if symbs != 0:
                sym = random.randint(0, len(symbols) - 1)
                ret += symbols[sym]
                symbs -= 1
            if nums != 0:
                num = random.randint(0, 9)
                ret += str(num)
                nums -= 1
        else:
            i -= 1
    extra = ""
    while symbs > 0:
        sym = random.randint(0, len(symbols) - 1)
        extra += symbols[sym]
        symbs -= 1
    ret = extra + ret
    while nums > 0:
        num = random.randint(0, 9)
        ret += str(num)
        nums -= 1
    return ret

def main(argv):
    words = 4
    caps = 0
    symbs = 0
    nums = 0

    text_file = open("words.txt", "r")
    lines = text_file.read().split('\n')

    opts, args = getopt.getopt(argv, "hw:s:n:c:", ["help", "words=", "symbols=", "numbers=", "caps="])

    for opt, arg in opts:
        if opt == "-h" or opt == "--help":
            print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n"
                             "                \n"
                             "Generate a secure, memorable password using the XKCD method\n"
                             "                \n"
                             "optional arguments:\n"
                             "    -h, --help            show this help message and exit\n"
                             "    -w WORDS, --words WORDS\n"
                             "                          include WORDS words in the password (default=4)\n"
                             "    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words\n"
                             "                          (default=0)\n"
                             "    -n NUMBERS, --numbers NUMBERS\n"
                             "                          insert NUMBERS random numbers in the password\n"
                             "                          (default=0)\n"
                             "    -s SYMBOLS, --symbols SYMBOLS\n"
                             "                          insert SYMBOLS random symbols in the password\n"
                             "                          (default=0)\n")
            return 0
        elif opt == "-w" or opt == "--words":
            words = int(arg)
        elif opt == "-c" or opt == "--caps":
            caps = int(arg)
        elif opt == "-s" or opt == "--symbols":
            symbs = int(arg)
        elif opt == "-n" or opt == "--numbers":
            nums = int(arg)
        else:
            return 0
    print(BuildPassword(words, caps, symbs, nums, lines))



if __name__ == "__main__":
   main(sys.argv[1:])