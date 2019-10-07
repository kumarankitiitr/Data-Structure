#include<iostream>
using namespace std;
#define MAX_SIZE 101
class stack{
	public:
	int A[MAX_SIZE];
	int top = -1;

	void push(int x){
		if(top == MAX_SIZE-1){
			cout<<"Error: stack overflow\n";
			return;
		}
		A[++top] = x;
	}

	void pop(){
		if(top == -1){
			cout<< "Error: No element to pop\n";
			return;
		}
		top--;
	}

	int Top(){
		return A[top];
	}

	void printstack(){
		for(int i=0; i<= top; i++){
			cout<<A[i]<<" ";
			
		}
		cout<<endl;
	}
};

int main(){
stack s;
s.push(7); 
s.push(3);
s.push(8);
s.printstack(); // 7 3 8
s.pop(); // 8
s.printstack();
}
