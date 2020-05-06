# removing duplicate var in given list by rearranging list

def remove_duplicate(n, arr):
    if n == 0 or n == 1:
        return n

    temp = list(range(n))

    j = 0
    for i in range(0, n - 1):

        if arr[i] != arr[i + 1]:
            temp[j] = arr[i]
            j += 1

    temp[j] = arr[n - 1]
    j += 1

    for i in range(0, j):
        arr[i] = temp[i]
        print(arr[i])
    return j

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        n = remove_duplicate(n, arr)
        for i in range(n):
            print(arr[i], end=" ")
        print()

