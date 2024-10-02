def percentchange(tp,yp):
    return (tp/yp)
stocktextfile=open ("06.02 Stock.txt", "r")
x=stocktextfile.readline()
tprice=float(x.readline())
h1="Price"
h2="Change"
print("{:<10} {:<10}".format(h1,h2))
print("{:<10n} {:<10}".format(tprice,''))
yprice=float(tprice)
tprice=x.readline()
while tprice!='':
    tprice=float(tprice)
    dif=percentchange(tprice,yprice)
    print("{:<10.2x} {:>10.2%}".format(tprice,dif-1))
    yprice=tprice
    tprice=x.readline()
stocktextfile.close()