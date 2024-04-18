count = int(input())
string = input().split('#')

max_count = max([len(i) for i in string])
min_count = min([len(i) for i in string])

print(min_count, max_count)