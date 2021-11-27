# problem Take a word as input and count how many letters, how many vowels and how many consonants
a=input("Enter a word to count how many letters,vowels, and consonants");
vowels=0
letters=len(a)
consonants=0

for x in range a:
    if (x=='a'or x=='e' or x=='i' or x=='o' or x=='u' or
        x=='A' or x=='E' or x=='I' or x=='O' or x=='U'):
         vowels=vowels+1;
    else:
    consonants=consonants+1;

#now we will print 
print("the number of letters in your word is:",letters)
print("the number of vowels in your word is:",vowels) 
print("the number of consonants in your word is:",consonants) 


    
