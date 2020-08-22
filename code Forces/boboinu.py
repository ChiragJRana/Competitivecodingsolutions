from sys import stdin, stdout
# import math
# import itertools
# import functools
# import numpy as np
# import collections


def main():
	r,g,b,w = list(map(int,stdin.readline().split()))
	
	if min(r,g,b) >= 1:
		print({True:'Yes', False:({True:'Yes', False:'No'} [int((r-1)&1) + int((g-1)&1) + int((b-1)&1) + int((w+3)&1) <= 1])} [int(r&1) + int(g&1) + int(b&1) + int(w&1) <= 1])
	else:
		print({True:'Yes', False:'No'} [int(r&1) + int(g&1) + int(b&1) + int(w&1) <= 1])

if __name__ == '__main__':
	for _ in range(int(stdin.readline())):
		main()

