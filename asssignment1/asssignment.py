# 1st Question
number =int(input("enter the number: "))
output = ''
if number % 3 == 0:
	output += 'Pling'

if number % 5 == 0:
    output += 'Plang'

if number % 7 == 0:
    output += 'Plong'
else:
    print(str(number))
print(output)
#output:
#enter the number: 35
#PlangPlong


#2nd question
numbers = int(input("Enter value of n numbers "))
sqr_sum = 0
sum_sqr = 0
final_sqr = 0
for i in range(1, numbers+1):
    sqr_sum += i*i
    sum_sqr += i
final_sum_sqr = sum_sqr * sum_sqr
print("square of sum : ", sqr_sum)
print("sum of square : ", final_sum_sqr)
#output:
#Enter value of n numbers 10
#square of sum :  385
#sum of square :  3025


# 3rd question
print("prime number range:")
for num in range(1, 13):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num+1):
           if (num % i) == 0:
               break
       else:
        if num <0:
            raise ValueError("there is no zeroth prime")
        print(num)
# output:
# prime number range:
# 2
# 3
# 5
# 7
# 11
# 13

#4th question
num_range=int(input("enter the range: "))
total_sum = 0
for i in range(num_range):
    if (i%3 == 0 or i%5 == 0):
        total_sum = total_sum+i
print (total_sum)
# output:
# enter the range: 20
# 78

#5th question
test_list = [5, 6, [], 9]
print("The original list is : " + str(test_list))
res = [ele for ele in test_list if ele != []]
print("List after empty list removal : " + (str(res)))
# output:
# The original list is : [5, 6, [], 9]
# List after empty list removal : [5, 6, 9]