class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def add(self, item):
        """指针头部添加元素"""
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node  # 空列表head指向新节点
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        """指定位置插入元素"""
        if index <= 0:
            """指定位置在第一个元素之前，在头部插入"""
            self.add(item)
        elif index > (self.length() - 1):
            """指定位置超过尾部，在尾部插入"""
            self.append(item)
        else:
            # 创建元素节点
            node = Node(item)
            cur = self._head
            # 循环到需要插入的位置
            for i in range(index - 1):
                cur = cur.next  # 循环到想插入位置的前一位
            node.next = cur.next  # 承接被顶替的位置
            cur.next = node  # 接上被顶替的前面一位

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == item:
                if not pre:  # 如果第一个就是删除的节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()


if __name__ == '__main__':
    link_list = SingleLinkList()
    # 向链表尾部添加数据
    for i in range(5):
        link_list.append(i)
    # 向头部添加数据
    link_list.add(6)
    # 遍历链表数据
    for i in link_list.items():
        print(i, end='\t')
    # 链表数据插入数据
    link_list.insert(3, 9)
    print('\n', list(link_list.items()))
    # 删除链表数据
    link_list.remove(0)
    # 查找链表数据
    print(link_list.find(4))
