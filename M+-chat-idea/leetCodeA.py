# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# הגדרת צומת בודד ברשימה מקושרת
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# פונקציה שמחברת שתי רשימות מקושרות (שמייצגות מספרים בסדר הפוך)
def sum2(firstList, seonedList):
    dummy = ListNode()        # ראש פיקטיבי לרשימת התוצאה
    current = dummy           # מצביע שיבנה את הרשימה
    carry = 0                 # משתנה להעברת עודף (כמו 1 ב-9+2 = 11)

    while firstList or seonedList or carry:
        v1 = firstList.val if firstList else 0
        v2 = seonedList.val if seonedList else 0

        total = v1 + v2 + carry
        carry = total // 10         # ספרת העשרות (אם יש)
        digit = total % 10          # ספרת היחידות

        current.next = ListNode(digit)  # יצירת צומת חדש בתוצאה
        current = current.next

        if firstList:
            firstList = firstList.next
        if seonedList:
            seonedList = seonedList.next

    return dummy.next  # מחזירים את הרשימה בלי הדמי

# פונקציה להדפסת רשימה מקושרת בצורה ידידותית
def listnode_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
# דוגמה: 342 = 2 → 4 → 3
l1 = ListNode(2, ListNode(4, ListNode(3)))
# דוגמה: 465 = 5 → 6 → 4
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = sum2(l1, l2)
print(listnode_to_list(result))  # פלט: [7, 0, 8]


