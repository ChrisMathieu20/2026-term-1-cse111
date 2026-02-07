import csv

def read_dictionary(filename,key_column_index):
    """Read the content of a CSV file and return a dictionary.
    Parameter filename: the name of the file to read
    Return: a dictionary
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)
        for row_list in reader:
            key_value = row_list[key_column_index]
            dictionary[key_value] = row_list
    return dictionary

def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    students = read_dictionary("students.csv",KEY_INDEX)
    inumber = input("Please enter an ID Number (xxxxxxxxx): ")
    inumber = inumber.replace("-","")
    if not inumber.isdigit():
        print("Invalid I-Number")
    elif len(inumber) != 9:
        if len(inumber) < 9:
            print("Invalid ID Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid ID Number: too many digits")
    else:
        if inumber in students:
            student = students[inumber]
            name = student[NAME_INDEX]
            print(f"The student's name is {name}")
        else:
            print("No such student")

if __name__ == "__main__":
    main()