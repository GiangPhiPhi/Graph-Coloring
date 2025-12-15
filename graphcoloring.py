import math
import matplotlib.pyplot as plt

"""
graph.txt
0 1 1 0 1 0 
1 0 1 1 0 1
1 1 0 1 1 0
0 1 1 0 0 1
1 0 1 0 0 1
0 1 0 1 1 0

"""
class GraphColoring:
    def __init__(self, adj_matrix, max_colors):
        self.adj_matrix = adj_matrix
        self.n = len(adj_matrix)
        self.max_colors = max_colors

        self.graph = self._build_adj_list() #matrix ke->list ke
        self.current_degree = {v: len(self.graph[v]) for v in self.graph}
        self.colors = {}

    def _build_adj_list(self):
        graph = {}
        for i in range(self.n):
            graph[i] = []
            for j in range(self.n):
                if self.adj_matrix[i][j] == 1:
                    graph[i].append(j)
        return graph
    #dinh chua to mau
    def _get_uncolored_nodes(self):
        return [v for v in self.graph if v not in self.colors]

    def _select_node(self):
        # chon dinh co bac lon nhat, neu bang nhau thi chon dinh co chi so nho hon
        return max(
            self._get_uncolored_nodes(),
            key=lambda x: (self.current_degree[x], -x)
        )
    #gan mau
    def _get_available_color(self, node):
        forbidden = {self.colors[n] for n in self.graph[node] if n in self.colors}
        for c in range(1, self.max_colors + 1):
            if c not in forbidden:
                return c
        return None

    def color_graph(self):
        print("bat dau to mau do thi")
        #den khi to het dinh
        while len(self.colors) < self.n:
            node = self._select_node()
            color = self._get_available_color(node)

            if color is None:
                print(f"khong the to mau dinh {node} voi {self.max_colors} mau")
                return False
            #gan mau
            self.colors[node] = color
            print(f"chon dinh {node} bac {self.current_degree[node]} to mau {color}")

            print(f"ha bac cac dinh ke cua {node}:")
            #giam bac dinh ke
            for neighbor in self.graph[node]:
                if neighbor not in self.colors:
                    old = self.current_degree[neighbor]
                    self.current_degree[neighbor] -= 1
                    print(f"  dinh {neighbor}: {old} -> {self.current_degree[neighbor]}")

            self.current_degree[node] = 0
            print("_" * 30)

        return True

    def print_result(self):
        print("\nket qua to mau:")
        for v in sorted(self.colors):
            print(f"dinh {v}: mau {self.colors[v]}")

    def draw_graph(self):
        if not self.colors:
            print("do thi chua duoc to mau")
            return

        radius = 3
        positions = {}

        for i in range(self.n):
            angle = 2 * math.pi * i / self.n
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            positions[i] = (x, y)

        # ve canh
        for u in self.graph:
            for v in self.graph[u]:
                if u < v:
                    x1, y1 = positions[u]
                    x2, y2 = positions[v]
                    plt.plot([x1, x2], [y1, y2], color="black")

        # ve dinh
        for v in range(self.n):
            x, y = positions[v]
            plt.scatter(x, y, s=800, c=f"C{self.colors[v]}")
            plt.text(x, y, str(v), ha="center", va="center", color="white")

        plt.title("ket qua to mau do thi")
        plt.axis("off")
        plt.show()


def read_adj_matrix_from_file(filename):
    matrix = []
    with open(filename, "r") as f:
        for line in f:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    return matrix


def main():
    filename = 'graph.txt'
    k = int(input("nhap so mau k: "))

    adj_matrix = read_adj_matrix_from_file(filename)

    solver = GraphColoring(adj_matrix, k)
    success = solver.color_graph()

    if success:
        solver.print_result()
        solver.draw_graph()
    else:
        print("to mau that bai")


if __name__ == "__main__":
    main()
