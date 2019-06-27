#!/usr/bin/python

def recursion(n):
	if n == 1:
		return 1
	else:
		return (n * recursion(n-1))

def main():
	fac = recursion(4)
	print(fac)

main()
