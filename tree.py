import turtle
 

# MergeSort in Python


def mergeSort(array, t):
    if len(array) > 1:
        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        t.forward(40)
        t.right(40)
        mergeSort(L, t)
        t.left(40)
        mergeSort(M, t)
        t.right(80)
        i = j = k = 0
        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
 
"""def tree(branchLen,t):
    if branchLen > 10:
        t.forward(branchLen)
        t.right(40)
        tree(branchLen-20,t)
        t.left(80)
        tree(branchLen-20,t)
        t.right(40)
        t.backward(branchLen)"""
 
def main():
    myWin = turtle.Screen()
    myWin.bgcolor("black")
    t = turtle.Turtle()    
    t.width(10)
    t.left(90)
    t.up()
    t.backward(250)
    t.down()
    t.color("silver")

    searching_array = [6, 5, 12, 10, 9, 1]
    mergeSort(searching_array, t)
    print("Sorted array is: ")
    printList(searching_array)
 
    #tree(150,t)
    myWin.exitonclick()

main()


