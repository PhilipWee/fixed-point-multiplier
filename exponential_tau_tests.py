# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 07:30:37 2021

@author: Philip Wee
"""


import math
from icecream import ic

test_num = 893

def convert_to_fixed_point(val,bit_precision):
    return int(val*(2**bit_precision))



#Assume delta t is 1 ms, tau is 20ms
delta_w = math.exp(-1/20)

#Print the expected value for testing
expected_val = test_num * delta_w
print("The expected value is:",expected_val)



def fixed_point_multiply(val,delta_w, bit_precision=16):
    #Express delta_w in fixed point bits (8bits) (.01010101)
    fixed_point_d_w = convert_to_fixed_point(delta_w,bit_precision)
    
    scaled_multiply_val = val * fixed_point_d_w
    multiply_val = scaled_multiply_val >> bit_precision
    return multiply_val

for test_num in range(0,65535,1000):
    expected_val = test_num * delta_w
    actual_val = fixed_point_multiply(test_num, delta_w)
    #Print the expected value for testing
    
    print("Test Num:",test_num,"Expected:",expected_val,"Actual:",actual_val)
    
print("The scaled_delta_w is:",convert_to_fixed_point(delta_w,16))

# print(delta_w)
# print(bin(95122))

# print(fixed_point_d_w)
# print(bin(fixed_point_d_w))
