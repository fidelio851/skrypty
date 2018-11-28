#!/usr/bin/env python

def main():
	pin = 1234
	if raw_input("Podaj PIN: ") == pin:
		print 'Pin poprawny'
	else:
		print 'PIN niepoprawny'


if __name__ == '__main__':
	main()

