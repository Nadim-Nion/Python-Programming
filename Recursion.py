# Recursion: Recursion is a process where a function can call itself.

def fact(n):
    if n==1: # Base Call : Using a condition to stop the recursive call
        return 1
    else:
        return n*fact(n-1)
    # fact(n-1) this is a recursive call


print(fact(5))
