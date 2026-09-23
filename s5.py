text = input ("enter a sentence : ")

word = input("enter a word to search :")

print("uppercase:",  text.upper())
print("lowercase :", text.lower())

print("number of times word occurs :", text.count(word))

if word in text :
    print("the word exist in the sentence.")
else :
    print("the word does not exist .")

old_word = input("enter word to replace :")
new_word = input("enter new word")

new_text = text.replace(old_word, new_word)

print("modified text :", new_text)
