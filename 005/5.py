# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

start=2520

def divisible(n):
	pass
	flag=0

	for x in [11,12,13,14,15,16,17,18,19,20]:
		pass
		if n%x!=0:
			pass
			flag=-1
			break

	if flag!=-1:
		pass
		return True
	else :
		return False

while True:
	pass
	if divisible(start):
		pass
		break
	else:
		start+=1

print start