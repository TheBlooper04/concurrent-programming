# Peterson's Algorithm

**Principle:** Based on Dekker's Algorithm, it **unifies the checks prior to accessing the critical section** by means of a single **conditional expression**.

**Pseudocode:**
```text
Global Variables: turn = 0, want_cs = [False, False]

<non-critical-section>
want_cs[thread_id] = True
turn = other_thread_id
while want_cs[other_thread_id] == True and turn == other_thread_id:
    pass
<critical-section>
want_cs[thread_id] = False
```

**Explanation:** the process indicates its intention to enter the critical section and yields the turn to the opposing process, such that when evaluating the `while` loop condition, if the process/thread detects that the other process has the turn and also wants to access, it waits until the other process leaves the critical region. The **main difference** with Dekker's algorithm is that **processes do not yield the turn upon leaving the critical region**, but rather beforehand, and they **check in a single statement** (`or` or `and`) **whether the condition to enter is met**, or whether they must yield entry due to the other process's turn priority.

**Problem:** although it presents itself as a simplification of Dekker's solution, since it abstracts the turn check inside the `while` loop into a single boolean expression that verifies the processes' priority turn, `turn`, and the other process's intention, `want_cs`, this algorithm still presents the same active-waiting problem exposed in Dekker's algorithm. This is because, when both processes want to access the critical section and, according to the priority rules, one process must yield the critical section to the other, that process wastes processor time.

# Algoritmo de Peterson

**Principio:** Basado en el Algoritmo de Dekker **unifica las verificaciones prévias al acceso a la sección crítica** mediante una **expresión condicional**

**Pseudocódigo:**
```text
Global Variables: turn = 0, want_cs = [False, False]

<non-critical-section>
want_cs[thread_id] = True
turn = other_thread_id
while want_cs[other_thread_id] == True and turn == other_thread_id:
    pass
<critical-section>
want_cs[thread_id] = False
```

**Explicación:** el proceso indica su intención de entrar a la sección crítica y cede el turno al proceso contrario de manera que si al momento de evaluar la condición del bucle `while` el proceso/hilo detecta que el otro proceso tiene el turno y además quiere acceder entonces espera hasta que
el otro proceso deje de estar dentro de la región crítica. La **principal diferencia** con el algoritmo de Dekker es que los **procesos no se ceden el turno al salir de la región crítica** sino préviamente a esta y **comprueban en una sola sentencia** (`or` o `and`) **si se cumple la situación para poder entrar** o deben de ceder la entrada a causa de la prioridad de turno del otro proceso.

**Problemática:** a pesar de presentarse como una simplificación a la solución de Dekker, ya que, abstrae la necesidad de una comprobación del turno dentro del bucle `while` en una expresión booleana que verifica el turno de prioridad de los procesos, `turn`, y la intención del otro proceso, `want_cs`. Este algoritmo presenta la misma problemática de espera activa expuesta en el algoritmo de Dekker, debido a que en caso de que ambos procesos quieran acceder a la sección crítica y por las reglas de prioridad el proceso deba de ceder la sección crítica al proceso contrario, este malgasta tiempo de procesador.