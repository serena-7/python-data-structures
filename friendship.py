from graphs import *


def make_simple_friendship(friends):
    graph = FriendGraph()
    people_nodes = [Node(friend) for friend in friends]
    graph.add_people(people_nodes)
    for i in range(len(people_nodes)):
        for j in range(i + 1, len(people_nodes)):
            graph.set_friends(people_nodes[i], people_nodes[j])

    return graph


if __name__ == "__main__":
    friendships = make_simple_friendship(["Jamie", "Mary", "Kimmy"])
    print(friendships)
