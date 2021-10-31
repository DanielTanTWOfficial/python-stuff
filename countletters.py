'''
    this program takes a string from the user and prints the number of times
    each character appears in the string.
'''

def main():
    countme = ''
    letterCount = {}
    
    countme = input("Enter a string: ")
    
    for letter in countme:
        # if the letter has not been counted, add to dictionary
        if letter not in letterCount:
            letterCount[letter] = 1
        # if the letter exists in the dictionary, +1 to its count
        else:
            letterCount[letter] = letterCount[letter] + 1
    
    print("The number of times each character in the string appears is as follows: ")
    
    for key, value in letterCount.items():
        print("{}: {}".format(key, value))
        
    

if __name__ == '__main__':
	main()