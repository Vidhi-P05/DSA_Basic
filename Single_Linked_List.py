#Single Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self):
        val = int(input("Enter the value: "))
        if self.head is None:
            self.head = Node(val)
        else:
            it = self.head
            while it.next is not None:
                it = it.next
            it.next = Node(val)

    def insertAtBegin(self):
        val = int(input("Enter the value: "))
        if self.head is None:
            self.head = Node(val)
        else:
            temp = Node(val)
            temp.next = self.head
            self.head = temp

    def deleteAtBegin(self):
        if self.head is None:
            print("The list is empty. Cannot delete.")
            return -1
        temp = self.head
        self.head = self.head.next
        return temp.val

    def deleteAtEnd(self):
        if self.head is None:
            print("The list is empty. Cannot delete.")
            return -1
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp.val
        else:
            it = self.head
            while it.next.next is not None:
                it = it.next
            temp = it.next
            it.next = None
            return temp.val

    def deleteByElement(self):
        target = int(input("Enter the target no: "))
        if self.head is None:
            print("The list is empty. Cannot delete.")
            return
        elif self.head.val == target:
            print(f"Element {target} found at the beginning. Deleting...")
            self.head = self.head.next
            return
        else:
            p = self.head
            q = None
            while p is not None and p.val != target:
                q = p
                p = p.next
            if p is not None and p.val == target:
                print(f"Element {target} found. Deleting...")
                q.next = p.next
            else:
                print(f"Element {target} not found. Could not delete.")

    def displayList(self):
        it = self.head
        while it is not None:
            print(it.val, end='->')
            it = it.next
        print("None")

class Menu:
    def __init__(self):
        self.linked_list = LinkedList()

    def show_menu(self):
        while True:
            print("Menu for Linked List Operations".center(124, '-'))
            print("1. Insert at the beginning")
            print("2. Insert at the end")
            print("3. Delete at the beginning")
            print("4. Delete at the end")
            print("5. Delete a particular element")
            print("6. Display List")
            print("7. Exit")
            choice = int(input("Enter the operation no: "))
            match choice:
                case 1:
                    self.linked_list.insertAtBegin()
                case 2:
                    self.linked_list.insertAtEnd()
                case 3:
                    print(f"Deleted element: {self.linked_list.deleteAtBegin()}")
                case 4:
                    print(f"Deleted element: {self.linked_list.deleteAtEnd()}")
                case 5:
                    self.linked_list.deleteByElement()
                case 6:
                    self.linked_list.displayList()
                case 7:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid choice.")

m = Menu()
while True:
    m.show_menu()