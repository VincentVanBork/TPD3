from criticalpath import Node

p = Node('project')
A = p.add(Node('A', duration=1))
B = p.add(Node('B', duration=3, lag=0))
C = p.add(Node('C', duration=4, lag=0))
D = p.add(Node('D', duration=7, lag=0))
E = p.add(Node('E', duration=2, lag=0))
F = p.add(Node('F', duration=5, lag=0))
G = p.add(Node('G', duration=2, lag=0))
H = p.add(Node('H', duration=1, lag=0))
I = p.add(Node('I', duration=3, lag=0))
J = p.add(Node('J', duration=1, lag=0))
p.link(A, B).link(A, C).link(B, D).link(D, E).link(C, E).link(E, J).link(C,F).link(C, H).link(F, I).link(C, G).link(H, I).link(G,I).link(I, J)
p.update_all()
p.get_critical_path()

p.duration

print(p.get_critical_path(),p.duration)