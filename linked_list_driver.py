#  CS 3B Intermediate Software Design in Python
#  Lab # 4
#  Module: Abstract Data Types
#  Description: Driver class to load linked list and execute.
#  Development Env:  Windows 10
#  Version:  Python 3.11
#  Module filename:  aldosiswantoa4.py
#  Date:  3/2/23
#

from aldosiswantoLL import LinkedList, LinkedListIterator


def main():
    # demo using default constructor
    print("LinkedList demo using default constructor")
    ll_object = LinkedListIterator(LinkedList())
    iterator = iter(ll_object)

    print("Default LinkedList demo length: " + str(ll_object.ll.length()))
    print("Displaying all items..")
    for value in iterator:
        print(value)

    # demo using parameterized constructor
    print("\nLinkedList demo using parameterized constructor, item value: 1")
    ll_object = LinkedListIterator(LinkedList(1))
    iterator = iter(ll_object)

    print("Parameterized LinkedList demo length: " + str(
        ll_object.ll.length()))
    print("Displaying all items..")
    for value in iterator:
        print(value)

    # appending values
    print("\nAppending values 2, 3, 4, 5")
    ll_object.ll.append(2)
    ll_object.ll.append(3)
    ll_object.ll.append(4)
    ll_object.ll.append(5)

    # displaying all values
    print("\nDisplaying all items..")
    for value in iterator:
        print(value)

    # demo get first item
    print("\nDemo get 1st item..")
    print(ll_object.ll.get(1))

    # demo delete 2nd item
    print("\nDemo delete 2nd item..")
    ll_object.ll.delete(2)
    print("LinkedList demo length: " + str(ll_object.ll.length()))
    print("Displaying all items..")
    for value in iterator:
        print(value)

    # demo insert item on 3rd position
    print("\nDemo insert 9 on the 3rd position..")
    ll_object.ll.insert(3, 9)
    print("LinkedList demo length: " + str(ll_object.ll.length()))
    print("Displaying all items..")
    for value in iterator:
        print(value)

    # demo pop linked list
    print("\nDemo pop linked list..")
    popped_value = ll_object.ll.pop()
    print("Popped Value: " + str(popped_value))
    print("LinkedList demo length: " + str(ll_object.ll.length()))
    print("Displaying all items..")
    for value in iterator:
        print(value)


if __name__ == "__main__":
    main()

"""
LinkedList demo using default constructor
Default LinkedList demo length: 0
Displaying all items..

LinkedList demo using parameterized constructor, item value: 1
Parameterized LinkedList demo length: 1
Displaying all items..
1

Appending values 2, 3, 4, 5

Displaying all items..
1
2
3
4
5

Demo get 1st item..
1

Demo delete 2nd item..
LinkedList demo length: 4
Displaying all items..
1
3
4
5

Demo insert 9 on the 3rd position..
LinkedList demo length: 5
Displaying all items..
1
3
9
4
5

Demo pop linked list..
Popped Value: 5
LinkedList demo length: 4
Displaying all items..
1
3
9
4

Process finished with exit code 0
"""