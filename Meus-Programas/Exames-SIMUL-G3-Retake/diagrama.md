```mermaid
classDiagram
    direction BT
    class A
    class B
    class C
    class D
    class E
    class K1
    class K2
    class K3

    K1 --> A
    K1 --> B
    K1 --> C

    K2 --> D
    K2 --> B
    K2 --> E

    K3 --> D
    K3 --> A
```