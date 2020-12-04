if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    runner_up = arr[-2]
    print(runner_up)
        