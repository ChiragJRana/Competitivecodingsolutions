from collections import Counter
import numpy as np
abc = np.array([1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,6,8,6,5,6,5,9,8,6,5,9,5,6])
cut_index = np.where(abc == np.amax(abc))
print(cut_index[0][0])
# print(counter)
# print(np.where(abc == 1)[0][0],np.where(abc == 1)[0][-1])
# def chg(chirag):
#     print(chirag)

# def main():
#     chirag = list('chirag')
#     chg(abc[:2])
#     print(chirag)

# if __name__ == '__main__':
#     main()
