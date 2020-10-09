#!/usr/bin/env python3

import sys
import re

CAESAR_KEY = -6


def main(args):
    rc = 0
    if not valid_input(args):
        usage()
        sys.exit(1)
    integers = list(map(int, [x for x in args[1].split(",")]))
    print(sum_test(integers))
    print(average_quotient_test(integers))
    print(even_integers_test(integers))
    print(smallest_position_test(integers))
    print(count_list_repeats_test(integers))
    print(new_16_bit_integer_test(integers))
    print(sort_test(integers))
    print(sort_transform_test(integers))
    print(sort_transform_filter_test(integers))
    print(caesar6_test(integers))
    characters = sort_transform_filter_helper(integers)
    print(f'** Caesar Encoded = {"".join(caesar_encoder(characters))}')
    sys.exit(rc)


def sum_test(integers):
    # Output #1: 941 (sum)
    return f"Output #1: {sum(integers)}"


def average_quotient_test(integers):
    # Output #2: 78,5 (average of the 12 values leaving an integer quotient, remainder)
    average = int(sum(integers) / len(integers))
    quotient = sum(integers) % average
    return f"Output #2: {average},{quotient}"


def even_integers_test(integers):
    # Output #3: 72,56,118 (even integers)
    return f'Output #3: {",".join([str(x) for x in integers if x % 2 == 0])}'


def smallest_position_test(integers):
    # Output #4: 56,6 (smallest, position)
    min_value = min(integers)
    # index starting at 1 rather than zero
    positions = [index + 1 for index, num in enumerate(integers) if num == min_value]
    positions = list(map(str, positions))
    return f'Output #4: {min_value},{",".join(positions)}'


def count_list_repeats_test(integers):
    # Output #5: 5,61,61,61,63,63 (#repeats, list)
    from collections import Counter

    histo = Counter(integers)
    singles_list = [num for num, count in histo.items() if count == 1]
    for num in singles_list:
        del histo[num]
    repeats_sum = sum([num for num in histo.values()])
    repeats_list = "".join(
        [(str(num) + ",") * count for num, count in sorted(histo.items())]
    )
    repeats_list = repeats_list.strip(",")
    return f"Output #5: {repeats_sum},{repeats_list}"


def new_16_bit_integer_test(integers):
    # Output #6: 18543 (value of new 16-bit integer)
    # ** the 1st 2 elements of the input data (72,111) are used to define a
    #    new 16-bit integer where 72 is the high byte and 111 the low byte
    answer = (integers[0] << 8) + integers[1]
    return f"Output #6: {answer}"


def sort_test(integers):
    # Output #7: 56,61,61,61,63,63,69,72,85,111,121 (sorted)
    sorted_ints = sorted(integers)
    return f'Output #7: {",".join(map(str, sorted_ints))}'


def sort_transform_test(integers):
    # Output #8: Ho?U=8vy=E?=
    # ** Hint: derived from Output #7
    return f'Output #8: {"".join(map(chr, integers))}'


def sort_transform_filter_test(integers):
    # Output #9: HOUVYE (upper case)
    characters = sort_transform_filter_helper(integers)
    return f'Output #9: {"".join(characters)}'


def sort_transform_filter_helper(integers):
    return [char.upper() for char in map(chr, integers) if re.match("[A-Za-z]", char)]


def caesar6_test(integers):
    # Output #10: Key (1 =<Key<=26)
    # ** “HOUVYE “(Output #9) is a coded word for “BIOPSY’ that has been encrypted
    #    using the Caesar Cipher. The Key unknown. Decipher “HOUVYE” to produce
    #    “BIOPSY’. Output #10 is the numerical value of Key.
    return f"Output #10: {CAESAR_KEY}"


def caesar_encoder(characters):
    # Prove the encoder works as expected.
    # input a list of characters
    # output a list of encoded characters
    ascii_offset = 64
    # first map from ordinal ascii values to 1-26 char_values
    char_values = [(num - ascii_offset) for num in list(map(ord, characters))]
    # encode with the key value
    encoded_values = list(map(lambda num: (num + CAESAR_KEY) % 26, char_values))
    # move back to the ascii range
    ascii_values = list(map(lambda num: num + ascii_offset, encoded_values))
    # return a list of encoded characters
    return list(map(chr, ascii_values))


def valid_input(args):
    if len(args) != 2:
        usage()
        return False
    return True


def usage():
    print("Usage:")
    print('    jims_challenge.py "<input list>"')
    print("Example:")
    print('    jims_challenge.py "72,111,63,85,61,56,118,121,61,69,63,61"')


if __name__ == "__main__":
    main(sys.argv)
