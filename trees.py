"""Tree class and tree node class."""


class Node():
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


class Tree():
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)

    def total_nodes(self):
        total = 0

        to_visit = [root]

        while len(to_visit) != 0:
            current = to_visit.pop()
            total += 1
            for child in current.children:
                to_visit.append(child)

        return total


if __name__ == '__main__':
    # Make an example tree and search for things in it

    resume = Node("resume.txt", [])
    recipes = Node("recipes.txt", [])
    jane = Node("jane/", [resume, recipes])
    server = Node("server.py", [])
    jessica = Node("jessica/", [server])
    users = Node("Users/", [jane, jessica])
    root = Node("/", [users])

    tree = Tree(root)
    print("server.py = ", tree.find_in_tree("server.py"))  # should find
    print("style.css = ", tree.find_in_tree("style.css"))  # should not find
    print(tree.total_nodes())
