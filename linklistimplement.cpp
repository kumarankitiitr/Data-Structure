#include<iostream>
using namespace std;
class node
{
	public:
		int data;
		node* next;

		node(int node_data){
			this -> data = node_data;
			this -> next = nullptr;
	}
};

class queue
{
	public:
	node* front;
	node* rear;

	queue(){
		this ->front = nullptr;
		this -> rear = nullptr;
	}

	void Enqueue(int node_data){
		node* newnode = new node(node_data);
		if(this-> front == nullptr && this->rear == nullptr){
			front = rear = newnode;
		}
		this->rear->next = newnode;
		this->rear = newnode;
	}

	void Dequeue(){
		node* temp = front;
		if(front == nullptr){
			return;
		}
		if(front == rear){
			front = rear = nullptr;
		}
		else
		{
			front = front->next;
		}
		delete temp;
		
	}

	void show(){
		node* temp = front;
		while( temp != nullptr){
			cout<< temp->data << " ";
			temp = temp->next;
		}
		cout<<"\n";
	}

};

int main(){
	queue q;
	q.Enqueue(7);//7
	q.Enqueue(6);//7 6
	q.Enqueue(4);//7 6 4
	q.Enqueue(8);// 7 6 4 8
	q.show();
	q.Dequeue();//6 4 8
	q.show();
}
