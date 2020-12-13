"""For this challenge:

    Collect the even numbers from num_list in a collector called evens
    Collect the odd numbers from num_list in a collector called odds
"""
# Leave this line alone
# num_list = [12, 8, 25, 0, 25, 18, 5, 1, 13, 25, 25, 10, 1, 10, 12, 4, 7, 16, 15, 23, 11, 20, 2, 15, 7, 17, 2, 20, 6, 23, 22, 25, 20, 22, 16, 2, 21, 20, 0, 18, 1, 15, 3, 4, 2, 20, 23, 6, 6, 20, 14, 5, 14, 14, 3, 17, 21, 14, 19, 4, 18, 24, 22, 6, 12, 5, 13, 7, 1, 14, 6, 4, 24, 11, 19, 24, 12, 15, 4, 7, 17, 2, 4, 2, 17, 8, 2, 19, 17, 11, 0, 14, 2, 9, 21, 0, 6, 17, 0, 2]

# # Write your code here
# evens = []
# odds = []

# for num in num_list:
#   if num%2==0:
#     evens.append(num)
#   else:
#     odds.append(num)


#print(evens)
# print(odds)

"""For this challenge:

    Collect the numbers from num_list that are divisible by 3 in a collector called div_by_3
    Collect the numbers from num_list that are divisible by 7 in a collector called div_by_7

Then after collecting the values in the two separate lists:

    Collect the numbers from div_by_3 and div_by_7 that are equal to each other in a collector called div_by_both

"""

# Leave this line alone
# num_list = [53, 83, 25, 33, 83, 46, 8, 42, 56, 9, 30, 54, 67, 4, 5, 74, 74, 17, 36, 53, 25, 92, 62, 72, 59, 70, 10, 70, 83, 92, 98, 66, 38, 70, 100, 89, 79, 95, 4, 3, 19, 14, 60, 92, 14, 13, 32, 14, 31, 68, 67, 94, 93, 40, 52, 98, 81, 40, 0, 40, 34, 27, 54, 50, 77, 49, 26, 72, 96, 28, 23, 9, 6, 0, 34, 91, 65, 29, 60, 34, 32, 58, 15, 90, 67, 25, 26, 42, 1, 59, 60, 17, 51, 89, 35, 27, 42, 50, 25, 92]

# # Write your code here
# div_by_3 = []
# div_by_7 = []
# div_by_both = []

# for num in num_list:
#   if num%3 ==0:
#     div_by_3.append(num)
#   if num%7 ==0:
#     div_by_7.append(num)
#   if num%3==0 and num%7==0:
#     div_by_both.append(num)


# print(div_by_3)
# print(div_by_7)
# print(div_by_both)


'''Finish writing the function divisors according to its docstring.'''
"""n = 0
div_of_n = []
all_div = []
def divisors(n):
  for div in all_div:
    if n%div ==0:
      if div !=n:
        div_of_n.append(div)

  return div_of_n

print(div_of_n)"""

n=0
def divisors(n):
  proper_divisors_lst = []
  for div in range(1,n):
    if n%div == 0 and n != div:
      proper_divisors_lst.append(div)
  return proper_divisors_lst

print(divisors(49))