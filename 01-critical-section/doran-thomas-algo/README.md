# Doran-Thomas Algorithm

## Description

Algorithm inspired by Dekker's solution to the critical section problem.

**Principle:** use of two global variables, `want_cs` and `turn`, to indicate the **process's intention** to **access the critical section** and to define a **rule that determines which process enters the critical section** in the event of a *tie*, respectively.

**Pseudocode:**
```text
Global Variables: turn = 0, want_cs = [False, False]

<non-critical-section>
want_cs[current_thread_id] = True
if want_cs[other_thread_id]:
    if turn == other_thread_id:
        want_cs[current_thread_id] = False
        while turn != current_thread_id:
            pass
        want_cs[current_thread_id] = True
    while want_cs[other_thread_id]:
        pass
<critical-section>
want_cs[current_thread_id] = False
turn = other_thread_id
```

**Explanation:** the process indicates its intention to access the critical section. It then checks whether the other process also wants access; if so, it checks whether or not it is its turn. **If it is not its turn**, it **waits** for the other process to hand over the turn upon leaving the critical section. Conversely, **if it is its turn**, it **checks whether the other process still intends to access and waits until it blocks** before entering the critical section, since if the process reaches the second loop of the pre-protocol, it already holds the turn and, therefore, the priority to access the critical section.

**Issue:** as with Dekker's algorithm, the solution presented by Doran-Thomas **has** a **busy-waiting** problem.

# Algoritmo de Doran-Thomas

## Descripción

Algoritmo inspirado en la solución de Dekker al problema de la región crítica.

**Principio:** uso de dos variables globales, `want_cs` y `turn`, para indicar la **intención del proceso** de querer **acceder a la sección crítica** y definir una **regla que estipule qué proceso entra a la sección crítica** en caso de *empate*, respectivamente.

**Pseudocódigo:**
```text
Global Variables: turn = 0, want_cs = [False, False]

<non-critical-section>
want_cs[current_thread_id] = True
if want_cs[other_thread_id]:
    if turn == other_thread_id:
        want_cs[current_thread_id] = False
        while turn != current_thread_id:
            pass
        want_cs[current_thread_id] = True
    while want_cs[other_thread_id]:
        pass
<critical-section>
want_cs[current_thread_id] = False
turn = other_thread_id
```

**Explicación:** el proceso indica su intención de querer acceder a la sección crítica. Posteriormente, comprueba si el otro proceso quiere acceder a la sección crítica, en dicho caso comprueba si es o no su turno. **Si no es su turno** este **espera** a que el otro proceso le ceda el turno al salir de la sección crítica. Por contra, **si es su turno** **comprueba si el otro proceso sigue teniendo intención de acceder y espera hasta que este se bloquee** antes de entrar a la sección crítica, ya que si el proceso evalúa el segundo bucle del preprotocolo este consta del turno y, por tanto, de la prioridad para acceder a la sección crítica.

**Problemática:** como en el caso del algoritmo de Dekker, la solución presentada por Doran-Thomas **presenta** un problema de **espera activa**.