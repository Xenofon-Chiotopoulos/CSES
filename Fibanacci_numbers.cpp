#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int a{0},b{1},count{},c{};
	cin >> count;
	for (int i = 0; i < count; ++i)
	{
		c = b;
		b = a + b;
		a = c;
	}
	int modulo = pow(10,9)+7;
	cout << a % modulo << endl;
}