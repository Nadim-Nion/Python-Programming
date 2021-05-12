from collections import deque

Bank=deque(["Nion","Nishad","Tazin"])

print(Bank)
Bank.popleft()
print(Bank)

Bank.popleft()
print(Bank)

Bank.popleft()
if not Bank:
    print("No Person Left")
