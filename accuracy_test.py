import math

cos = [1000, 10000, 2**14, 2**15, 2**64]
sin = [0, 0, 0, 0, 0, 0]
scaling = [1000, 10000, 2**14, 2**15, 2**64]
deltas = [0, 0, 0, 0, 0, 0, 0]
x = 60
eps = 100
# true x = 0.6 (x / eps )

# for ff in range(100):

for i in range(x):
    for j in range(len(cos)):
        cos[j] = cos[j] - sin[j] // eps
        sin[j] = sin[j] + cos[j] // eps

for i in range(len(cos)):
    print(
        f"for scaling {scaling[i]}: sin = {sin[i]/scaling[i]}, cos = {cos[i]/scaling[i]}")
    print(
        f"for scaling {scaling[i]}: sin = {sin[i]}, cos = {cos[i]}")

print(x/eps)
print(f"true value sin = {math.sin(x/eps)}, cos = {math.cos(x/eps)} ")

for i in range(len(cos)):
    print(
        f"for scaling {scaling[i]}: sin_delta = {(sin[i]/scaling[i] - math.sin(x/eps)):.12f}, cos = {(cos[i]/scaling[i] - math.cos(x/eps)):.12f}")

print("")
cos = [1000, 10000, 2**14, 2**15, 2**128]
sin = [0, 0, 0, 0, 0]
scaling = [1000, 10000, 2**14, 2**15, 2**128]
deltas = [0, 0, 0, 0, 0, 0]
x = 314159
eps = 100000
for i in range(x):
    for j in range(len(cos)):
        cos[j] = cos[j] - sin[j] // eps
        sin[j] = sin[j] + cos[j] // eps

for i in range(len(cos)):
    print(
        f"for scaling {scaling[i]}: sin_delta = {(sin[i]/scaling[i] - math.sin(x/eps)):.12f}, cos = {(cos[i]/scaling[i] - math.cos(x/eps)):.12f}")

print(x/eps)
print(f"true value sin = {math.sin(x/eps)}, cos = {math.cos(x/eps)} ")
print("done")
