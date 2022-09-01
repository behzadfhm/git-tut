from random import randint

answer = randint(1, 10)
print(answer)
while True:
    try:
        guess = int(input('Please Enter a valid number between 1~10: '))
        if 0 < guess < 11:
            if guess == answer:
                print("You are Genuis!")
                break
        else:
            print("Please Choose your number between 1 to 10!")
    except ValueError:
        print('Please Enter a valid Number')
