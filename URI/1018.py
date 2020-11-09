v = int(input())
print(v)
print("{} nota(s) de R$ 100,00".format(v//100))
r = v % 100
print("{} nota(s) de R$ 50,00".format(r//50))
r = r % 50
print("{} nota(s) de R$ 20,00".format(r//20))
r = r % 20
print("{} nota(s) de R$ 10,00".format(r//10))
r = r % 10
print("{} nota(s) de R$ 5,00".format(r//5))
r = r % 5
print("{} nota(s) de R$ 2,00".format(r//2))
r = r % 2
print("{:.0f} nota(s) de R$ 1,00".format(r))
