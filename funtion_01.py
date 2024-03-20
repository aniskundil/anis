# def fasting(pious):
#     print(f'ramdan {pious.lower()}')
# fasting(input(''))   
# fasting('mubark')
# def phone_description(phone_type,model):
    # print(f' i have a {phone_type} phone')
    # print(f" my {phone_type}'s model is that of {model}")
# phone_description(input('what is your phone type:'),input('what year is it:'))
# 
# def shoe_type(brand, size):
# print(f'your shoe brand is {brand} and your shoesize {size}')
# shoe_type()
# 
# def nigeria(state,capital):
    # print(f'the capital of {state} is {capital}')
# nigeria(capital=input("put in your state's capital:"), state=input('put in the state:'))

# def pet_description(animal_type,pet_name):
#     print(f'n\i have a {animal_type}')
# #     print(f"n\my {animal_type}'s name is {pet_name}")
# pet_description('dog','billy')

# def make_shirt(size,text):
#     print(f' your shirt size is {size} and {text} is the text which will be print will be print on your shirt')
#make_shirt(int(input('what is your shirt size:')), input('what would you like to be printed on your shirt:'))

# def make_shirt():
#     size=int(input('what is your shirt size:'))
#     text=input('what would you like to be printed on your shirt:')
#     print(f' your shirt size is {size} and {text} is the text which will be printed on your shirt')
# make_shirt()



# def large_T_shirt(size='large', message='I love python'):
#     print(f'\nThe size of the shirt is {size} and the message printed is {message}')
# large_T_shirt()



# def median_shirt(size,message='i love python'):
#     print(f'\nThe size of the shirt is {size} and the message printed is {message}')
#median_shirt(size=input('what is you size:'))

def city(city, country='nigeria'):
    print(f'\n{city} city is in {country}')
city('kaduna')
city("kano")


def cleaned_name(first_name, last_name , middle_name):
    if middle_name:
        full_name=f'{first_name} {middle_name} {last_name}'
    
