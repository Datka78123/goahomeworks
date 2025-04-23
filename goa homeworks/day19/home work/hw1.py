#შექმენით ფუნქცია, რომელიც აერთებს ორ ლისტს (ორივეში მხოლოდ integer-ებია) და ასევე ალაგებს მათ ზრდადობის მიხედვით.

lis1 = ['ll','lll']
lis2 = ['l','llll']


def func(l,k):
    res=[] #result
    for i in l:
        res.append(i)
    for i in k:
        res.append(i)
    return res


print(func(lis1,lis2))
