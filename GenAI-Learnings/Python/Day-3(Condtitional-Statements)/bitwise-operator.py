# Bitwise operator
# &,|,^,~,<<,>>




a = 10
print("Binary Form of a is : ",format(a,'b')," ",type(format(a,'b')))
print("The length of the binary form of a is : ",a.bit_length())




x = 10
y = 13

print("The binary form of x is : ",format(x,'b'))
print("The binary form of y is : ",format(y,'b'))

#and
and_result = x&y
print("The & operator result is : ",and_result)
print("The binary form of x is : ",format(and_result,'b'))

# or
or_result = x|y
print("The I operator result is : ",or_result)
print("The binary form of x is : ",format(or_result,'b'))


#xor

xor_result = x^y
print("The ^ operator result is : ",xor_result)
print("The binary form of x is : ",format(xor_result,'b'))

# left shiift - a*2^n
left_shift_result = x<<4
print("The << operator result is : ",left_shift_result)
print("The binary form of x is : ",format(left_shift_result,'b'))


# right shift - a/2^n

right_shift_result = x>>2
print("The >> operator result is : ",right_shift_result)
print("The binary form of x is : ",format(right_shift_result,'b'))
