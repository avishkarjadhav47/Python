#Q68-Q100 Most IMP

# =========================
# Q1 Print Your Name
# =========================
print("Avishkar")

# =========================
# Q2 Sum of Two Numbers
# =========================
a = int(input())
b = int(input())

print(a + b)

# =========================
# Q3 Area of Rectangle
# =========================
length = float(input())
breadth = float(input())

area = length * breadth

print(area)

# =========================
# Q4 Swap Two Variables
# =========================
a = int(input())
b = int(input())

a, b = b, a

print(a, b)

# =========================
# Q5 Celsius to Fahrenheit
# =========================
c = float(input())

f = (c * 9/5) + 32

print(f)

# =========================
# Q6 Even or Odd
# =========================
n = int(input())

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# =========================
# Q7 Positive Negative Zero
# =========================
n = int(input())

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

# =========================
# Q8 Largest Among Three Numbers
# =========================
a = int(input())
b = int(input())
c = int(input())

print(max(a, b, c))

# =========================
# Q9 Leap Year
# =========================
year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# =========================
# Q10 Grade Calculator
# =========================
marks = int(input())

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")

# =========================
# Q11 Print 1 to 100
# =========================
for i in range(1, 101):
    print(i)

# =========================
# Q12 Print Even Numbers 1-100
# =========================
for i in range(2, 101, 2):
    print(i)

# =========================
# Q13 Sum of First N Natural Numbers
# =========================
n = int(input())

print(n * (n + 1) // 2)

# =========================
# Q14 Factorial
# =========================
n = int(input())

fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

# =========================
# Q15 Multiplication Table
# =========================
n = int(input())

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# =========================
# Q16 Reverse a Number
# =========================
n = int(input())

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)

# =========================
# Q17 Palindrome Number
# =========================
n = int(input())

temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# =========================
# Q18 Armstrong Number
# =========================
n = int(input())

temp = n
digits = len(str(n))

total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")

# =========================
# Q19 Prime Number
# =========================
n = int(input())

if n < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")

# =========================
# Q20 Print All Primes Between 1-100
# =========================
for num in range(2, 101):

    prime = True

    for i in range(2, int(num**0.5) + 1):

        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)

# =========================
# Q21 Count Vowels
# =========================
s = input().lower()
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(count)

# =========================
# Q22 Reverse String
# =========================
s = input()
print(s[::-1])

# =========================
# Q23 Palindrome String
# =========================
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# =========================
# Q24 Count Words
# =========================
s = input()
print(len(s.split()))

# =========================
# Q25 Character Frequency
# =========================
s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# =========================
# Q26 Remove Duplicates from String
# =========================
s = input()
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)

# =========================
# Q27 Anagram
# =========================
s1 = input()
s2 = input()
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

# =========================
# Q28 Most Frequent Character
# =========================
s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(max(freq, key=freq.get))

# =========================
# Q29 First Non-Repeating Character
# =========================
s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
for ch in s:
    if freq[ch] == 1:
        print(ch)
        break

# =========================
# Q30 String Compression
# =========================
s = input()
result = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1
result += s[-1] + str(count)
print(result)

# =========================
# Q31 Largest Element
# =========================
lst = list(map(int, input().split()))
print(max(lst))

# =========================
# Q32 Second Largest Element
# =========================
lst = list(map(int, input().split()))
unique = list(set(lst))
unique.sort()
print(unique[-2])

# =========================
# Q33 Remove Duplicates from List
# =========================
lst = list(map(int, input().split()))
result = []
for num in lst:
    if num not in result:
        result.append(num)
print(result)

# =========================
# Q34 Common Elements in Two Lists
# =========================
a = [1,2,3,4]
b = [3,4,5,6]
print(list(set(a) & set(b)))

# =========================
# Q35 Rotate List by K Positions
# =========================
lst = [1,2,3,4,5]
k = 2
print(lst[-k:] + lst[:-k])

# =========================
# Q36 Move All Zeros To End
# =========================
lst = [1,0,2,0,3,0,4]
non_zero = []
zeroes = []
for num in lst:
    if num == 0:
        zeroes.append(num)
    else:
        non_zero.append(num)
print(non_zero + zeroes)

# =========================
# Q37 Merge Two Sorted Lists
# =========================
a = [1,3,5]
b = [2,4,6]
print(sorted(a + b))

# =========================
# Q38 Check if List is Sorted
# =========================
lst = list(map(int, input().split()))
if lst == sorted(lst):
    print("Sorted")
else:
    print("Not Sorted")

# =========================
# Q39 Missing Number
# =========================
lst = [1,2,3,5]
n = len(lst) + 1
expected = n * (n + 1) // 2
actual = sum(lst)
print(expected - actual)

# =========================
# Q40 Find Duplicate Elements
# =========================
lst = [1,2,3,2,4,1,5]
seen = set()
dup = set()
for num in lst:
    if num in seen:
        dup.add(num)
    else:
        seen.add(num)
print(list(dup))

# =========================
# Q41 Count Occurrences in Tuple
# =========================
t = (1, 2, 3, 2, 4, 2)
x = 2
print(t.count(x))

