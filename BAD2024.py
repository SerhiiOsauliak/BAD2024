with open('C:\\Users\\osaul\\Downloads\\10m.txt', 'r') as file:
    data = [int(line.strip()) for line in file]

max_value = max(data)
min_value = min(data)

data.sort()
num = len(data)
if num % 2 == 0:
    median_value = (data[num // 2 - 1] + data[num // 2]) / 2
else:
    median_value = data[num // 2]

average_value = sum(data) / num


def find_longest_subsequence(lst, increasing=True):
    longest_subsequence = []
    current_subsequence = []
    for i in range(len(lst) - 1):
        if (increasing and lst[i] < lst[i + 1]) or (not increasing and lst[i] > lst[i + 1]):
            current_subsequence.append(lst[i])
        else:
            current_subsequence.append(lst[i])
            if len(current_subsequence) > len(longest_subsequence):
                longest_subsequence = current_subsequence
            current_subsequence = []
    current_subsequence.append(lst[-1])
    if len(current_subsequence) > len(longest_subsequence):
        longest_subsequence = current_subsequence
    return longest_subsequence


longest_increasing_subsequence = find_longest_subsequence(data)
longest_decreasing_subsequence = find_longest_subsequence(data, increasing=False)

print('Maximum value:', max_value)
print('Minimum value:', min_value)
print('Median value:', median_value)
print('Average value:', average_value)
print('Longest_increasing_subsequence:', longest_increasing_subsequence)
print('Longest_decreasing_subsequence:', longest_decreasing_subsequence)
