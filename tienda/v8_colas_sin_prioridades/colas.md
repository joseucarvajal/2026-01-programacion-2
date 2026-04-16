Las colas son estructuras FIFO (First In First Out):
Las colas tienen las siguientes operaciones:
    - enqueue: Encolar o agregar un nuevo elemento a la cola: Agrega el nuevo elemento al final de la cola
    - dequeue: Desencolar o atender el elemento que está a la cabeza de la cola
    - Preguntar quien sigue pero SIN atenderlo: peek

Ejemplos:
(a, b, c, d)
se atiende (des-encola -dequeue-) a:
(b, c, d)
se atiende (des-encola -dequeue-) b:
(c, d)
llega una nueva persona e (encola -enqueue-) e:
(c, d, e)
Peek: Preguntar quien sigue
Respuesta es: c, el próximo en atender es C
(c, d, e)
