import SinglyLinkedList

if __name__ == 'main':
    Head = SinglyLinkedList()
    Head.addNodeStarting(15)
    Head.addAtEnd(100)
    Head.addNodeStarting(150)
    Head.addAtEnd(1)
    Head.addAtEnd(122)
    Head.printLinkedList()
    Head.findMiddleElement()
    Head.reverseLinkedList()
    Head.printLinkedList()
    Head.rotateLinkedList(3)
    Head.printLinkedList()
    Head.rotateLinkedList(2)
    Head.printLinkedList()