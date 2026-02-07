def text_file_reader(filename):
    """Read the content of a text file into a list and 
    return a list. Each element of the list will contain 
    one line of text from the text file.
    Parameter filename: the name of the text file.
    Return: a list of strings
    """
    content_list = []
    with open(filename,"rt") as file:
        for elements in file:
            element = elements.strip()
            content_list.append(element)
    return content_list

def remove_first_element(_list,element_index=0):
    """Remove the first element from the list and return 
    the list without the first element.
    Parameter
        _list: the list that contain the element.
        element_index: the index of the element in the list
        that initiated to zero in this case.
    Return: a list without the first element
    """
    return _list.pop(element_index)

def remove_last_element(_list):
    """Remove the last element from the list and return 
    the list without the last element.
    Parameter _list: the list that contain the element
    Return: a list without the last element
    """
    return _list.pop()

def replace_selected_occurences(_list,_from,_to):
    """Replace all occurences of an element from the list to another 
    and return the list updated.
    Parameter
        _list: the list
        _from: the element to replace
        _to: the new element that replace the last one
    Return: a list updated
    """
    for i in range(len(_list)):
        if _list[i] == _from:
            _list[i] = _to
    return _list

def count_selected_occurences(_list,to_count):
    """Count the number of times that an occured element 
    appeared inside the list and return the count.
    Parameter
        _list: the list that contain the element to find
        to_count: the element to count
    Return: the number of times the element appeared
    """
    count = 0
    for _ in range(len(_list)):
        if _list[_] == to_count:
            count += 1
    return count

def main():
    # Open the provinces.txt file for reading.
    # Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
    provinces = text_file_reader("provinces.txt")
    # Print the entire list.
    print(provinces)
    # Remove the first element from the list.
    remove_first_element(provinces)
    print("After first element removed")
    print(provinces)
    # Remove the last element from the list.
    remove_last_element(provinces)
    print("After last element removed")
    print(provinces)
    # Replace all occurrences of "AB" in the list with "Alberta".
    replace_selected_occurences(provinces,"AB","Alberta")
    print("After replacing 'AB' by 'Alberta'")
    print(provinces)
    # Count the number of elements that are "Alberta" and print that number.
    count = count_selected_occurences(provinces,"Alberta")
    print(f"'Alberta' occurs {count} times in the modified list.")
    
if __name__ == "__main__":
    main()