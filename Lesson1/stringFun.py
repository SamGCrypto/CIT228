# exercise 1 - use your own first and last name
print("---------------------------------")
print("exercise 1")
name = "Samuel Gorcyca"
print(name.title())
print(name.upper())
print(name.lower())
print("First initial is: ", name[0].upper())

#execise #2 - make up your own noun, adj, verb and ending
#use concatenation to create sentence1
#use an f-string to create sentence2
print("---------------------------------")
print("exercise 2")
noun = "monk"
adj = "tired"
verb = "yawned"
ending ="falling asleep"
sentence1 = "the " + adj + " little " + noun + " " + verb + " "+ ending
sentence2 = f"the {adj} little {noun} {verb} {ending}"
print(sentence1.upper())
print(sentence2.lower())
print("---------------------------------")
print("exercise 3")
noun = "fish"
adj = "swims"
ending = "very fast"
ending = "up the very"
sentence1 = "the " + noun + " " + adj + " " + verb + " "+ ending
sentence2 = f"the {noun} {adj} {verb} {ending}"
print(sentence1.upper())
print(sentence2.lower())
print("---------------------------------")
print("exercise 4")
color = ["red", "blue", "black", "green"]
fruit = ["strawberry", "blueberry", "blackberry", "kiwi"]
print(f"{color[0]} is the color of \t\t {fruit[0]}")
print(f"{color[1]} is the color of \t\t {fruit[1]}")
print(f"{color[2]} is the color of \t\t {fruit[2]}")
print(f"{color[3]} is the color of \t\t {fruit[3]}")