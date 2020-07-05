#9.Write a binary search function. It should take a sorted sequence and the item it is looking for. 
# It should return the index of the item if found.
# It should return -1 if the item is not found.


import math


def search_item(sequence, item):
    
    mid_value = math.ceil(len(sequence) / 2)
    
    if item == sequence[mid_value]:
        return sequence.index(item)
    else:
        try:
            if item > sequence[mid_value]:
                return search_item(sequence[mid_value:], item)
            elif item < sequence[mid_value]:
                return search_item(sequence[:mid_value], item)

        except IndexError:
            return -1

seq=range(50,150)

result = search_item(seq, 52)
print(result)