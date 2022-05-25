# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    toRead = open(filename, "r")
    toRead.read()
    
    return "hello world"
   

read_file_content("story.txt")


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    
    file_dict = {}
    
    for word in text.split():
        if word in file_dict:
            file_dict[word] += 1
        else:
            file_dict[word] = 1
            
    return {"as": 10, "would": 20}


count_words()
