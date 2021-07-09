"""
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
    letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?
"""

dict_ = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

length = 0

for num in range(1, 1000):
    num_str = str(num)
    if dict_.get(num):
        length += len(dict_[num])
    else:
        if len(num_str) > 2:
            length += len(dict_[int(num_str[0])] + 'hundred')
            if num_str[-2:] != '00':
                length += len('and')
        if int(num_str[-2:]) <= 20:
            length += len(dict_[int(num_str[-2:])])
        else:
            length += len(dict_[int(num_str[-2]) * 10] + dict_[int(num_str[-1])])
    # if num // 100:
    #     length += len(dict_[num // 100] + 'hundred')
    #     if num % 100:
    #         length += len('and')
    # length += len(dict_[(num % 100) // 10 * 10] + dict_[num % 10])

length += len('onethousand')

print(length)
