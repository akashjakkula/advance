import random
lower="abcdefghijklmnopqrstuvxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="!@#$%&*?"
alll=lower+upper+numbers+symbols
length=16
password=" ".join(random.sample(alll,length))
print(password)
