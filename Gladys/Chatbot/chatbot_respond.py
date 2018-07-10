#response to greetings
import random
def response_greetings(greeting):
    greeting_file=open("Greetings.txt", "r")
    lst_greet=[]
    for line in greeting_file:
        lst_greet.append(''.join(line.strip('\n').split('\n')))
    greeting_file.close()
    print(lst_greet)
    if greeting in lst_greet:
        return random.choice(lst_greet)
    else:
        return ("Whoops, try a greeting instead!")

greet=str(input("Welcome to MEDIChat! Type a greeting to start :): "))
print(response_greetings(greet))
