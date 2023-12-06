from prompts import sentences as sen
import random as rd
import time
import keyboard
from colorama import Fore as f, Style


def check_key_press():
    print(f.LIGHTCYAN_EX + "\nPress any key to start typing...\n")
    keyboard.read_event(suppress=True)


def check_errors(prompt: str, u_prompt: str):
    error = []
    count = 0
    sub_count: float = 0
    prom = prompt.split()
    u_prom = u_prompt.split()
    if len(prom) != len(u_prom):
        miss = len(prom) - len(u_prom)
        for i in range(miss):
            u_prom.append("-missed/skipped word-")
    else:
        pass
    for p, u in zip(prom, u_prom):
        if p == u:
            continue
        else:
            for ps, us in zip(p, u):
                if ps == us:
                    continue
                else:
                    sub_count += 1/len(p)

            count += 1
            error.append(u)

    crct = len(prom) - count
    return crct, count, error, round(sub_count, 2)


while True:
    y = rd.choice(sen)
    print(f.LIGHTYELLOW_EX + "\n", y, "\n")
    check_key_press()
    start = time.time()
    x = input(f.GREEN + "\n>> : ")
    end = time.time()
    taken = round(end - start)
    correct_words, misspelled_words, errors, sub = check_errors(y, x)
    try:
        print(f"{f.CYAN}{sub}")
        print("\n"
              f"{f.BLUE}time taken : {taken}s\n"
              f"{f.GREEN}crct words: {correct_words}\n"
              f"{f.GREEN}wpm : {round((correct_words / (taken + sub)) * 60)} words per minute\n"
              f"{f.RED}errors: {errors}\n"
              f"{f.GREEN}Accuracy: {round((correct_words/(correct_words+misspelled_words)*100)-sub)}% \n"
              f"{f.RED}misspelled words: {misspelled_words}\n"
              f"{Style.RESET_ALL}")
    except ZeroDivisionError:
        print("\n"
              f"time taken : {taken}s\n"
              f"crct words: {correct_words}\n"
              f"wpm : 0 words per minute\n"
              f"errors: {errors}\n"
              f"Accuracy: {(correct_words/(correct_words+misspelled_words)*100)-sub}% \n"
              f"misspelled words: {misspelled_words}\n")
    while True:
        choice = input("Do you want to continue ? y/n : ").lower()
        if "y" == choice:
            break
        elif "n" == choice:
            exit()
        else:
            pass
