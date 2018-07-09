import os

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(arr)

    for i in range(n - 1, -1, -1):
        fptr.write(' '.join(map(str, arr[i])))

    fptr.close()