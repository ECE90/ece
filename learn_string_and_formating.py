#print("hello world")

"""
Variables (Değişkenler)
çoklu satar

Sting(katar) = iki tırnak içine yazan herşey
"""


a = 5
b = 3
toplam = a + b
print(toplam)

print("Toplam = ",toplam)


print ("{0} {1} {2}".format(*args: "Toplam", "=", toplam))
print("{0} {1} {2}".format(*args: "Toplam", "=", a + b))
print(f"""{a} + {b} = {toplam}""")
