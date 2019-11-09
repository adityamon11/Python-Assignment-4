from functools import *;
from math import sqrt;
def PrimeNos(n1):
	flg=0
	for i in range(2,int(sqrt(n1))+1):
		if(n1%i==0):
			flg=1;
	if(flg==0):
		return n1;

def MapMul(n1):
	return n1*2;

def Reducer(n1,n2):
	if(n1>n2):
		return n1
	else:
		return n2


def main():
	arr = list();
	x = int(input("Enter the number of elements "));
	for i in range(0,x):
		arr.append(int(input("Enter the number ")));
	
	filteredList = list(filter(PrimeNos,arr));
	mappedList = list(map(MapMul,filteredList));
	red = int(reduce(Reducer,mappedList));
	print(filteredList);
	print(mappedList);
	print(red);
	
if __name__ == '__main__':
	main();
