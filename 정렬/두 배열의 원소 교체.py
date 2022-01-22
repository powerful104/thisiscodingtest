n, k = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
max_ = sum(A)
for _ in range(k):
    A[0], B[n-1] = B[n-1], A[0]
    if sum(A) > max_:
        max_ = sum(A)
    A.sort()
    B.sort()

print(max_)