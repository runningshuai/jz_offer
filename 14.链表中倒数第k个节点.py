"""
题目描述
输入一个链表，输出该链表中倒数第k个结点。
思路：
1、遍历一遍得到链表长度n，第二次遍历到n-(k-1)就找到了，只有一个指针干活，复杂度2n-k
2、遍历链表只要少走k-1就好了，在未知链表长度时，怎么才能找到这个位置？通过两个指针可以做到
    p1, p2，p1先走k-1,p2原地待命，那么p2就滞后了k-1，也就是少走了k-1。
    p1走k-1后，p2开始走，p1走到末尾p2就走了（p1走的长度 - (k-1),也就是n-(k-1)）

"""


def FindKthToTail(head, k):
    p1, p2 = head, head
    t = 0
    while p1:
        # 走完k-1，第k个p2开始跟着p1走
        if t >= k:
            p2 = p2.next
        p1 = p1.next
        t += 1
    if t < k:
        return None
    return p2