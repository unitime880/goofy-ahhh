def most_frequent(list):
    return max(set(list), key = list.count)  

numbers = [140, 52, 51, 99, 88, 14, 777, 68594059685904, 3456765943045678, 68594034569789605, 68954034567765434]
most_frequent(numbers)
