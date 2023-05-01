# Python3 code to demonstrate working of
# Convert String list to ascii values
# using loop + ord()

# initialize list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list : " + str(test_list))

# Convert String list to ascii values
# using loop + ord()
res = []
for ele in test_list:
	res.extend(ord(num) for num in ele)

# printing result
print("The ascii list is : " + str(res))
#***********************************
a = 79

# Base 2(binary)
bin_a = bin(a)
print(bin_a)
print(int(bin_a, 2))


#python 3.x
text = input("enter a string to convert into ascii values:")
ascii_values = []
for character in text:
    ascii_values.append(ord(character))
print(ascii_values)
#********************************************
num = 24.89

rounded = round(num, 1)
print(rounded)
