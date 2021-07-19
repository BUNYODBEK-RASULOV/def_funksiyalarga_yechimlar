# 1-misol
# a=float(input("input a:"))
# b=float(input("input b:"))
# c=float(input("input c:"))
# d=int(input("input d:"))
# e=int(input("input e:"))
# def daraja_hisobla(x):
#     """"Sonning 3-darajasini hisoblaydigan funksiya"""
#     y=x*x*x
#     return y
# daraja_hisobla(a)
# daraja_hisobla(b)
# daraja_hisobla(c)
# daraja_hisobla(d)
# daraja_hisobla(e)

# 2-misol
# a = float(input("input a:"))
# b = float(input("input b:"))
# c = float(input("input c:"))
#
# def  daraja_1_2_3Hisobla(x):
#     y2 = x**2
#     y3 = x **3
#     y4 = x ** 4
#     print("y^2=",y2)
#     print("y^3=",y3)
#     print("y^4=", y4)
#
# daraja_1_2_3Hisobla(a)
# daraja_1_2_3Hisobla(b)
# daraja_1_2_3Hisobla(c)

# 3-misol
# a=float(input("input a:"))
# b=float(input("input b:"))
# c=float(input("input c:"))
# d=int(input("input d:"))
# def MEAN(x,y):
#     import math
#     arifmetik=(x+y)/2
#     geomitrik=math.sqrt(x**2+y**2)
#     print("{} va {} sonlarining O'rta arifmetigi={}".format(x,y,arifmetik))
#     print("{} va {} sonlarining O'rta geometrigi={} \n ".format(x,y,geomitrik))
# MEAN(a,b)
# MEAN(a,c)
# MEAN(a,d)

# 4-misol
# a=float(input("input a:"))
# b=float(input("input b:"))
# c=float(input("input c:"))
# def yuza_premetr(x):
#     import math
#     s=math.sqrt(3)*x*x/4
#     p=3*x
#     print("tomoni {} bo'lgan uchburchakning yuzasi s={}".format(x,s))
#     print("tomoni {} bo'lgan uchburchakning perimetri p={}\n".format(x,p))
# yuza_premetr(a)
# yuza_premetr(b)
# yuza_premetr(c)

# 5-misol
# x1 = float(input("input x1:"))
# y1 = float(input("input y1:"))
# x2 = float(input("input x2:"))
# y2 = float(input("input y2:"))
#
#
# def turtburchak_yuza_perimetr(x1, y1, x2, y2):
#     import math
#     a = abs(x1 - x2)
#     b = abs(y1 - y2)
#     s = a * b
#     p = 2 * (a + b)
#     print("uchlarining kordinatasi x1={},y1={},x2={},y2={} bulgan 4 burchakning yuzasi s={}".format(x1, y2, x2, y2, s))
#     print("uchlarining kordinatasi x1={},y1={},x2={},y2={} bulgan 4 burchakning perimetri s={} \n".format(x1, y2, x2, y2,p))
#
# turtburchak_yuza_perimetr(x1, y1, x2, y2)

# 6-misol
# a=input("a sonni kiriting:")
# def son_raqamlari (a):
#     s=0
#     for x in a:
#         x = int(x)
#         s=s+x
#     print("raqamlari yig'indisi:",s)
#     print("raqamlari soni:",len(a))
# son_raqamlari(a)

# 7-misol
# a = int(input("input a:"))
#
#
# def sonni_teskarisini_yozadi(a):
#     print("a=", a)
#     s = 0
#     while a != 0:
#         b = a % 10
#         s = s * 10 + b
#         a = a // 10
#     print("b=", s)
#
#
# sonni_teskarisini_yozadi(a)


# 8-misol
# a = int(input("input a:"))
# r = int(input("input r:"))
#
#
# def sonQushadiOxiriga(x, r):
#     x = 10 * x + r
#     print("yangi son:", x)
#
#
# sonQushadiOxiriga(a, r)

# 9-misol
# a = int(input("input a:"))
# r = int(input("input r:"))
# c=a
# def chapdanQushadi(a,r):
#     while a!=0:
#         r=r*10
#         a=a//10
#     print(r+c)
# chapdanQushadi(a,r)

# 10-misol
# a = int(input("input a:"))
# b = int(input("input b:"))
# def swap(a,b):
#     a = a + b
#     b = a - b
#     a = a - b
#     print("a=", a)
#     print("b=", b)
# swap(a,b)

# 11-misol
# a = int(input("input x:"))
# b = int(input("input y:"))
# def mixMax(a,b):
#     c=a
#     if c<b:
#         c=b
#     print("x=",a+b-c)
#     print("y=",c)
# mixMax(a,b)

# 12-misol
# a=float(input("input a:"))
# b=float(input("input b:"))
# c=float(input("input c:"))
# d=float(input("input d:"))
#
# def sort(a,b,c,d):
#     mas = [a, b, c, d]
#     for x in range(4):
#         for y in range(4):
#             if mas[x] < mas[y]:
#                 k = mas[x]
#                 mas[x] = mas[y]
#                 mas[y] = k
#     print(mas)
#
# sort(a,b,c,d)

