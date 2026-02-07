import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")
    append_random_numbers(numbers)
    print(f"numbers {numbers}")
    append_random_numbers(numbers,3)
    print(f"numbers {numbers}")
    words = ["join", "love", "smile", "love", "cloud", "head", "laugh"]
    append_random_words(words,5)

def append_random_numbers(numbers_list,quantity=1):
    for _ in range(quantity):
        rand_num = random.uniform(0,100)
        num = round(rand_num,1)
        numbers_list.append(num)

def append_random_words(words_list,quantity=1):
    print()
    for _ in range(quantity):
        rand_wds = random.choice(words_list)
        print(rand_wds)

if __name__ == "__main__":
    main()