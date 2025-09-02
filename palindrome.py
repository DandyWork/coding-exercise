def is_palindrome(word):          # Define a function called is_palindrome that takes one parameter "word"
    reversed_word = word[::-1]    # Reverse the string using slicing, word[start:stop:step], not mentioning start and stop will take a whole world , for step if negative means its reading right to left 
    return word == reversed_word  # Compare original and reversed, return True if they are equal, otherwise False

print(is_palindrome("madam"))   # True (because "madam" backwards is "madam")
print(is_palindrome("hello"))   # False (because "hello" backwards is "olleh")
