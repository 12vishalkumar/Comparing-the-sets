# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
S1 = set(map(int, input().split()))
S2 = set(map(int, input().split()))
print(S1.issubset(A) and S2.issubset(A))