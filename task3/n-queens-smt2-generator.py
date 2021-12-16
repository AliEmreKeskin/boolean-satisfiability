class n_queens_smt2_generator:
    def __init__(self):
        self.body = ""
        self.create_header()
        self.create_footer()

    def create_header(self):
        self.header = "(declare-fun p (Int Int) Bool)\n(assert (and\n"

    def create_body(self, the_n):
        self.body = self.at_least_one_queen_on_every_row(the_n)
        self.body += self.at_most_one_queen_on_every_row(the_n)
        self.body += self.at_least_one_queen_on_every_column(the_n)
        self.body += self.at_most_one_queen_on_every_column(the_n)
        self.body += ";-------------------------------\n"
        self.body += self.at_most_one_queen_on_every_diagonal(the_n)

    def create_footer(self):
        self.footer = "))\n(check-sat)\n(get-model)"

    def generate(self, the_n):
        self.create_body(the_n)

    def write_file(self, filename):
        file = open(filename, "w")
        file.write(self.header)
        file.write(self.body)
        file.write(self.footer)
        file.close()

    def at_least_one_queen_on_row(self, row, the_n):
        string = "(or"
        for i in range(1, the_n + 1):
            string += " (p " + str(row) + " " + str(i) + ")"
        string += ")\n"
        return string

    def at_least_one_queen_on_every_row(self, the_n):
        string = ""
        for i in range(1, the_n + 1):
            string += self.at_least_one_queen_on_row(i, the_n)
        return string

    def at_most_one_queen_on_row(self, row, the_n):
        string = ""
        for j in range(1, the_n):
            for k in range(j + 1, the_n + 1):
                string += "(or (not (p {row_} {j_})) (not (p {row_} {k_})))\n".format(
                    row_=row, j_=j, k_=k
                )
        return string

    def at_most_one_queen_on_every_row(self, the_n):
        string = ""
        for i in range(1, the_n + 1):
            string += self.at_most_one_queen_on_row(i, the_n)
        return string

    def at_least_one_queen_on_column(self, column, the_n):
        string = "(or"
        for i in range(1, the_n + 1):
            string += " (p {i_} {column_})".format(i_=i, column_=column)
        string += ")\n"
        return string

    def at_least_one_queen_on_every_column(self, the_n):
        string = ""
        for i in range(1, the_n + 1):
            string += self.at_least_one_queen_on_column(i, the_n)
        return string

    def at_most_one_queen_on_column(self, column, the_n):
        string = ""
        for i in range(1, the_n):
            for k in range(i + 1, the_n + 1):
                string += (
                    "(or (not (p {i_} {column_})) (not (p {k_} {column_})))\n".format(
                        column_=column, i_=i, k_=k
                    )
                )
        return string

    def at_most_one_queen_on_every_column(self, the_n):
        string = ""
        for i in range(1, the_n + 1):
            string += self.at_most_one_queen_on_column(i, the_n)
        return string

    def at_most_one_queen_on_every_diagonal(self, the_n):
        string = ""
        for i in range(1, the_n):
            for i_prime in range(i + 1, the_n + 1):  # guaranties i<i_prime
                for j in range(1, the_n + 1):
                    for j_prime in range(1, the_n + 1):
                        if (i + j == i_prime + j_prime) or (i - j == i_prime - j_prime):
                            string += "(or (not (p {i_} {j_})) (not (p {i_prime_} {j_prime_})))\n".format(
                                i_=i, j_=j, i_prime_=i_prime, j_prime_=j_prime
                            )
        return string


if __name__ == "__main__":
    g = n_queens_smt2_generator()
    g.generate(8)
    g.write_file("n-queens.smt")
