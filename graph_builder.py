from vertex import Vertex


def create_graph():
    """creates a graph based off of user input."""

    graph = []

    name = input("Add an initial vertex name: ")
    v1 = Vertex(name)
    graph.append(v1)

    while input("Would you like to add another vertex? Y/N: ") == "Y":

        name = input("Add a vertex name: ")

        vn = Vertex(name)   # vertex n

        adjacencies = input("What existing vertices would you like this vertex to be connected to? Please enter their names separated only by a single space. ")

        adjacencies = adjacencies.split()  # this is now a list of adjacent vertex names

        for adjacency in adjacencies:

            a = Vertex(adjacency)
            vn.add_adjacency(a)
            a.add_adjacency(vn)

        graph.append(vn)

    return graph

def set_weights(graph):

    while input("Would you like to weight any of the edges on this graph? Y/N: ") == 'Y':

        verts = input("Enter the two vertices you would like to weight the edge between separated by spaces: ")
        verts = verts.split()
        v1 = verts[0]
        v2 = verts[1]
        weight = int(input(f"Now enter the weight you would like to give the edge connecting {v1} and {v2}: "))

        for v in graph:

            if v.name == v1:

                v.set_weight(v2, weight)

            if v.name == v2:

                v.set_weight(v1, weight)

    return graph

def print_graph(graph):

    for v in graph:

        print(v)


def main():

    graph = create_graph()
    weighted_graph = set_weights(graph)
    print_graph(weighted_graph)


if __name__ == "__main__":
    main()



