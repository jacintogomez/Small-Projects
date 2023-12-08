import math


def child(element, degree):
    children = []
    for j in range(1, degree + 1):
        children.append(degree * (element - 1) + j + 1)
    return children


def parent(element, degree):
    return math.floor((element - 2) / degree) + 1


def displaytree(n, i):
    print('Parent\tNode#\tChildren')
    for x in range(1, i + 1):
        print(str(parent(x, n))+'\t\t'+str(x)+'\t\t'+str(child(x, n)))


# first 10 nodes of 5-ary tree:
print('Input the degree (number of children per node), and number of iterations you want to see (# of nodes)')
n=int(input('Enter degree n: '))
i=int(input('Enter the number of nodes: '))
displaytree(n, i)