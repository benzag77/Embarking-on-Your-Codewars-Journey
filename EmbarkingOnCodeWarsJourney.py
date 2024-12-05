#Even or odd

number = int(input("Enter a number: "))

def even_odd(number):

    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."
    
print(even_odd(number))

#Convert a Number to a String

def number_to_string(num):

    return str(num)

num = 123

print(number_to_string(num))
print(type(num))

#Vowel Count

def get_count(sentence):

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0 

    for chr in sentence:
        if chr in vowels:
            count += 1
    return count

sentence = "a given string"
print(f'There are {get_count(sentence)} vowels in the string.')