
class Vertex:
    """represents a vertex as in graph theory which are connected by edges."""


    def __init__(self, name, adjacency_list=[]):
        """initializes a vertex object with an adjacency list containing other vertices."""

        self.name = name
        self.adjacency_list = adjacency_list


    def __repr__(self):
        """returns a string representation of this vertex"""

        return_str = f"\n{self.name}\n\n"

        for adjacency in self.adjacency_list:

            if adjacency[0].name != self.name:
            
                return_str += f"{adjacency[0].name} | weight: {adjacency[1]}\n"


        return return_str


    def add_adjacency(self, vertex, weight=1):
        """adds a vertex and weight in a tuple pair to the adjacency list"""

        self.adjacency_list.append([vertex, weight]) # adds an adjacency to the adjacency list as a list

    def set_weight(self, vertex_name, weight):
        """weights an edge on an existing adjacency"""

        for a in self.adjacency_list:

            if a[0].name == vertex_name:
                a[1] = weight

   
    def get_adjacency(self, vertex):
        """returns weight of input vertex if in adjacency list and -1 otherwise"""
        # note: returning -1 in the case of a non-existent adjacency does assume all positive edge weights

        for adjacency in self.adjacency_list:

            if adjacency[0] is vertex:
                
                return adjacency[1]  # returns the weight of the edge connecting this vertex to the inputted vertex

        return -1


        
