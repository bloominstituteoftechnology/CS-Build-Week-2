class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        linked lists are assumed to be non-empty due to problem constraints
        digits are stored in reverse order (first is ones place, second is tens, etc)

        cycle through the linked list while keeping track of current decimal place
        """
        def linked_list_to_decimal(node):
            # value = 0
            # decimal_place = 1
            # while node is not None:
            #     value += node.val * decimal_place
            #     decimal_place *= 10
            #     node = node.next
            # return value
            value = ""
            while node is not None:
                value = str(node.val) + value
                node = node.next
            return int(value)

        def decimal_to_linked_list(num):
            # nodes = []
            # # while num / (decimal_place * 10)  > 0:
            # while num >= 10:
            #     nodes.append(ListNode(num % (10)))
            #     num //= 10
            # nodes.append(ListNode(num))
            # for i in range(len(nodes) - 1):
            #     nodes[i].next = nodes[i + 1]
            # return nodes[0]
            nodes = []
            num = str(num)
            for i in range(len(num)):
                nodes.append(ListNode(int(num[len(num) - i - 1])))
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            return nodes[0]

        n1 = linked_list_to_decimal(l1)
        n2 = linked_list_to_decimal(l2)

        sum = n1 + n2

        return decimal_to_linked_list(sum)


def make_list(nested_arr):
    l1 = ListNode(nested_arr[0][0])
    l2 = ListNode(nested_arr[1][0])
    l1_end = l1
    l2_end = l2
    for item in nested_arr[0][1:]:
        node = ListNode(item)
        l1_end.next = node
        l1_end = node
    for item in nested_arr[1][1:]:
        node = ListNode(item)
        l2_end.next = node
        l2_end = node
    return l1, l2


def print_list(ll):
    node = ll
    val = []
    while node is not None:
        # print(node.val, end=" -> ")
        val.append(node.val)
        node = node.next
    # print("None")
    print(val)


test = Solution()

ex1 = [
    [2, 4, 3],
    [5, 6, 4]
]
ex2 = [
    [1, 2, 3],
    [3, 4, 5]
]

sol1 = test.addTwoNumbers(*make_list(ex1))
sol2 = test.addTwoNumbers(*make_list(ex2))

print_list(sol1)
print_list(sol2)