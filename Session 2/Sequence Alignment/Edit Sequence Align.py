#Algorithm for solving sequence alignment
'''
    Input strings x,y of len(x) = m, len(y) = n and find minimum number of
    edit steps and the specific steps to transform x into y.

    Time Complexity: O(nm)
'''


class SequenceAlignment(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.solution = []

    delta = lambda self, x, y, i, j: 1 if x[i] != y[j] else 0

    def find_solution(self, OPT, m, n):
        if m == 0 and n == 0:
            return

        # We can only do insert if n != 0, align if there are element in both x, y, etc.
        insert = OPT[m][n - 1] + 1 if n != 0 else float("inf")

        align = (
            OPT[m - 1][n - 1] + self.delta(self.x, self.y, m - 1, n - 1)
            if m != 0 and n != 0
            else float("inf")
        )

        delete = OPT[m - 1][n] + 1 if m != 0 else float("inf")

        best_choice = min(insert, align, delete)

        if best_choice == insert:
            self.solution.append("insert_" + str(self.y[n - 1]))
            return self.find_solution(OPT, m, n - 1)

        elif best_choice == align:
            self.solution.append("align_" + str(self.y[n - 1]))
            return self.find_solution(OPT, m - 1, n - 1)

        elif best_choice == delete:
            self.solution.append("remove_" + str(self.x[m - 1]))
            return self.find_solution(OPT, m - 1, n)

    def alignment(self):
        n = len(self.y)
        m = len(self.x)

        OPT = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(1, m + 1):
            OPT[i][0] = i

        for j in range(1, n + 1):
            OPT[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                OPT[i][j] = min(
                    OPT[i - 1][j - 1] + self.delta(self.x, self.y, i - 1, j - 1),
                    OPT[i - 1][j] + 1,
                    OPT[i][j - 1] + 1,
                )  # align, delete, insert respectively

        self.find_solution(OPT, m, n)

        return (OPT[m][n], self.solution[::-1])





if __name__ == '__main__':
    x = 'TGACGTGC'
    y = 'TCGACGTCA'

    print('We we want to transform: ' + x + ' to: ' + y + "\n")

    sqalign = SequenceAlignment(x, y)
    min_edit, steps = sqalign.alignment()

    print('Minimum amount of edit steps are: ' + str(min_edit) + "\n")
    print('And the way to do it is: ' + str(steps))




#Problem Explanation
'''
    We we want to transform: TGACGTGC to: TCGACGTCA
    
    Options:>   1) Align    2) Insert   3) Remove
    
    
            #Before
            [T G A C G T G C]
            [T C G A C G T C A]
    
    
    #Simplification
    -----------------------------------------
    -        1 2 3 4 5 6 7 8 9       seq(1) -
    -       [T - G A C G T G C]             -
    -----------*-----------*-*---------------
    -       [T C G A C G T C A]             -
    -        1 2 3 4 5 6 7 8 9       seq(2) -
    -----------------------------------------
    
    
            #After
            [T  C   G   A   C   G   T   C   A]
            [T  C   G   A   C   G   T   C   A]
'''

#Steps
'''
                    ['align_T',
            (1)=>       'insert_C',
                            'align_G',
                                'align_A',
                                    'align_C',
                                        'align_G',
                                            'align_T',
            (2)=>                               'remove_G',
                                                    'align_C',
            (3)=>                                       'insert_A']
    
    
    So the minimum number of steps is: 3
'''