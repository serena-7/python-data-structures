from linked import *


def shorten_word(l1):
    l2 = LinkedList()
    current = l1.head.next
    while current is not None:
        l2.append(current.data)
        current = current.next
    return l2


if __name__ == "__main__":
    l1 = LinkedList()
    l1.append("apple")
    l1.append("berry")
    l1.append("cherry")
    l1.print_list()
    new_list = shorten_word(l1)
    new_list.print_list()
    l1.print_list()
