import random
import time


def get_random_num(min_rand, max_rand):
    return random.randint(min_rand, max_rand)


def get_underscore_list(original_list):
    str_underscord = ''
    for l in original_list:
        str_underscord += '_'*len(l)
        str_underscord += ' '

    return str_underscord

def get_arr_in_str(original_list):
    str_list = ''
    for l in original_list:
        str_list += l
        str_list += ' '

    return str_list


def replace_char(underscore_str, str_list, input_str):
    print(underscore_str)
    is_gas = False
    for index, s in enumerate(str_list):
        if input_str == s:
            underscore_str = underscore_str[:index] + s + underscore_str[index + 1:]
            str_list = str_list[:index] + " " + str_list[index + 1:]

            is_gas = True

    return underscore_str, str_list, score, is_gas


lists_in_list = [['Act', 'as', 'if'], ['Act', 'withouttattt', 'expectation'], ['All', 'is', 'well'],
                 ['Allow', 'for', 'delays'], ['Always', 'be', 'honest'],
                 ['Always', 'be', 'yourself'], ['Always', 'deliver', 'quality'], ['Ask', 'powerful', 'questions'],
                 ['Audit', 'your', 'metrics'], ['Audit', 'your', 'mistakes']]

random_num = get_random_num(1, len(lists_in_list) - 1)
print(random_num)
underscore_str = get_underscore_list(lists_in_list[random_num])
str_list = get_arr_in_str(lists_in_list[random_num])

print(f"underscore_str : {underscore_str}")
print(f"str_list : {str_list}")

start_time = time.time()

print(underscore_str)
input_str = input("please enter str")
score = 0
while input_str != "exit" and '_' in underscore_str:
    underscore_str, str_list, score, is_gas = replace_char(underscore_str, str_list, input_str)
    if is_gas:
        score += 5
    else:
        score -= 1
    print(f"[{underscore_str}]")
    print(f"Your score is {score} points")
    if not '_' in underscore_str:
        break
    input_str = input("please enter str")
    if input_str in underscore_str:
        continue
current_time = time.time() - start_time
if current_time < 30.0 and input_str != 'exit':
    print(current_time)
    score += 30

print(f"Your score is {score} points")
