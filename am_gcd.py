

# GCD for an array elements
def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    # min = numpy.min(arr)
    m = arr[0]
    for i in range(1, len(arr)):
        m = gcd(m, arr[i])
    return m
# to calculate the gcd of tow numbers
def gcd(m, n):
    if m % n != 0:
        return gcd(n, m % n)
    else:
        return n
 # input :

arr = list()

num = input('enter un  nombre')

for i in range(int(num)):
    n = input('number')
    arr.append(int(n))

# program
print("the GCD of array is ")
print(generalizedGCD(num, arr))













