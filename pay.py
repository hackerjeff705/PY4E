xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
try:
    h = float(xh)
    r = float(xr)
except:
    print("Error input must be numeric")
    quit()

if h > 40:
    nt = h * r
    ot = (h-40) * 0.5 * r
    tot = nt + ot
else:
    tot = h * r
print(tot)
