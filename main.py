import pandas as pd

df = pd.read_csv('uni_dataset.csv')
df = df.drop('Index',axis=1)

#Most sorting algorithms only work on lists or simple arrays. Edit a standard sorting algorithm to compare a specific key from each of the nested list elements. Hint: lst[3][2] accesses the 3rd element of the 4th list.
lst = []

for x in range(len(df)-1):
  lst.append(tuple(df.iloc[x].values))
labels = df.columns.values
df.head()

#Most sorting algorithms only work on lists or simple arrays. Edit a standard sorting algorithm to compare a specific key from each of the nested list elements. Hint: lst[3][2] accesses the 3rd element of the 4th list
def insertionSort(arr, column):
  for i in range(1, len(arr)):
    value = arr[i]
    j = i-1
    while j >= 0 and (int(arr[j][column].replace('%', '')) > int(value[column].replace('%', ''))):
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = value

insertionSort(lst, 3)
#for i in range(len(lst)):
  #print(lst[i][6])

#Using selection sort order lst2 by student satisfaction. The journalists want to write about the 40 universities with highest satisfaction.
def selectionSort(arr):
  size = len(arr) - 40
  for i in range(1, len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
      if int(arr[j][3].replace('%', '')) < int(arr[min_index][3].replace('%', '')):
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  lst2 = arr[size:]
  return lst2

lst2 = selectionSort(lst)
lst2.reverse()
#print(lst2)

#Write a linear search algorithm to find where a specific university is within these 40.
def linearSearch(arr, n, x):
  for i in range(0, n):
    if (arr[i][0] == x):
      return i
  return False

value = linearSearch(lst2, len(lst2), 'x')
#if (value == False):
  #print('University is not in list')
#else:
  #print('University is at index', value)

#Implement an efficient sorting algorithm to arrange universities by name (ignore any starting with ‘university of…’ so University of Bath would be before Birmingham City University
def quickSort(A):
  quickSortRec(A,0,len(A))

def quickSortRec(A, lo, hi):
  # sorts A[lo:hi]
  if hi-lo <= 1:
    return
  iPivot = partition(A,lo,hi)
  quickSortRec(A,lo,iPivot)
  quickSortRec(A,iPivot+1,hi)
  
def partition(A, lo, hi):
  flag = False
  if A[lo][0][:14] == "University of ":
    pivot = A[lo][0][14:]
    flag = True
  else:
    pivot = A[lo][0]
  B = [0 for i in range(lo,hi)]
  loB = 0
  hiB = len(B)-1
  for i in range(lo+1,hi):
    if A[i][0][:14] == "University of ":
      if A[i][0][14:] < pivot:
        B[loB] = A[i]
        loB += 1
      else:
        B[hiB] = A[i]
        hiB -= 1
    else:
      if A[i][0] < pivot:
        B[loB] = A[i]
        loB += 1
      else:
        B[hiB] = A[i]
        hiB -= 1


  if flag:
    pivot= "University of " + pivot
    B[loB] = A[lo]
  else:
    B[loB] = A[lo]

  for i in range(lo,hi):
    A[i] = B[i-lo]
  return lo+loB


def sortAlphabetically(lst):
  #print(lst)
  quickSort(lst)
  return lst

#print(sortAlphabetically(lst))


#Implement an efficient search algorithm to find how many universities have satisfaction > 85%
def binarySearch(array, value):
  first = 0
  last = len(array) + 1
  index = -1
  while (first <= last) and (index == -1):
    middle = (first + last) // 2
    if int(array[middle][3].replace('%', '')) == value:
      index = middle
    else:
      if value < int(array[middle][3].replace('%', '')):
        last = middle - 1
      else:
        first = middle + 1
        
  values = len(array) - index
  return values

lst2 = selectionSort(lst)
x = 86
results = binarySearch(lst2, x)
#if (results == -1):
  #print('No result available')
#else:
  #print('There are', results, 'unis with a score over 85%')