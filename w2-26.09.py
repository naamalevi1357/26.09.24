# start

list_klt: list[int] = []
count: int = 0
while True:
    klt: int = int(input("what is numbers ? "))
    if klt == -999:
        break
    if 0 > klt > 10:
        continue
    # count+=1
    list_klt.append(klt)
    print(list_klt)
    print(list_klt.count(klt))

# stop

# klt: int = int(input("what is numbers ? "))
#
# for i in range(10):
#     if klt == -999:
#         break
#     if 0 > klt > 10:
#         continue
#     list_klt.append(klt)
# print(list_klt)
# print(list_klt.count(klt))


# stop
