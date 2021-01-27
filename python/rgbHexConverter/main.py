def rgb(r, g, b):
    r = clamp(r)
    g = clamp(g)
    b = clamp(b)
    string = '{:02X}{:02X}{:02X}'.format(r, g, b)
    return string

def clamp(x):
    if x < 0:
        return 0
    elif x > 255:
        return 255
    else:
        return x

print(rgb(-20,275,125))    