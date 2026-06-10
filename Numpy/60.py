#Vectorization,Broadcasting,Boolean indexing,Reshaping Most IMP

import numpy as np

# Dataset
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([5,10,15,20,25])

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# =========================
# Q1 Create Array
# =========================
np.array([1,2,3,4,5])

# Q2 Zeros
np.zeros(5)

# Q3 Ones
np.ones(10)

# Q4 0-9
np.arange(10)

# Q5 10-50 step 10
np.arange(10,51,10)

# =========================
# Q6 Shape
# =========================
matrix.shape

# Q7 Dimension
matrix.ndim

# Q8 Total Elements
matrix.size

# Q9 Datatype
matrix.dtype

# Q10 Convert to Float
arr1.astype(float)

# =========================
# Q11 First Element
# =========================
arr1[0]

# Q12 Last Element
arr1[-1]

# Q13 Third Element
arr1[2]

# Q14 Second Row
matrix[1]

# Q15 First Column
matrix[:,0]

# =========================
# Q16 First 3 Elements
# =========================
arr1[:3]

# Q17 Last 2 Elements
arr1[-2:]

# Q18 Middle 3 Elements
arr1[1:4]

# Q19 First 2 Rows
matrix[:2]

# Q20 Last 2 Columns
matrix[:,1:]

# =========================
# Q21 Add 10
# =========================
arr1 + 10

# Q22 Multiply by 2
arr1 * 2

# Q23 Square
arr1 ** 2

# Q24 Add Arrays
arr1 + arr2

# Q25 Multiply Arrays
arr1 * arr2

# =========================
# Q26 Sum
# =========================
arr1.sum()

# Q27 Mean
arr1.mean()

# Q28 Median
np.median(arr1)

# Q29 Max
arr1.max()

# Q30 Min
arr1.min()

# =========================
# Q31 Transpose
# =========================
matrix.T

# Q32 Matrix Multiplication
np.dot(matrix, matrix)

# OR
matrix @ matrix

# Q33 Determinant
np.linalg.det(matrix)

# Q34 Inverse
# (Need invertible matrix)
A = np.array([[1,2],[3,4]])
np.linalg.inv(A)

# Q35 Diagonal Elements
np.diag(matrix)

# =========================
# Q36 Reshape
# =========================
np.array([1,2,3,4,5,6]).reshape(2,3)

# Q37 Flatten
matrix.flatten()

# Q38 Column Vector
arr1.reshape(-1,1)

# Q39 Row Vector
arr1.reshape(1,-1)

# Q40 Reshape Using -1
np.arange(12).reshape(3,-1)

# =========================
# Q41 Greater than 25
# =========================
arr1[arr1 > 25]

# Q42 Less than Mean
arr1[arr1 < arr1.mean()]

# Q43 Even Elements
arr1[arr1 % 2 == 0]

# Q44 Odd Elements
arr1[arr1 % 2 != 0]

# Q45 Between 15 and 45
arr1[(arr1 >= 15) & (arr1 <= 45)]

# =========================
# Q46 Random Numbers
# =========================
np.random.rand(5)

# Q47 Random Matrix
np.random.rand(3,3)

# Q48 Random Integers
np.random.randint(1,100,10)

# Q49 Seed
np.random.seed(42)

# Q50 Normal Distribution
np.random.normal(0,1,10)

# =========================
# Q51 Unique Elements
# =========================
a = np.array([1,2,2,3,3,4])

np.unique(a)

# Q52 Frequency Count
unique, counts = np.unique(a, return_counts=True)

dict(zip(unique, counts))

# Q53 Sort Array
np.sort(a)

# Q54 Second Largest
np.sort(np.unique(a))[-2]

# Q55 Duplicates
unique, counts = np.unique(a, return_counts=True)

unique[counts > 1]

# Q56 Replace Even Numbers with 0
a = np.array([1,2,3,4,5,6])

a[a % 2 == 0] = 0

a

# Q57 Indices where >20
np.where(arr1 > 20)

# Q58 Vertical Stack
np.vstack((arr1, arr2))

# Q59 Horizontal Stack
np.hstack((arr1, arr2))

# Q60 Split into 3 Equal Parts
np.split(np.arange(12), 3)