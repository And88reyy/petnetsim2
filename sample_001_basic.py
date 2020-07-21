from itertools import count, combinations
from petnetsim.elements import Place, Arc, Transition

A = Place('A', init_tokens=6)
B = Place('B', init_tokens=4)
C = Place('C')
D = Place('D')

places = [A, B, C, D]

T = Transition('T')

transitions = [T]

arcs = [Arc(A, T, 2),
        Arc(B, T, 1),
        Arc(T, C, 4),
        Arc(T, D, 1)
        ]


def print_sim(step, t):
    print('step:', step, '  t:', t)
    for p in places:
        print(p.name, p.tokens, sep=': ')


def run():

    print('------------------------------------')
    print(' run')

    for t in transitions:
        t.reset()
    for p in places:
        p.reset()

    max_steps = 100
    t = 0.0

    print_sim(0, t)

    for step in range(1, max_steps):

        # enabled transitions
        enabled = [t for t in transitions if t.enabled()]

        # TODO: conflict groups of enabled
        conflict_groups = [[enabled]]
        for t in conflict_groups:
            t.fire()

        # TODO: if no transitions are active, advance time
        num_waiting = 0

        print_sim(step, t)

        if len(enabled) == 0 and num_waiting == 0:
            print(' -- breaking condition --')
            break


run()