#include<iostream>
using namespace std;
class node
{
	public:
		int data;
		node* next;

		node(int node_data){
			this->data = node_data;
			this->next = nullptr;
		}
};

class LinkedList{
	public:
		node* head;

		LinkedList(){
			this -> head = nullptr;
		}

	void insert_node(int node_data){
		node* newnode = new node(node_data);
		if(this->head != nullptr){
			newnode->next = this->head;
		}
		this->head = newnode;

	}
};

void printLinkedList(node* head){
	while(head != nullptr){
		cout<< head-> data << " ";
		head = head -> next;
	}
	cout<<"\n";
}

void Deletenode(node* head, int position){
	node* temp1 = head;
	if(position == 1){
		head = temp1 -> next;// head now points to second node
		delete temp1;
		return;
	}

	for(int i = 0; i< position-2; i++){
		temp1 = temp1->next; // temp1 points to (n-1)th node
	}
	node* temp2 = temp1->next; //nth node
	temp1 -> next = temp2->next; //(n+1)th node
	delete temp2;
}


int main(){
	LinkedList l1;
	l1.insert_node(7); // 7
	l1.insert_node(8); // 8 7
	l1.insert_node(6); // 6 8 7
	l1.insert_node(3); // 3 6 8 7
	printLinkedList(l1.head);
	Deletenode(l1.head, 2); // 6
	printLinkedList(l1.head);


	LinkedList* l2 = new LinkedList;
	l2->insert_node(4); // 4
	l2 -> insert_node(5); // 5 4
	l2 -> insert_node(2); // 2 5 4
	l2 -> insert_node(1); //  1 2 5 4
	printLinkedList(l2 ->head);
	Deletenode(l2->head, 3); // 5
	printLinkedList(l2->head);

}
