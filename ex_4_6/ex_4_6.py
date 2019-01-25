def computepay(fh,fr):
    if fh > 40:
        ot = (fh - 40) * 1.5 * fr
        tp = ot + (40 * fr)
    else:
        tp = fh * fr
    return tp

ih = input("Enter Hours:")
ir = input("Enter Rate:")

fh = float(ih)
fr = float(ir)

p = computepay(fh, fr)
print(p)
