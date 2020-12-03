"""
--- Day 1: Report Repair ---

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

To begin, get your puzzle input.

Answer:
"""

input = [
1953,
2006,
1926,
1946,
1722,
1776,
1924,
1860,
2002,
1920,
1911,
1750,
1657,
2005,
1829,
1693,
1717,
1844,
1642,
1875,
1741,
1755,
1688,
1700,
1842,
1598,
1942,
1599,
1710,
1627,
1915,
1913,
1814,
1852,
1564,
1877,
1569,
1669,
2009,
1807,
1906,
1838,
1794,
1839,
1783,
1851,
1716,
1705,
1914,
1786,
1812,
1616,
1997,
1718,
1984,
1751,
1810,
1928,
1701,
1632,
1948,
616,
1981,
1878,
1903,
1690,
1836,
1631,
1649,
1562,
1707,
457,
1861,
1843,
979,
1605,
1652,
1596,
1730,
1560,
1886,
1802,
1614,
1929,
1570,
1907,
1950,
1969,
1629,
1769,
1575,
1932,
1983,
1781,
1954,
1663,
1644,
2004,
1772,
1044,
794,
1882,
1808,
1831,
1635,
1976,
1834,
1855,
1721,
1372,
1777,
1702,
1945,
1788,
1989,
1819,
1874,
1720,
787,
1806,
1966,
1949,
1694,
1752,
1887,
1687,
1943,
1665,
1774,
1645,
1900,
1661,
1968,
1706,
1586,
1977,
1691,
1991,
1870,
1865,
1764,
1967,
1714,
1594,
1429,
1647,
1858,
1805,
1561,
1895,
1559,
1988,
1565,
1799,
1862,
1578,
1664,
1816,
1628,
1960,
1775,
1746,
1324,
1835,
1658,
1918,
1671,
1957,
1864,
696,
1679,
254,
1017,
1622,
1601,
1592,
1782,
1767,
1825,
1655,
1784,
1896,
1965,
1600,
1963,
1840,
1749,
1970,
1980,
1936,
1685,
1790,
1902,
1729,
2001,
1638,
1986,
1879,
1847,
1866,
]

# Attempt at a one-pass O(n) solution

# We make a dictionary and iterate through the input
dict = {}
num1, num2 = 0,0
for value in input:
# If 2020 - value is already in the dictionary, then we have found our two numbers (the value we are at, and 2020 - value)
    if (2020 - value) in dict: # this is an efficient search since dictionaries allow for O(1) key lookups 
        num1 = value
        num2 = 2020 - value
# If not then we add the value as a key in the dictionary
    else:
        dict[value] = value
print(num1,num2,num1*num2)

# num1: 696
# num2: 1324
# answer = num1 * num2 = 921504 (correct!)

# Part 2

import itertools
import math

result = []
# we use itertools.combinations to make 3-tuples of the elements in input
for threeNums in itertools.combinations(input, 3):
    # then we check each 3-tuple to see if the elements add up to 2020
    if sum(list(threeNums)) == 2020:
        result = list(threeNums)
# finally we use math.prod to obtain the product of the three relevant elements
product = math.prod(result)
print(product)
# output: 195700142 (correct!)