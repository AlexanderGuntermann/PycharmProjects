# function takes a list as a parameter
def permute_string(word):
    # empty results list we will append to later
    results = []
    # if the length is zero, return an empty list
    if len(word) == 0:
        return []
    # if the length of the word is 1, return the word in the list
    if len(word) == 1:
        return [word]

    # loop from i to the length of the word
    for i in range(len(word)):
        # first character of the word
        firstLetter = word[i]
        # the rest of the word minus the first letter achieved by string slicing
        remainingLetters = word[:i] + word[i+1:]
        # loop for every time the permutation is called on the word minus the first character
        for j in permute_string(remainingLetters):
            # append the first letter plus the recursive result
            results.append([firstLetter]+j)
    return results

# printing loops for every example from the assignment
example_four = list("a")
for x in permute_string(example_four):
    print(x)
    print("")
example_two = list("ab")
for k in permute_string(example_two):
    print(k)
print("")
example_three = list("aabb")
for n in permute_string(example_three):
    print(n)
print("")
example = list("hello")
for j in permute_string(example):
    print(j)






