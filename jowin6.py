#WAP to get the value from the dictionary for the given key?

d = {100:'Jowin', 200:'Ajay', 300:'Aashik'}
print(d)

Key = input('Enter the key to fetch the value:\t')

if Key in d:
     print('The corresponding data for key:', Key,'is:', d[Key])

     print('The corresponding data for key:', Key,'is:', d.get(Key))

else:
     print('The specified key is not present within the Dictionary')



#WAP to find the product of values present within a list without using builtin functions?

lst = [1,2,3,4,5,6,7,8,9]

res = 1

for i in lst:
    res *= 5

    print(res, 'is the sum of the list')
