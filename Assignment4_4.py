from functools import *;
def EvenNos(n1):
	if (n1%2==0):
		return n1;

def MapMul(n1):
	return n1*n1;

def Reducer(n1,n2):
	return n1+n2;


def main():
	arr = list();
	x = int(input("Enter the number of elements "));
	for i in range(0,x):
		arr.append(int(input("Enter the number ")));
	
	filteredList = list(filter(EvenNos,arr));
	mappedList = list(map(MapMul,filteredList));
	red = int(reduce(Reducer,mappedList));
	print(filteredList);
	print(mappedList);
	print(red);
	
if __name__ == '__main__':
	main();
