from trees import *


def make_tree(CEO, direct_reports):
    org_chart = Tree(Node(CEO, direct_reports))
    return org_chart


if __name__ == "__main__":
    org_chart = make_tree("Bob", ["Jim", "Sara", "Mike"])
    print(org_chart)
    print(org_chart.root.children)
