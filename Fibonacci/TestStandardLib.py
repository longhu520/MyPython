import os
# os.getcwd()
# os.system('ls -trl')
# dir(os)
# help(os)

import glob
# print(glob.glob('*.py'))

import sys
# print(sys.argv)
# sys.stderr.write('Warning, log file not found starting a new one\n')
# sys.stdout.write('Warning, log file not found starting a new one\n')

import re
# print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

import math
# print(math.cos(math.pi/3))
# print(math.log(64,2))

import random
# print(random.choice(['apple', 'orange', 'tomato']))
# print(random.sample(range(100),10))
# print(random.random())
# print(random.randrange(10))

import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))

# from urllib.request import urlopen
# with urlopen('https://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
#     for line in response:
#         line = line.decode('utf-8')
#         if 'EST' in line or 'EDT' in line :
#             print(line)


# from datetime import date
# now = date.today()
# print(now)
#
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
#
# birthday = date(1963, 12, 6)
# age = now - birthday
# print(age.days/365)

# import zlib
# s = b'witch which has which witches wrist watch'
# print(zlib.crc32(s))
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# z = zlib.decompress(t)
# print(len(z))
# print(zlib.crc32(z))


def average(values) :
    """
    :param values:
    :return: int

    Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
print(doctest.testmod())