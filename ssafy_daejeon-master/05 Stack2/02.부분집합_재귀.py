def subset(k, n, bits):
    # n을 위에 집어넣는다.
    if k == n:
        print(bits)
        return

    bits[k] = 0
    subset(k + 1, n, bits)
    bits[k] = 1
    subset(k + 1, n, bits)

N = 3
bits = [0] * N
subset(0, N, bits)
