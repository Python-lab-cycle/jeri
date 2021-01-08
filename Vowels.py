#From a list of vowels selected from a given word
word=input("Enter your sentence:")
for letter in word:
    if letter in 'aeiou':
        print(letter,end="")
        
