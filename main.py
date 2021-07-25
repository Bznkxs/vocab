import pandas as pd
import random
import json
from non_blocking import getch, kbhit
from time import time
import math
vocab = pd.read_csv('vocab.csv', header=None)

try:
    with open("stats.json", 'r') as fp:
        stats = json.load(fp)
except FileNotFoundError:
    stats = {}


def shuffle_test():
    # pick words randomly
    n = len(vocab)
    l_w = []
    for i in range(n):
        word = vocab.iloc[i, 0]
        if word not in stats:
            stats[word] = {"c": 0, "la": 0}  # c: time of continuous correct; la: last appearance
        stats[word]['la'] += 1
        if stats[word]['c'] <= stats[word]['la']:
            stats[word]['la'] = 0
            l_w.append(i)

    random.shuffle(l_w)
    while l_w:
        fails = []
        for p, i in enumerate(l_w):
            word = vocab.iloc[i, 0]
            print(f"{p+1}/{len(l_w)}:", word)
            t_start = time()

            time_limit = 10
            refresh_interval = 1
            t_refresh = time() - refresh_interval
            timeout = True
            while time() - t_start < time_limit:
                if kbhit():
                    getch()
                    timeout = False
                    break
                if time() - t_refresh >= refresh_interval:
                    t_refresh = time()
                    print(math.ceil(time_limit - (time() - t_start)), "second(s) left   \n\033[A", end='', flush=True)

            print('pronunciation hint:', vocab.iloc[i, 1])
            print('def:', vocab.iloc[i, 2])
            print('notable examples:', vocab.iloc[i, 3])
            if timeout:
                print("Timeout. Count as a wrong. Enter to continue.")
                input()
                print("\n\n\n")
                x = 'n'
            else:
                print("Got that? Y/n", flush=True)
                x = input()
                print(x, '\n\n')
            if x.lower() == 'n':
                fails.append(i)
                stats[word]['c'] = -1
            else:
                stats[word]['c'] += 1  # zeros be the wrong words

        l_w = fails
        random.shuffle(l_w)
    with open("stats.json", 'w') as fp:
        json.dump(stats, fp)

if __name__ == '__main__':
    shuffle_test()
