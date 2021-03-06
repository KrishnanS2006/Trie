# Class for a Trie
class Trie:
    def __init__(self):
        self.start = TrieElement("", None)  # Sets the starting Trie Element

    # Adds to the Trie
    def add(self, name):
        if not isinstance(name, str):
            return False
        if len(name) < 1:
            return False
        current = self.start
        if len(name) == 1:
            self.start.add(name)
            return
        for letter in name[:-1]:
            next = current.next(letter)
            if not next:
                current.add(letter)
                current = current.next(letter)
            else:
                current = next
        current.add(name[-1])
        return True

    # Deletes from the Trie
    def delete(self, name):
        current = self.start
        for letter in name[:-1]:
            current = current.next(letter)
            if not current:
                return False
        current.delete(name[-1])
        return True

    # Searches in the Trie
    def search(self, name):
        current = self.start
        for letter in name:
            current = current.next(letter)
            if not current:
                return False
        return True

    # Generates Autocomplete
    def autocomplete(self, name):
        current = self.start
        for letter in name:
            current = current.next(letter)
            if not current:
                return False, False
        return True, [n.name for n in current.next()]

    # Displays the Trie
    def display(self, current=None, level=0, special=False):
        if not current:
            current = self.start
            to_print = "The Current Trie:"
        else:
            if len(current.parent.children) < 2:
                to_print = " " + current.__repr__()
            else:
                to_print = " " * (level - 1) + "" + current.__repr__()
        if not current.has_children:
            to_print = " " + current.__repr__()
            if special:
                return "\n" + " " * (level - 1) + to_print
            else:
                return to_print
        else:
            for x, child in enumerate(current.children):
                if len(child.parent.children) > 1 and x != 0 and not child.parent == self.start:
                    to_print += self.display(child, level + 1, True)
                elif child.parent == self.start:
                    to_print += "\n" + self.display(child, level + 1)
                else:
                    to_print += self.display(child, level + 1)
            if special:
                return "\n" + " " * (level - 1) + to_print
            else:
                return to_print

    def __repr__(self):
        return self.display()


# Class for an element in the Trie
class TrieElement:
    # Sets the name, children, and parent
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.has_children = False
        self.parent = parent

    # Returns a child or all its children
    def next(self, name=None):
        if not name:
            return self.children
        for child in self.children:
            if child.name == name:
                return child
        return None

    # Adds a child
    def add(self, name):
        if not self.has_children:
            self.has_children = True
        if name in [n.name for n in self.children]:
            return
        self.children.append(TrieElement(name, self))

    # Deletes a child
    def delete(self, name):
        for x, child in enumerate(self.children):
            if child.name == name:
                del self.children[x]
        if len(self.children) < 1:
            self.has_children = False

    def __repr__(self):
        return self.name


# Some testing code
if __name__ == "__main__":
    trie = Trie()
    trie.add("a")
    trie.add("b")
    trie.add("at")
    trie.add("al")
    trie.add("alt")
    trie.add("alte")
    trie.add("alter")
    trie.add("ate")
    trie.add("ar")
    trie.add("art")
    trie.add("are")
    trie.add("aren")
    trie.add("arent")
    trie.add("by")
    trie.add("bye")
    trie.add("bo")
    trie.add("bol")
    trie.add("bold")
    trie.delete("alt")
    print(trie)
