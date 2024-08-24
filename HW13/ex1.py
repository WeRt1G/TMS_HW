from time import sleep
def fibonachi_gen(limit):
    last1 = 1
    last2 = 1
    counter = 0

    while counter < limit:
        counter += 1
        print(f"{last1=}")
        print(f"{last2=}")
        tmp = last1 + last2
        last1 = last2
        last2 = tmp
        yield tmp

for el in fibonachi_gen(10):
    print(el)
    sleep(0.3)

