print("--------TIYS 8-3--------------")
def shirtStats(size,message):
    print(f"Your shirt is size {size} with the message {message} printed on the front of it.")

shirtStats("medium","I love Python")
shirtStats("large","I love Python")
shirtStats("small","I love Python")

print("------------TIYS 8-4--------------")
def shirtStat(size, message=''):
    if message == '':
        if size=='medium':
            print("Your shirt is size medium with the message I love Python on the front of it")
        if size =='large':
            print("Your shirt is size large with the message with 'Hell0 W0rld' on the front of it")
        if size =='small':
            print("Your shirt is size small with the message with 'In a world where you can be anything, be kind' on the front of it")
    else:
        print(f"Your shirt is size {size} with the message {message} printed on the front of it.")
shirtStat('medium',)
shirtStat('large',)
shirtStat('small',)
