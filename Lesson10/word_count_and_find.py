def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def find_words(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        wordCount = content.lower().count("the")
        print(wordCount)


filenames = ['hanselandgretel.txt', 'rapunzel.txt', 'the_raven.txt']
for filename in filenames:
    count_words(filename)
    find_words(filename)