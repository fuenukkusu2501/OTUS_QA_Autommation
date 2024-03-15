def get_area(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(area)


get_area(13, 14, 15)






