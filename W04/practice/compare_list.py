def main():
    list1 = ["red", "orange", "yellow", "green", "blue"]
    list2 = ["red", "orange", "green", "green", "blue"]
    index = compare_lists(list1, list2)
    if index == -1:
        print("The contents of list1 and list2 are equal")
    else:
        print(f"list1 and list2 differ at index {index} => {list1[index]} : {list2[index]}")

def compare_lists(list1,list2):
    """Compare the contents of two lists. If the contents
    of the two lists are not equal, return the index of
    the first difference. If the contents of the two lists
    are equal, return -1.
    Parameters
        list1: a list
        list2: another list
    Return: an index or -1
    """
    # Get the length of the shortest list.
    length1 = len(list1)
    length2 = len(list2)
    limit = min(length1, length2)
    i = 0
    while i < limit:
        element1 = list1[i]
        element2 = list2[i]
        if element1 != element2:
            break
        i += 1
    if length1 == length2 == i:
        i = -1
    return i

if __name__ == "__main__":
    main()