import sys

if len(sys.argv) != 2:
    print("Usage: python palindrome_check.py <word>")
    sys.exit(1)

word = sys.argv[1].lower().replace(" ", "")

if word == word[::-1]:
    print("Palindrome")
    sys.exit(0)
else:
    print("Not a palindrome")
    sys.exit(1)