# 13-misol
# a = float(input("input a:"))
# b = float(input("input b:"))
# c = float(input("input c:"))
# d = float(input("input d:"))
#
#
# def sortmin(a, b, c, d):
#     mas = [a, b, c, d]
#     for x in range(4):
#         for y in range(4):
#             if mas[x] > mas[y]:  # oldingi masalada < edi shart
#                 k = mas[x]
#                 mas[x] = mas[y]
#                 mas[y] = k
#     print(mas)
#
#
# sortmin(a, b, c, d)

# 14-misol
# a = 1
# mas = []
# i = 0
# while a:
#     i = i + 1
#     a = input("{}-sonni kiriting:".format(i))
#     mas.append((a))
#
#
# def sortmin(mas):
#     for x in range(i):
#         for y in range(i):
#             if mas[x] > mas[y]:  # oldingi masalada < edi shart
#                 k = mas[x]
#                 mas[x] = mas[y]
#                 mas[y] = k
#     print(mas)
#
#
# sortmin(mas)

# 15-misol
# a=float(input("input a:"))
# b=float(input("input b:"))
# c=float(input("input d:"))
# def silljit(a,b,c):
#     aa=a
#     a=b
#     b=c
#     c=aa
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# silljit(a,b,c)


# 16-misol
# a=float(input("input a:"))
# b=float(input("input b:"))
# def ishora(x):
#     if x>0 :
#         print(+1)
#     elif x==0:
#         print(0)
#     else:
#         print(-1)
#
# ishora(a)
# ishora(b)

# 17-misol
# a=float(input("input a:"))
# b=float(input("input b:"))
# c=float(input("input d:"))
# def KvIldizlariSoniniTop(a,b,c,):
#     D=b**2-4*a*c
#     if D>0:
#         print("ikkita ildizga ega")
#     elif D==0:
#         print("Bitta ildizga ega")
#     else:
#         print("haqiqiy ildizlarga ega emas")
#
# KvIldizlariSoniniTop(a,b,c)

# 18-misil
# a=float(input("input r:"))
# def DoiraYuzi(r):
#     import math
#     s=math.pi*r**2
#     print("{} radiusli doiraning yuzasi s={}".format(r,s))
# DoiraYuzi(a)

# 19-misol
# R = float(input("input R:"))
# r = float(input("input r:"))
#
#
# def QolganYuza(R, r):
#     import math
#     s = math.pi * (abs(r ** 2 - R ** 2))
#     print("{} va {} radiusli doiralar orasidagi yuzasi s={}".format(R, r, s))
#
#
# QolganYuza(R, r)

# 20-misol
# R = float(input("input a:"))
# r = float(input("input b:"))
# def UchburchakPerimetrXisobla(a,b):
#     import math
#     p=a+b+math.sqrt(a**2+b**2)
#     print("{} va {} katetga ega ucburchak perimetri P={}".format(a,b,p))
# UchburchakPerimetrXisobla(R,r)

# 21-misol
# R = float(input("input a:"))
# r = float(input("input b:"))
# def sumRange(a,b):
#     if a>=b:
#         print("natija:",0)
#     else:
#         s=(a+b-1)*(b-a)/2
#         print("{} va {} sonlari orasidagi sonlar yig'indisi s={}".format(a,b,s))
# sumRange(R,r)

# 22-misol
# a = float(input("input a:"))
# c = input("input amall +=1, -=2, *=3, 4=/:")
# b = float(input("input b:"))
# def Calc(a,c,b):
#     ishora={
#         "1": a+b,
#         "2": a-b,
#         "3": a*b,
#         "4": a/b
#     }
#     s=ishora[c]
#     print(s)
#
# Calc(a,c,b)

# 23misol
# x=int(input("input x:"))
# y=int(input("input y:"))
# def Quarter(x,y):
#     if x>0 and y>0 :
#         print("1-chorak")
#     if x<0 and y>0:
#         print("2-chorak")
#     if x>0 and y<0 :
#         print("4-chorak")
#     if x<0 and y<0 :
#         print("3-chorak")
#     if x==0 and y==0 :
#         print("kordinata bishida")
# Quarter(x,y)

# 24-misol
# a=int(input("input a:"))
# def jufttoq(a):
#     if a%2==1:
#         print("Trure")
#     else:
#         print("False")
# jufttoq(a)

# 25-misol
# a=int(input("input a:"))
# def isSquare(x):
#     i=0
#     c=True
#     while(i<x):
#         if (i*i==x):
#             print(c)
#             c=False
#         i=i+1
#     if c:
#         print("False")
# isSquare(a)

# 26-misol
# a=int(input("input a:"))
# def isSquare(x):
#     while(x>1):
#         x=x/5
#     if x==1:
#         print("True")
#     else:
#         print("False")
# isSquare(a)

