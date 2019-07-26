def swapnibble(x):
	
	return ( (x & 15) <<4 | (x & 240) >> 4 )



def main():
	x=100
	y=swapnibble(x)
	print(y)


main()
