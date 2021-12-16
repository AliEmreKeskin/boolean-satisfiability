from typing import List, Tuple


class layout_smt2_generator:
    def __init__(self):
        self.create_header()
        self.create_footer()

    def create_header(self):
        self.header = ""

    def create_body(
        self, rect_size: Tuple[int, int], grid_size: Tuple[int, int], name: str
    ):
        self.body = "(declare-fun {} (Int Int) Bool)\n".format(name)
        self.body += "(assert\n"
        a = self.possible_rectangles(rect_size, grid_size, name)
        self.body += self.one_of(a)
        self.body += ")\n"

    def create_footer(self):
        self.footer = "(check-sat)\n(get-model)"

    def generate(
        self, rect_size: Tuple[int, int], grid_size: Tuple[int, int], name: str
    ):
        self.create_body(rect_size, grid_size, name)

    def write_file(self, filename):
        file = open(filename, "w")
        file.write(self.header)
        file.write(self.body)
        file.write(self.footer)
        file.close()

    def possible_rectangles(
        self, rect_size: Tuple[int, int], grid_size: Tuple[int, int], name: str
    ) -> List[str]:
        rect_list = []
        for tl_y in range(grid_size[1] - rect_size[1] + 1):
            for tl_x in range(grid_size[0] - rect_size[0] + 1):
                string = "(and"
                for j in range(rect_size[1]):
                    for i in range(rect_size[0]):
                        string += " ({name_} {i_} {j_})".format(
                            name_=name, i_=tl_x + i, j_=tl_y + j
                        )
                string += ")"
                rect_list.append(string)
        return rect_list

    def at_least_one(self, elements: List[str]) -> str:
        string = "(or\n"
        for i in elements:
            string += i + "\n"
        string += ")\n"
        return string

    def at_most_one(self, elements: List[str]) -> str:
        string = "(and\n"
        for i in range(0, len(elements) - 1):
            for j in range(i + 1, len(elements)):
                string += "(or (not {}) (not {}))\n".format(elements[i], elements[j])
        string += ")\n"
        return string

    def one_of(self, elements: List[str]) -> str:
        string = "(and\n"
        string += self.at_least_one(elements)
        string += self.at_most_one(elements)
        string += ")\n"
        return string


if __name__ == "__main__":
    g = layout_smt2_generator()
    g.generate((2, 2), (8, 8), "p")
    g.write_file("layout.smt")
