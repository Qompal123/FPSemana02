palavra1 = str(input())
palavra2 = str(input())

intersect = set(palavra1) & set(palavra2)

print("". join(sorted(intersect)))