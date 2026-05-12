def euler(dx, dy, dz, x0, y0, z0, h):
    x = x0 + dx * h
    y = y0 + dy * h
    z = z0 + dz * h

    return x, y, z
