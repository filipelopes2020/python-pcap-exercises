```mermaid
classDiagram
    direction BT

    class A
    class B
    class C
    class D
    class E

    B --|> A
    D --|> A
    C --|> B
    D --|> B
    E --|> C
    E --|> D
    E --|> A
```