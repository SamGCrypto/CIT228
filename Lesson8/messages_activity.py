def show_messages(messages, emptyMsg):
    while messages:
        current_msg= messages.pop()
        print(current_msg)
        emptyMsg.append(current_msg)
 
def print_all(test):
    for i in test:
        print(i)

mesSend=['Hello thank you for texting','Hell0 W0rld','Python is weird']
emptyList=[]
print("Original List")
print_all(mesSend)
print("Transfer list")
print_all(emptyList)

show_messages(mesSend, emptyList)

print("Original List")
print_all(mesSend)
print("Transfer list")
print_all(emptyList)
