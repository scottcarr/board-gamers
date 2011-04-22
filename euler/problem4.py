biggest=0

for i in range(999):
    for j in range(999):
        product = i*j
        mystring = str(product)
        if mystring==mystring[::-1]:
            if product > biggest:
                biggest = product

print biggest

