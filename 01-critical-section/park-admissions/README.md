# Simulación de entradas a un parque

## Descripción

El problema consiste en un parque que **cuenta con dos puertas**, **puerta 0** y **puerta 1**, por donde acceden diferentes personas. La única condición de las puertas del parque es que **no pueden estar ambas abiertas al mismo tiempo para el paso de personas**. De esta manera, se registra el tiempo de cada persona que accede así como la puerta a través de la cual accede al parque. Se pide contabilizar **10 entradas** por cada puerta y su *tiempo medio*, es decir, el tiempo medio que transcurre entre la entrada de una persona y la siguiente para dicha puerta.

Para la **simulación** realista, asíncrona e impredecible de las personas que acceden al parque se utiliza un **retardo aleatorio** sobre los procesos de como **máximo 5000 ms**.

>**Implementación:** algoritmo de **Peterson**

**Pseudocódigo:**
```text
Global Variables: turn = 0, want_cs = [False, False]

<non-critical-section>
want_cs[thread_id] = True
turn = other_thread_id
while want_cs[other_thread_id] and turn == other_thread_id:
    pass
<critical-section>
want_cs[thread_id] = False
```
