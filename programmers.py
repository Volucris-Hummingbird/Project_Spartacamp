a = int(input())


def even_odd():
    if 1 <= a <= 1000:
        if a % 2 == 0:
            return (f"{a} is even")
        else:
            return (f"{a} is odd")


print(even_odd())
