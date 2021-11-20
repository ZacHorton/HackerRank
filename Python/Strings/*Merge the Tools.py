"""
Solution and explanation provided by FJSevilla on HackerRank
iter(s) returns an iterator for S.
[iter(s)]*n makes a list of n times the same iterator for s.
[] unpack a list:
zip make an iterator that aggregates elements from each of the iterables.
setdefault method returns the key value available in the dictionary and if given key is not available then it
    will provided default value and adds it to the dictionary.
"""


def merge_the_tools(string, k):
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
