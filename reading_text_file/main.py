# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    # [assignment] Add your code here
    file=open('story.txt', 'r')
    filename = file.read()
    file.close()
    print(filename)
    return(filename)

def count_words():
    text = read_file_content()
    # after reading the words, we split to individual words
    result = text.split()
    # the words are used to form a library
    count = dict()

    for result in result:
        if result in count:
            count[result] +=1
        else:
            count[result] =1
    print(count)
    return(result)
count_words()
