# start

tamp: list[float] = []
count: int = 0
while True:
    tamp1: float = float(input(" what is tamprtora?"))
    if tamp1 == -999:
        break
    if tamp1 < -50 or tamp1 > 50:
        continue
    if not tamp1 == -999:
        count += 1
    tamp.append(tamp1)
tamp.extend([-20.0, 39.1, 18.5])
# d: in + B + brings me a new record And in extend it changes the belly of the list
print(tamp)
print(max(tamp))
print(min(tamp))
if 18.5 in tamp:
    print(True)
else:
    print(False)
print(tamp.count(-20.0))
print(sum(tamp))
for c in tamp:
    print(c)
print(tamp.index(39.1))
print(tamp)
del tamp[0]
print(tamp)
del tamp[:: 2]
print(tamp)
# m:
# tamp.remove(18.05)
# print(tamp)
# Due to the fact that we did several operations before the number 18.5 does not exist
# (that's why I mentioned it as a bowl due to making an error)
tamp_last = tamp.pop()
print(tamp)
tamp2 = tamp.copy()
tamp.extend(tamp2)
print(tamp)
tamp.sort()
print(tamp)
tamp3 = tamp.copy()
tamp.extend(tamp3)
print(tamp)
tamp.sort(reverse=True)
print(tamp)

# stop
