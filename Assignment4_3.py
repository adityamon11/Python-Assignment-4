from functools import *;
def GreaterNos(n1):
	if (n1>=70 and n1<=90):
		return n1;

def MapAdder(n1):
	n1=n1+10;
	return n1;

def Reducer(n1,n2):
	return n1*n2;


def main():
	arr = list();
	x = int(input("Enter the number of elements "));
	for i in range(0,x):
		arr.append(int(input("Enter the number ")));
	
	filteredList = list(filter(GreaterNos,arr));
	mappedList = list(map(MapAdder,filteredList));
	red = int(reduce(Reducer,mappedList));
	print(filteredList);
	print(mappedList);
	print(red);
	
if __name__ == '__main__':
	main();
