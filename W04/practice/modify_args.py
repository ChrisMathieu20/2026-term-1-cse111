def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x} lx {lx}")
    modify_args(x, lx)
    print(f"After calling modify_args(): x {x} lx {lx}")

def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("\tmodify_args(n, alist)")
    print(f"\tBefore changing n and alist: n {n} alist {alist}")
    # Change the values of both parameters.
    n += 1
    alist.append(4)
    print(f"\tAfter changing n and alist: n {n} alist {alist}")

if __name__ == "__main__":
    main()