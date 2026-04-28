import sys

def shift_char(c, shift):
    # A–Z only
    if 'A' <= c <= 'Z':
        return chr(((ord(c) - ord('A') + shift) % 26) + ord('A'))
    return ''

def format_output(text):
    # split into blocks of 5
    blocks = [text[i:i+5] for i in range(0, len(text), 5)]

    # print 10 blocks per line
    for i in range(0, len(blocks), 10):
        print(" ".join(blocks[i:i+10]))

def main():
    # get shift from command line
    shift = int(sys.argv[1])

    # read stdin input
    message = sys.stdin.read()

    # clean + uppercase
    message = message.upper()

    result = ""

    for c in message:
        if 'A' <= c <= 'Z':
            result += shift_char(c, shift)

    format_output(result)

if __name__ == "__main__":
    main()
