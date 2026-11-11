def Color(G):
    """
    Takes in a graph, returns the coloring of the nodes in dictionary if able to, return None if no such coloring exists.
    """
    coloring = {node: None for node in G}
    colors = [1,2,3]
    def can_color(node,c):
        """
        take in a node and a color to check if the node can take that color.
        """
        for i in G[node]:
            if coloring[i] == c:
                return False
        return True
    
    def backtrack():
        node = None

        for i in G:
            if coloring[i] is None:
                node = i
                break

        if node is None:
            return True
        
        for c in colors:
            if can_color(node,c):
                coloring[node] = c

                if backtrack():
                    return True

                coloring[node] = None
        return False
    if backtrack():
        return  coloring

    return None
