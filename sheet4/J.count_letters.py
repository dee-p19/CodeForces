S = input()
lst =[0] * 26
for i in S:
    lst[ord(i) - ord('a')] += 1
for i in range(26):
    if lst[i] != 0:
        print(f"{chr(i + ord('a'))} : {lst[i]}")

