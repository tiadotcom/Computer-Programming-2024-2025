# Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all of the nested lists. 

def nested_sum(t):
    result = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            result += t[i][j]
    return result

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))

