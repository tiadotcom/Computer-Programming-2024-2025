# Write a function called cumsum that takes a list of numbers and returns the cumulative sum; 
# that is, a new list where the ith element is the sum of the first i + 1 elements from the original list.

def cumsum(t):
    cumulative_sum = []
    total = 0
    for num in t:
        total += num
        cumulative_sum.append(total)
    return cumulative_sum

t = [1, 2, 3]
print(cumsum(t))  
