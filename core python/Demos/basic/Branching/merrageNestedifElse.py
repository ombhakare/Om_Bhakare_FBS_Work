gender = str(input("enter the gender (m/f):  "))
age = int(input("enter the age: "))

if(gender == 'male'):
    if(age >= 21):
        print('eligible for merrage')
    else:
        print('is not eligible for merrage')
else:
    if(age >= 18):
        print('is eligible for merrage')
    else:
        print('is not eligible for merrage')