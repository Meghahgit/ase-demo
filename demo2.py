def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Hardcoded string to check
word = "madam"

# Check and print result
if is_palidrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
