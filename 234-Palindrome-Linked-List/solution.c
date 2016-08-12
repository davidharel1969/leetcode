/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int calc_len(struct ListNode* head){
    int ans=0;
    struct ListNode* cur=head;
    while(cur){
        ans++;
        cur=cur->next;
    }
    return ans;
}
struct ListNode* skip_n(struct ListNode* head,int n){
    int i=0;
    struct ListNode* cur=head;
    while(i++!=n)
        cur=cur->next;
    return cur;
}
struct ListNode* reverse(struct ListNode* head){
    struct ListNode* cur=head;
    struct ListNode*last=0;
    while(cur){
        struct ListNode* next=cur->next;
        cur->next=last;
        last=cur;
        cur=next;
    }
    return last;
}
bool is_equal(struct ListNode* a,struct ListNode* b){
    while(a && b){
        printf("%d %d\n",a->val,b->val);
        if (a->val!=b->val)
            return false;
        a=a->next;
        b=b->next;
    }
    return true;
}
void print(struct ListNode* head){
    while(head){
        printf("%d,",head->val);
        head=head->next;
    }
    printf("------\n");
}


bool isPalindrome(struct ListNode* head) {
    if (!head || !head->next) return true;
    int len=calc_len(head);
    printf("n=%d\n",len);
    struct ListNode* before_mid=skip_n(head,len/2-1);
    struct ListNode*mid=before_mid->next;
    before_mid->next=0;
    
    //print(head);
    //print(mid);    
    mid=reverse(mid);
    //print(head);
    //print(mid);
    return is_equal(head,mid);
    
}