# =========================
# Q42 Max and Min in Tuple
# =========================
t = (10, 5, 20, 1, 15)
print(max(t))
print(min(t))

# =========================
# Q43 Tuple <-> List Conversion
# =========================
t = (1, 2, 3)
lst = list(t)
print(lst)

lst = [4, 5, 6]
t = tuple(lst)
print(t)

# =========================
# Q44 Set Union
# =========================
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

# =========================
# Q45 Set Intersection
# =========================
print(a & b)

# =========================
# Q46 Set Difference
# =========================
print(a - b)

# =========================
# Q47 Symmetric Difference
# =========================
print(a ^ b)

# =========================
# Q48 Check Subset
# =========================
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))

# =========================
# Q49 Frequency Count
# =========================
lst = [1, 2, 2, 3, 3, 3]

freq = {}

for i in lst:
    freq[i] = freq.get(i, 0) + 1

print(freq)

# =========================
# Q50 Student Marks Dictionary
# =========================
students = {
    "Rahul": 80,
    "Neha": 90,
    "Amit": 75
}

for k, v in students.items():
    print(k, v)

# =========================
# Q51 Highest Value Key
# =========================
d = {
    "Rahul": 80,
    "Neha": 90,
    "Amit": 75
}

print(max(d, key=d.get))

# =========================
# Q52 Merge Dictionaries
# =========================
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = d1 | d2
print(merged)

# =========================
# Q53 Invert Dictionary
# =========================
d = {'a': 1, 'b': 2}

inv = {}

for k, v in d.items():
    inv[v] = k

print(inv)

# =========================
# Q54 Factorial Using Function
# =========================
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

print(factorial(5))

# =========================
# Q55 Prime Using Function
# =========================
def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True

print(is_prime(13))

# =========================
# Q56 Fibonacci Using Function
# =========================
def fibonacci(n):

    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)
print()

# =========================
# Q57 Recursive Factorial
# =========================
def factorial_rec(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial_rec(n - 1)

print(factorial_rec(5))

# =========================
# Q58 Recursive Fibonacci
# =========================
def fib(n):

    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(7))

# =========================
# Q59 Divide By Zero Handling
# =========================
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

# =========================
# Q60 Invalid Input Handling
# =========================
try:
    n = int(input("Enter number: "))
    print(n)

except ValueError:
    print("Invalid Input")

# =========================
# Q61 Custom Exception
# =========================
class NegativeNumberError(Exception):
    pass

try:

    n = -5

    if n < 0:
        raise NegativeNumberError("Negative number not allowed")

except NegativeNumberError as e:
    print(e)

# =========================
# Q62 Constructor
# =========================
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Rahul", 90)

print(s.name)
print(s.marks)

# =========================
# Q63 Instance Method
# =========================
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

s = Student("Rahul")
s.display()

# =========================
# Q64 Inheritance
# =========================
class Person:

    def greet(self):
        print("Hello")

class Student(Person):
    pass

s = Student()
s.greet()

# =========================
# Q65 Method Overriding
# =========================
class Person:

    def greet(self):
        print("Hello")

class Student(Person):

    def greet(self):
        print("Hi Student")

s = Student()
s.greet()

# =========================
# Q66 Encapsulation
# =========================
class Student:

    def __init__(self):
        self.__marks = 90

    def get_marks(self):
        return self.__marks

s = Student()
print(s.get_marks())

# =========================
# Q67 Polymorphism
# =========================
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.sound()

# =========================
# Q68 Two Sum
# =========================
nums = [2, 7, 11, 15]
target = 9

d = {}

for i, num in enumerate(nums):

    diff = target - num

    if diff in d:
        print([d[diff], i])

    d[num] = i

# =========================
# Q69 Valid Parentheses
# =========================
s = "()[]{}"

stack = []

mp = {
    ')': '(',
    ']': '[',
    '}': '{'
}

valid = True

for ch in s:

    if ch in "([{":
        stack.append(ch)

    else:

        if not stack or stack.pop() != mp[ch]:
            valid = False
            break

print(valid and len(stack) == 0)

# =========================
# Q70 Longest Common Prefix
# =========================
strs = ["flower", "flow", "flight"]

prefix = strs[0]

for word in strs[1:]:

    while not word.startswith(prefix):
        prefix = prefix[:-1]

print(prefix)

# =========================
# Q71 Remove Duplicates Sorted Array
# =========================
nums = [1,1,2,2,3,4,4]

result = []

for num in nums:
    if num not in result:
        result.append(num)

print(result)

# =========================
# Q72 Merge Intervals
# =========================
intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()

merged = [intervals[0]]

for start, end in intervals[1:]:

    if start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)

    else:
        merged.append([start, end])

print(merged)

# =========================
# Q73 Kadane's Algorithm
# =========================
nums = [-2,1,-3,4,-1,2,1,-5,4]

curr = nums[0]
best = nums[0]

for num in nums[1:]:

    curr = max(num, curr + num)
    best = max(best, curr)

print(best)

# =========================
# Q74 Buy and Sell Stock
# =========================
prices = [7,1,5,3,6,4]

