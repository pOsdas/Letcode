class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.root = Node(0)
        self.root.next = self.root
        self.root.prev = self.root
        self.key_count = {}
        self.count_bucket = {}

    def _add_node_after(self, new_node, prev_node):
        """Adding a new node after opening"""
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node):
        """Delete node from list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def inc(self, key: str) -> None:
        if key in self.key_count:
            current_count = self.key_count[key]
            new_count = current_count + 1
            self.key_count[key] = new_count
            current_node = self.count_bucket[current_count]

            if new_count not in self.count_bucket:
                new_node = Node(new_count)
                self.count_bucket[new_count] = new_node
                self._add_node_after(new_node, current_node)
            else:
                new_node = self.count_bucket[new_count]

            new_node.keys.add(key)
            current_node.keys.remove(key)

            if not current_node.keys:
                self._remove_node(current_node)
                del self.count_bucket[current_count]
        else:
            self.key_count[key] = 1
            if 1 not in self.count_bucket:
                new_node = Node(1)
                self.count_bucket[1] = new_node
                self._add_node_after(new_node, self.root)
            self.count_bucket[1].keys.add(key)

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return

        current_count = self.key_count[key]
        current_node = self.count_bucket[current_count]

        if current_count == 1:
            del self.key_count[key]
            current_node.keys.remove(key)
        else:
            new_count = current_count - 1
            self.key_count[key] = new_count

            if new_count not in self.count_bucket:
                new_node = Node(new_count)
                self.count_bucket[new_count] = new_node
                self._add_node_after(new_node, current_node.prev)
            else:
                new_node = self.count_bucket[new_count]

            new_node.keys.add(key)
            current_node.keys.remove(key)

        if not current_node.keys:
            self._remove_node(current_node)
            del self.count_bucket[current_count]

    def getMaxKey(self) -> str:
        if self.root.prev == self.root:
            return ""
        return next(iter(self.root.prev.keys))

    def getMinKey(self) -> str:
        if self.root.next == self.root:
            return ""
        return next(iter(self.root.next.keys))
