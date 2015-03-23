text = input("enter your sentence\n")

counter = 0
text_copy = ""

#len of xxx == 26
#count ony letter of alphabet
#count only unique letters



alphabet = ('a' ,  'b' ,  'c' ,  'd' ,  'e' ,  'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z')
for letter in text:   
    if letter in alphabet:
        if letter not in text_copy:
            text_copy = text_copy + letter
            counter = counter +1

if counter == 26:
    print("it's a pangram")
else:
    print("it's not a pangram")

