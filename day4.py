"""
Day 4 - Password recovery

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 197487-673251.
"""


#PART1

START_PASS = 197487
END_PASS = 673251
PASSWORD_LEN = 6


def check_len(password: str):
    return len(password) == PASSWORD_LEN


def check_range(password: str):
    return START_PASS <= int(password) <= END_PASS


def check_adjacent_digs(password: str):
    any_adj = False

    for i in range(0, len(password) - 1):
        any_adj = any_adj or password[i] == password[i+1]

    return any_adj


def check_increasing(password: str):
    incr_flag = True

    for i in range(0, len(password) - 1):
        incr_flag = incr_flag and password[i] <= password[i+1]

    return incr_flag

#PART1
possible_passwords = 0
for x in range(START_PASS, END_PASS):
    i = str(x)
    if check_adjacent_digs(i) and check_increasing(i):
        possible_passwords += 1

print(possible_passwords)


#PART2

def check_any_2seq(password: str):
    i = 0

    while i < len(password):
        curr_seq = password[i]
        seq_count = 1
        i += 1

        while i < len(password) and password[i] == curr_seq:
            seq_count += 1
            i += 1

        if seq_count == 2:
            return True
    return False


possible_passwords = 0
for x in range(START_PASS, END_PASS):
    pwd = str(x)
    if check_adjacent_digs(pwd) and check_increasing(pwd) and check_any_2seq(pwd):
        possible_passwords += 1

print(possible_passwords)


# 719 is too low
# 747 is too low
# 966 is too low
# 1126
