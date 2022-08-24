# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        Mid=self.mid(head);
        Mid_next=Mid.next;
        Mid.next=None;
        root=head;
        Reverse=self.reverse(Mid_next);
        Traverse=self.traverse(root,Reverse);
        return Traverse;
    
    def traverse(self,root,Reverse):
        curA=root;
        curB=Reverse;
        while curB:
            if curA.val!=curB.val:
                return False;
            curA=curA.next;
            curB=curB.next;
        return True;
        
    def reverse(self, Mid_next):
        previous=None;
        current=Mid_next;
        while current:
            temp=current.next;
            current.next=previous;
            previous=current;
            current=temp;
        return previous;
        
        
        
        
    def mid(self,head):
        slow=head;
        fast=head;
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow;
            
        