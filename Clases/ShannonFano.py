class Nodo:
    def __init__(self, prob, symbol=None):
        self.prob = prob
        self.symbol = symbol
        self.left = None
        self.right = None


class ShannonFano:
    def __init__(self):
        self.codes = {}

    def divide(self, prob_list):
        total = sum(prob_list)
        half = total / 2
        curr_sum = 0
        index = 0
        prev_diff = abs(2 * half)

        for prob in prob_list:
            curr_sum += prob
            if abs(total - 2 * curr_sum) < prev_diff:
                prev_diff = abs(total - 2 * curr_sum)
                index += 1
            else:
                break
        return index

    def codificar_recursivo(self, node, code=''):
        if node.left is None and node.right is None:
            self.codes[node.symbol] = code
            return

        if node.left is not None:
            self.codificar_recursivo(node.left, code + '0')
        if node.right is not None:
            self.codificar_recursivo(node.right, code + '1')

    def codificar(self, symbols_probs):
        symbols_probs.sort(key=lambda x: x[1], reverse=True)
        symbols = [item[0] for item in symbols_probs]
        probs = [item[1] for item in symbols_probs]

        root = Nodo(sum(probs))
        nodes = [Nodo(prob, symbol) for symbol, prob in symbols_probs]

        while len(nodes) > 1:
            index = self.divide([node.prob for node in nodes])
            left_nodes = nodes[:index]
            right_nodes = nodes[index:]

            left_prob = sum(node.prob for node in left_nodes)
            right_prob = sum(node.prob for node in right_nodes)

            left_node = Nodo(left_prob)
            left_node.left = left_nodes[0] if len(left_nodes) == 1 else Nodo(left_prob)
            left_node.right = None if len(left_nodes) == 1 else left_nodes[-1]

            right_node = Nodo(right_prob)
            right_node.left = right_nodes[0] if len(right_nodes) == 1 else Nodo(right_prob)
            right_node.right = None if len(right_nodes) == 1 else right_nodes[-1]

            nodes = [left_node, right_node] + nodes[2:]

        root.left = nodes[0]
        root.right = nodes[1]

        self.codificar_recursivo(root)

        return self.codes

    def decodificar(self, coded_data, code_table):
        decoded_data = ""
        while coded_data:
            for symbol, code in code_table.items():
                if coded_data.startswith(code):
                    decoded_data += symbol
                    coded_data = coded_data[len(code):]
                    break
        return decoded_data