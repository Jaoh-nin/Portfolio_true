amount = input().split()
am_1 = int(amount[0])
am_2 = int(amount[1])
am_3 = int(amount[2])
price = int(input())
ovr = (am_1 * 2)+(am_2 * 2) * am_3

print(ovr)
print(price * ovr)