# 27-misol
# a=int(input("input n:"))
# k=int(input("input pow k:"))
# def isSquare(x,k):
#     while(x>1):
#         x=x/k
#     if x==1:
#         print("True")
#     else:
#         print("False")
# isSquare(a,k)

# 28-misol
# 24-misolga qralsin


# 30-misol
# k=int(input("sonni kiriting k:"))
# n=int(input("qaysi xonadagi raqami chiqsin n:"))
# def Diget(k,n):
#     for x in range(n):
#         s=k%10
#         k=k//10
#     print(s)
#
# Diget(k,n)


# funksiyaga oid qo'shimcha masalalar

# 37-misol
# a = int(input("input a:"))
# b = int(input("input pow a, b:"))
#
#
# def pow(a, b):
#     s = 1
#     for i in range(b):
#         s = s * a
#     print(f"a^b={s}")
#
#
# pow(a, b)

# 38-misol
# a = int(input("input a:"))
# b = int(input("input pow a, b:"))
#
#
# def pow(a, b):
#     s = 1
#     if b > 0:
#         for i in range(b):
#             s = s * a
#         print(f"a^b={s}")
#     else:
#         for i in range(abs(b)):
#             s = s * 1 / a
#         print(f"a^b={s}")
#
#
# pow(a, b)

# 40-misol
# x = int(input("input x:"))
# e = int(input("input pow x, e:"))
#
#
# def exp1(x,e):
#     faktorial = 1
#     powx = 1
#     s = 1
#     for i in range(1, e + 1):
#         faktorial = faktorial * i
#         powx = powx * x
#         s = s + powx / faktorial
#     print(f"s={s}")
#
#
# exp1(x, e)

# 41-misol
# x = float(input("input x:"))
# e = int(input("input pow x, e:"))
#
#
# def sin1(x, e):
#     powx = x
#     s = x
#     for i in range(1, e + 1):
#         faktorial = 1
#         for j in range(1,2*i+2):
#             faktorial=faktorial*j
#         powx = powx * x * x * (-1)
#         s = s + powx / faktorial
#
#     print(f"sinx={s}")
#
#
# sin1(x, e)

# 42-misol
# x = float(input("input x:"))
# e = int(input("input pow x, e:"))
#
#
# def cos1(x, e):
#     powx = 1
#     s = 1
#     for i in range(1, e + 1):
#         faktorial = 1
#         for j in range(1,2*i+1):
#             faktorial=faktorial*j
#         powx = powx * x * x * (-1)
#         s = s + powx / faktorial
#
#     print(f"cosx={s}")
#
#
# cos1(x, e)

# 43-misol
# x = float(input("input |x|<1 :"))
# e = int(input("input pow x, e:"))
#
#
# def Ln1(x, e):
#     s = 0
#     powx = -1
#     for i in range(1, e + 1):
#         powx = powx * (-1) * x
#         s = s + powx / i
#     print(f"ln(1+{x})={s}")
#
#
# Ln1(x, e)

# 44-misol
# x = float(input("input |x|<1 :"))
# e = int(input("input pow x, e:"))
#
#
# def arctg1(x, e):
#     powx = x
#     s = x
#     for i in range(1, e + 1):
#         powx = powx * x * x * (-1)
#         s = s + powx / (2 * i + 1)
#     print(f"arctg({x})={s}")
#
#
# arctg1(x, e)

# 45-misol
# x = float(input("input |x|<1 :"))
# a = int(input("input  a:"))
# e = int(input("input pow x, e:"))
#
#
# def pow4(x, a, e):
#     s = 1
#     powx = 1
#     faktorial = 1
#     aa = a
#     for i in range(1, e + 1):
#         powx = powx * x
#         faktorial = faktorial * i
#         s = s + aa * powx / faktorial
#         aa = aa * (a - i)
#     print("s=", s)
#
#
# pow4(x, a, e)

# 50-misol
# t = int(input("print t (sekund) :"))
#
#
# def Time(t):
#     tsekund = t % 60
#     tminut = t // 60 - 60 * (t // 3600)
#     tsoat = t // 3600
#     print(f"{t} sekund = {tsoat}soat:{tminut}minut:{tsekund}minut")
#
#
# Time(t)

# 56-misol
# bu misolni yechishda koplikis sondan to'plamidan faydalandik
# z = complex(float(input("X1 kiriting:")), float(input("Y1 kiriting")))
# z2 = complex(float(input("X2 kiriting:")), float(input("Y2 kiriting")))
#
#
# def masofa(z, z2):
#     print(abs(z - z2))
#
#
# masofa(z, z2)

# 57-misol
# bu misolni yechishda koplikis sondan to'plamidan faydalandik
# z = complex(float(input("X1 kiriting:")), float(input("Y1 kiriting")))
# z2 = complex(float(input("X2 kiriting:")), float(input("Y2 kiriting")))
# z3 = complex(float(input("X3 kiriting:")), float(input("Y3 kiriting")))
#
#
# def masofa(z, z2, z3):
#     print(abs(z - z2) + abs(z - z3) + abs(z2 - z3))
#
#
# masofa(z, z2, z3)
