from graph import Graph


class HitsAlgorithmb:
    """
    Hub update : Each node’s Hub score = \Sigma  (Authority score of each node it points to).
    Authority update : Each node’s Authority score = \Sigma  (Hub score of each node pointing to it).
    """

    def __init__(self, n_iteration: int, graph: Graph):
        self.graph = graph
        self.n_iteration = n_iteration
        self.node_cnt = graph.GetNodeCount()

    @staticmethod
    def normalise(hub: dict, auth: dict):
        a = sum(hub.values())
        b = sum(auth.values())
        n_hub = {i: (j / a) for i, j in hub.items()}
        n_auth = {i: (j / b) for i, j in auth.items()}
        return n_hub, n_auth

    def HitsIteration(self, edges: list, old_hub: dict, old_auth: dict):
        hub = {i: 0 for i in range(self.node_cnt)}
        auth = {i: 0 for i in range(self.node_cnt)}
        for i in edges:
            fr, to = i
            hub[fr] += old_auth[to]
            auth[to] += old_hub[fr]
        n_hub, n_auth = self.normalise(hub, auth)
        return n_hub, n_auth

    def calculate(self):
        hub = {i: 1 for i in range(self.node_cnt)}
        auth = {i: 1 for i in range(self.node_cnt)}
        edges = self.graph.GetOrderedEdges()
        for i in range(self.n_iteration):
            hub, auth = self.HitsIteration(edges, hub, auth)
        return hub, auth




if __name__ == '__main__':
    reza = Graph(6, 10)
    # reza.InsertNodes([(1, 0), (2, 0), (3, 0)])
    reza.InsertNodes([(0,1),(1,0),(1,2),(0,2),(2,3),(3,2),(4,3),(5,3),(4,5),(5,4)])
    reza1 = HitsAlgorithmb(10, reza)
    hub, auth = reza1.calculate()
    print("hub :", hub)
    print("auth :", auth)
hubj = {0: 0.18301267010793054, 1: 0.18301267010793054, 2: 0.13397465978413892, 3
: 0.1339746597841389, 4: 0.18301267010793057, 5: 0.18301267010793057}
autjh = {0: 0.10566258026853473, 1: 0.10566258026853473, 2: 0.28867483946293054,
         3: 0.28867483946293054, 4: 0.10566258026853473, 5: 0.10566258026853473}
