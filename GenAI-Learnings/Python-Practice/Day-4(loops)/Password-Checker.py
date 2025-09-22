special_chars = "!@#$%^&*()-_=+[]{}\\|;:'\",.<>/?`~"
while True:
    pwd = input("Enter password: ")
    length_ok = False
    digit_ok = False
    special_ok = False
    count = 0
    for _ in pwd:
        count += 1
    if count >= 8:
        length_ok = True
    for ch in pwd:
        if '0' <= ch <= '9':
            digit_ok = True
        i = 0
        while i < len(special_chars):
            if ch == special_chars[i]:
                special_ok = True
                break
            i += 1
        if digit_ok and special_ok:
            break
    if length_ok and digit_ok and special_ok:
        print("Password accepted — meets all strength requirements.")
        break
    else:
        print("Password rejected. Issues found:")
        if not length_ok:
            print(" - Must be at least 8 characters.")
        if not digit_ok:
            print(" - Must contain at least one digit (0-9).")
        if not special_ok:
            print(" - Must contain at least one special character (e.g. !,@,#,$,%).")
        print("Please try again.\n")
