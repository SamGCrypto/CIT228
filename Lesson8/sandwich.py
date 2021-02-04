def make_sandwich(*sandwichToppings):
    for a in sandwichToppings:
        print(f"--{a}")

make_sandwich('Cheese','Peppers','Tomato','Pasta','Bacon','Lettuce')
make_sandwich('Cheese','Peppers','Tomato','Pasta')
make_sandwich('Bacon','Lettuce')
