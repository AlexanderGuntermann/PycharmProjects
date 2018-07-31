# empty list that holds the results
results = []
def permute_string(prefix,word):
    # length of the string
    n = len(word)
    # if the length of the string is 0 then return it
    if n == 0:
        results.append(prefix)
    # if the length is greater than 0, then:
    else:
        for i in range(n):
            # first letter
           letter= word[i]
            # remaining letters in the word minus the first one
           remainingLetters = word[:i] + word[i+1:]
            # recursive call
           permute_string(prefix+letter,remainingLetters)

# method call for the prefix and the string
permute_string("","hello")

# prints out the words in a list
print(results)

