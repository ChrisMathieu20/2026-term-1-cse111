LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word,filename,case_sensitive=False):
    with open(filename, "r",encoding="utf-8") as file:
        is_in_file = False
        for lists in file:
            list = lists.strip()
            if word == list:
                is_in_file = True
    return is_in_file

def word_has_character(word,character_list):
    has_character = False
    for letter in word:
        if letter in character_list:
            has_character = True
    return has_character

def word_complexity(word):
    lower = word_has_character(word,LOWER)
    upper = word_has_character(word,UPPER)
    digits = word_has_character(word,DIGITS)
    special = word_has_character(word,SPECIAL)
    complexity = 0
    if lower:
        complexity += 1
    if upper:
        complexity += 1
    if digits:
        complexity += 1
    if special:
        complexity += 1
    return complexity

def password_strength(password,min_length=10,strong_length=16):
    is_dictionary_word = word_in_file(password,"wordlist.txt")
    is_common_password = word_in_file(password,"toppasswords.txt",True)
    complexity = word_complexity(password)
    strength = 0
    if is_dictionary_word:
        value = 0
        strength *= value
        print(f"Strength: {strength} -- Password is a dictionary word and is not secure.")
    elif is_common_password:
        value = 0
        strength *= value
        print(f"Strength: {strength} -- Password is a commonly used password and is not secure.")
    elif len(password) < min_length:
        value = 1
        strength += value
        print(f"Strength: {strength} -- Password is too short and is not secure.")
    elif (len(password) >= min_length) and (len(password) < strong_length):
        value = complexity + 1
        strength += value
        print(f"Strength: {strength}")
    elif len(password) >= strong_length:
        value = 5
        strength += value
        print(f"Strength: {strength} -- Password is long, length trumps complexity this is a good password.")

def main():
    is_quit = False
    while not is_quit:
        user_entry = input("Enter your password: type [Q] or [q] to quit -- ")
        if user_entry == "q" or user_entry == "Q":
            print("Have a nice day.")
            is_quit = True
        else:
            password_strength(user_entry)
            is_quit = False

if __name__ == "__main__":
    main()