min_price = prices[0]
profit = 0

for p in prices:

    min_price = min(min_price, p)
    profit = max(profit, p - min_price)

print(profit)

# =========================
# Q75 Majority Element
# =========================
nums = [2,2,1,1,1,2,2]

count = 0
candidate = None

for num in nums:

    if count == 0:
        candidate = num

    count += 1 if num == candidate else -1

print(candidate)

# =========================
# Q76 Intersection of Arrays
# =========================
a = [1,2,2,1]
b = [2,2]

print(list(set(a) & set(b)))

# =========================
# Q77 Top K Frequent Elements
# =========================
from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

freq = Counter(nums)

print(freq.most_common(k))

# =========================
# Q78 Rotate Array
# =========================
nums = [1,2,3,4,5,6,7]
k = 3

print(nums[-k:] + nums[:-k])

# =========================
# Q79 Move Zeroes
# =========================
nums = [0,1,0,3,12]

result = [x for x in nums if x != 0]
result.extend([0] * nums.count(0))

print(result)

# =========================
# Q80 Product of Array Except Self
# =========================
nums = [1,2,3,4]

result = []

for i in range(len(nums)):

    prod = 1

    for j in range(len(nums)):

        if i != j:
            prod *= nums[j]

    result.append(prod)

print(result)

# =========================
# Q81 Difference Between append(), extend(), insert()
# =========================

lst = [1, 2]

lst.append([3, 4])
print(lst)          # [1, 2, [3, 4]]

lst = [1, 2]
lst.extend([3, 4])
print(lst)          # [1, 2, 3, 4]

lst = [1, 2]
lst.insert(1, 100)
print(lst)          # [1, 100, 2]


# =========================
# Q82 Difference Between == and is
# =========================

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)       # True (values same)
print(a is b)       # False (different objects)


# =========================
# Q83 Mutable vs Immutable
# =========================

# Mutable
lst = [1, 2, 3]
lst[0] = 100
print(lst)

# Immutable
s = "hello"
# s[0] = 'H'  # Error


# =========================
# Q84 Shallow Copy vs Deep Copy
# =========================

import copy

a = [[1, 2], [3, 4]]

shallow = copy.copy(a)
deep = copy.deepcopy(a)

a[0][0] = 999

print(shallow)      # Changed
print(deep)         # Unchanged


# =========================
# Q85 List vs Tuple
# =========================

lst = [1, 2, 3]
tup = (1, 2, 3)

lst[0] = 10         # Works
# tup[0] = 10       # Error


# =========================
# Q86 Set vs Dictionary
# =========================

s = {1, 2, 3}
d = {"a": 1, "b": 2}

print(type(s))
print(type(d))


# =========================
# Q87 Generator vs Iterator
# =========================

def gen():
    yield 1
    yield 2
    yield 3

g = gen()

print(next(g))
print(next(g))
print(next(g))


# =========================
# Q88 Lambda Function
# =========================

square = lambda x: x * x

print(square(5))


# =========================
# Q89 Map Filter Reduce
# =========================

from functools import reduce

nums = [1, 2, 3, 4, 5]

print(list(map(lambda x: x * 2, nums)))

print(list(filter(lambda x: x % 2 == 0, nums)))

print(reduce(lambda a, b: a + b, nums))


# =========================
# Q90 Decorator
# =========================

def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

@decorator
def greet():
    print("Hello")

greet()


# =========================
# Q91 Word Frequency
# =========================

text = "python is easy python is powerful"

freq = {}

for word in text.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)


# =========================
# Q92 Duplicate Words
# =========================

text = "python java python c java"

freq = {}

for word in text.split():
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    if count > 1:
        print(word)


# =========================
# Q93 Sort Dictionary By Values
# =========================

d = {'a': 5, 'b': 2, 'c': 8}

result = dict(sorted(d.items(), key=lambda x: x[1]))

print(result)


# =========================
# Q94 Group Anagrams
# =========================

from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    groups[key].append(word)

print(list(groups.values()))


# =========================
# Q95 Longest Substring Without Repeating Characters
# =========================

s = "abcabcbb"

seen = set()

left = 0
max_len = 0

for right in range(len(s)):

    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    max_len = max(max_len, right - left + 1)

print(max_len)


# =========================
# Q96 Balanced Brackets
# =========================

s = "{[()]}"

stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

valid = True

for ch in s:

    if ch in "([{":
        stack.append(ch)

    else:

        if not stack or stack.pop() != pairs[ch]:
            valid = False
            break

print(valid and len(stack) == 0)


# =========================
# Q97 Matrix Transpose
# =========================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = list(zip(*matrix))

print(transpose)


# =========================
# Q98 Spiral Matrix Traversal
# =========================

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

result = []

while matrix:

    result += matrix.pop(0)

    matrix = list(zip(*matrix))[::-1]

print(result)


# =========================
# Q99 Binary Search
# =========================

arr = [1,2,3,4,5,6,7]
target = 5

left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        print(mid)
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1


# =========================
# Q100 Merge Sort
# =========================

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(merge_sort([5,3,8,2,1,9]))