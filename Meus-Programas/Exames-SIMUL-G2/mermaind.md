classDiagram
    direction BT

    class A
    class B
    class C
    class D
    class E

    B --|> A
    C --|> A
    D --|> B
    E --|> B
    E --|> A
    F --|> C
    G --|> E
    G --|> D
    G --|> F