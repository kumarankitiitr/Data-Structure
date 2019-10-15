#include<iostream>
using namespace std;
class BstNode{
    public:
        int data;
        BstNode* left;
        BstNode* right;

        BstNode(int data){
            this->data = data;
            this->left = nullptr;
            this->right = nullptr;
        }
};

class BstTree{
    public:
        BstNode* root;

        BstTree(){
            this->root = nullptr;
        }


};
BstNode* Insert(BstNode* root,int node_data){
    BstNode* newnode = new BstNode(node_data);
    if(root == nullptr){
        // empty tree
        root = newnode;
    }
    else if(node_data <= root->data){
        root->left = Insert(root->left, node_data);
    }
    else{
        root->right = Insert(root->right, node_data);
    }
    return root;

}

bool search(BstNode* root, int data){
    if(root == nullptr) return false;
    else if(root->data == data) return true;
    else if(data <= root->data) return search(root->left, data);
    else return search(root->right, data);
}

int main(){
    BstTree t;
    BstNode* root = nullptr;
    root = Insert(t.root, 15);
    root = Insert(root,10);
    root = Insert(root,20);
    root = Insert(root,25);
    root = Insert(root,8);
    root = Insert(root,12);
    cout<< search(root, 25)<<endl;
    cout<< search(root, 48)<<endl;
    
}
