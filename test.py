import numpy as np

def sum_values(list):
  ssum = 0
  for i in list:
    ssum+=i
  return ssum

#testing fuction
l = [10,30,40,10,1]
sum_list = sum_values(l)

print(sum_list)
