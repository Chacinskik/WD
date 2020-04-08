def nty_wyraz_geo(a=1,q=2,ile=10):
    return a*(q**(ile-1))

def suma_wyrazow_geo(a=1,q=2,ile=10):
    if (q==1):
        return a*ile
    else:
        return a*((1-(q**ile))/1-q)