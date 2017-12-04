import itertools

RIGHT=1
UP=2
LEFT=3
DOWN=4

def spiral():
    max, dir = 0, RIGHT
    num, x, y = 1, 0, 0

    while True:
        yield (num, x, y)

        num += 1

        if dir is RIGHT:
            x += 1
            if x > max:
                max += 1
                dir = UP
        elif dir is UP:
            y -= 1
            if y <= -max:
                dir = LEFT
        elif dir is LEFT:
            x -= 1
            if x <= -max:
                dir = DOWN
        elif dir is DOWN:
            y += 1
            if y >= max:
                dir = RIGHT

#print(list(itertools.islice(spiral(), 10)))

search = 312051
for (num, x, y) in spiral():
    if num == search:
        distance = abs(x) + abs(y)
        print(distance)
        break
