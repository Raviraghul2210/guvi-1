r=input()
if(r>='a' and r<='z'):
    l=['a','e','i','o','u']
    if r in l:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Invalid')
