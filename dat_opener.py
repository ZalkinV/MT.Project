import os
import functools
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


CONSOLE_WIDTH = os.get_terminal_size()[0]
FILE_PATH = Path("30019244.dat")
RESULT_PATH = Path("dat_results")
OUTPUT_DELIMETER = "".ljust(CONSOLE_WIDTH, "-")


def find_word(lines, word = "Ch0.Amp"):
    for line in lines:
        result = (str(line)).find(word)
        if (result != -1):
            print(result)
            print(line)
        print(OUTPUT_DELIMETER)

def print_chars(lines):
    for line in lines:
        bytes = bytearray(line)
        #chars = functools.reduce(lambda string, char: string + char, map(chr, bytes))
        for byte in bytes:
            print(chr(byte), end="")
        print(OUTPUT_DELIMETER)

def print_bytes(lines):
    for line in lines:
        print(line)
        print(OUTPUT_DELIMETER)

def find_longer_than(lines, length):
    longest_lines = []
    for index, line in enumerate(lines):
        cur_length = len(line)
        if (cur_length >= length):
            print(f"Line #{index}: lenght={cur_length}")
            longest_lines.append(line);
            #cur_pos = lines.tell();
            #begin_pos = cur_pos - cur_length;
            #longest_lines.append([begin_pos, cur_length])
    return longest_lines


def read_in_loop():
    with open(FILE_PATH, "rb") as file:
        for (index, line) in enumerate(file):
            print(index)


if __name__ == "__main__":
    file_content = open(FILE_PATH, "rb").readlines()
    longest_lines = find_longer_than(file_content, 100000)


    for (index, line) in enumerate(longest_lines):
        ints = np.frombuffer(line, dtype=np.int8)
        plt.plot(ints)
        #plt.savefig(RESULT_PATH / f"Line len={len(line)}")
        plt.close()


