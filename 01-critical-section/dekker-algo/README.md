# Dekker's Algorithm

## Description
*Attempted solutions* to the critical region problem for shared-memory systems with **2 processes**.

For an **algorithm** to be considered **valid** from a concurrency standpoint, it must **satisfy 3 main criteria**:
- **Mutual exclusion:** Only **one process** can be inside the **critical region** at a *time*
- **Progress (Absence of Deadlock):** **Processes can advance** to the critical section **without waiting indefinitely** for *one another*
- **Bounded waiting:** Any process that wants to **enter the critical section** must be able to do so within a **finite time**

Additionally, **Dijkstra's 4 requirements** are considered:
- **Symmetric solution:** No assumptions can be made about the static priority of the processes
- **Speed independence:** No assumptions can be made about the relative execution speed of the processes
- **Non-interference:** a process that stops or is interrupted outside the critical section cannot affect the processes that want to access the critical section
- **Bounded waiting:** if two or more processes want to access the critical section, a decision on who enters must be made within a finite number of steps

Thus, **4 attempted Dekker solutions** are identified:

### First Attempt

**Principle**: Use of a global turn variable to **decide who enters** the critical section.

**Pseudocode**:
```text
Global Variables: turn = 0

<non-critical-section>
while turn != my_turn:
    await
<critical-section>
turn = other_thread_turn
```
**Explanation:** The global variable, `turn`, defines access priority to the critical region at every moment, such that once a process leaves the critical region, priority is handed over to the opposite process/thread.

**Problem**: It violates **Non-interference**; if one of the processes *blocks or stops*, the **other process remains blocked** waiting for its turn, which will never come.

### Second Attempt

**Principle:** Use of a **boolean array** to **indicate whether the process wants to access** the critical section or not.

**Pseudocode:**
```text
Global Variables: want_cs = [False, False]
<non-critical-section>
while want_cs[other_thread_index] == True:
    await
want_cs[current_thread_index] = True
<critical-section>
want_cs[current_thread_index] = False
```
**Explanation:** Although the **algorithm** is presented using **boolean variables**, one for each process, in practice an **array, list, or any other data structure** that allows both variables to be accessed simultaneously within a sequential program is used. In this way, it is checked whether the other process wants to access the critical section or not; if it does want to access it, the process blocks and waits for the other to leave the critical section before entering.

**Problem:** It violates **Mutual Exclusion**; both processes check whether the other wants to access the section; however, **due to interleaving**, it can happen that **both processes** check the condition in such a way that they **manage to bypass the pre-protocol** and access the critical section simultaneously. An example of such interleaving would be: one process checks the condition first, exits the loop, and before marking that it wants to access the critical section, control is handed over to the opposite process/thread, which then evaluates the entire loop up to the assignment.

### Third Attempt

**Principle:** **reverse the statements of the Second Attempt**, first **indicating the intention to access** before checking whether the opposing process intends to do the same.

**Pseudocode:**
```text
Global Variables: want_cs = [False, False]

<non-critical-section>
want_cs[current_thread_index] = True
while want_cs[other_thread_index] == True:
    await
<critical-section>
want_cs[current_thread_index] = False
```

**Explanation:** Following the reasoning of the **Second Attempt**, both processes try to access the critical section, but first indicate their intention to enter before checking whether the opposing process wants to enter or not. In this way, **the mutual exclusion violation problem from the previous attempt is solved**, guaranteeing that **the critical region can only be accessed** when the **opposing process does not want to access it**, or **has already accessed it beforehand** (it has indicated its intention to access and has passed the pre-protocol).

**Problem:** It violates the **Absence of Deadlock**; **due to the interleaving of the processes/threads**, it can happen that both processes indicate they want to access the critical section, `want_cs = [True, True]`, before either of them evaluates whether the other wants to access it. This results in both processes evaluating and entering the waiting loop, where they will remain **waiting indefinitely** for the other process. This is due, among other things, to the lack of a rule determining priority between the two processes in the event of a *tie* in their arrival order.

### Fourth Attempt

**Principle:** same principles as the **Third Attempt**, including a **state alternation** in case both processes get held up in the loop checking the state of the opposing process.

**Pseudocode:**
```text
Global Variables: want_cs = [False, False]

<non-critical-section>
want_cs[current_thread_index] = True
while want_cs[other_thread_index] == True:
    want_cs[current_thread_index] = False
    want_cs[current_thread_index] = True
<critical-section>
want_cs[current_thread_index] = False
```

**Explanation:** the process indicates its intention to access the critical section and checks whether the other process also wants to access it. As in the previous case, due to interleaving it can happen that both processes indicate they want to access the critical section before either of them has executed the pre-protocol statements, and therefore both get trapped inside the loop indefinitely. To solve this, the process inside the loop **alternates its state**, changing the boolean value associated with its identifier in `want_cs`. In this way, **the deadlock problem is eliminated**, since *at some point during execution* the interleaving will cause one of the processes to evaluate the condition while the other indicates its intention not to access the section, allowing it to enter.

**Problem:** It violates **Bounded Waiting (Dijkstra)**; the **rule** established to decide the **order of preference** among processes **is not defined within a finite number of steps**. In addition, what is known as **livelock** occurs, where the processes/threads carry out a continuous mutual change of state in response to one another without achieving any progress.

### Dekker's Algorithm

**Principle:** application of the principles of the global turn variable and boolean access variables to the critical section.

**Pseudocode:**
```text
Global Variables: turn = 0, want_cs = [False, False]

<non-critical-section>
want_cs[current_thread_index] = True
while want_cs[other_thread_index] == True:
    if turn != my_turn:     // my_trun will refer to the current thread id
        want_cs[current_thread_index] = False
        while turn != my_turn:
            await
        want_cs[current_thread_index] = True
<critical-section>
want_cs[current_thread_index] = False
turn = other_thread_turn
```

**Explanation:** the process indicates its intention to access the critical section before checking the intentions of the other process/thread. If both want to access it, the process/thread checks whose turn it is, using the `turn` variable. If it is the **other process's turn**, this process **gives up trying to enter the critical section** and **remains waiting until it is its turn**, at which point it **again indicates its intention to access and insists on entering** until the other process stops indicating its intention to enter (in the case where both processes wanted to enter at that moment).

**Problem:** despite the correctness of the algorithm, it is worth mentioning the **processor time wasted during process waits (active waiting/busy waiting)** when a process is **already inside the critical section** and others must wait their turn according to the access priority rule for the critical region.

# Algoritmo de Dekker

## Descripción
*Intentos de solución* al problema de la región crítica para sistemas de memoria compartida por **2 procesos**.

Para que un **algoritmo** sea considerado **válido** desde el punto de vista de la concurrencia, debe **satisfacer 3 criterios principales**:
- **Exclusión mutua:** Solo puede haber **un proceso** en *simultáneo* dentro de la **región crítica**
- **Progreso (Ausencia de Interbloqueo):** Los **procesos pueden avanzar** a la sección crítica **sin esperar indefinidamente** *unos de otros*
- **Espera limitada:** Cualquier proceso que quiera **entrar a la sección crítica** debe de poder hacerlo en un **tiempo finito**

Adicionalmente, se consideran los **4 requisitos de Dijkstra**:
- **Solución Simétrica:** No se pueden hacer suposiciones sobre la prioridad estática de los procesos
- **Velocidad Independiente:** No se pueden hacer suposiciones sobre la velocidad relativa de ejecución de los procesos
- **No interferencia:** un proceso que para o se interrumpe fuera de la sección crítica no puede afectar a los procesos que quieren acceder a la sección crítica
- **Espera limitada:** si dos o más procesos quieren acceder a la sección crítica se debe de tomar una decisión de quién entra en un número finito de pasos

Es así que se identifican **4 intentos de solución de Dekker**:

### Primer Intento

**Principio**: Uso de una variable global de **turno para decidir quién entra** a la sección crítica.

**Pseudocódigo**:
```text
Global Variables: turn = 0

<non-critical-section>
while turn != my_turn:
    await
<critical-section>
turn = other_thread_turn
```
**Explicación:** La variable global,`turn`, define la prioridad de acceso a la región crítica en cada momento de manera que una vez el proceso sale de la región crítica el turno de prioridad se cede al proceso/hilo opuesto.

**Problemática**: Incumple la **No Interferencia**; si uno de los procesos se *bloquea o se para* el **otro proceso se queda bloqueado** esperando su turno, el cual nunca llegará.

### Segundo Intento

**Principio:** Uso de un **arreglo de booleanos** para **indicar cuando el proceso quiere acceder o no** a la sección crítica.

**Pseudocódigo:**
```text
Global Variables: want_cs = [False, False]
<non-critical-section>
while want_cs[other_thread_index] == True:
    await
want_cs[current_thread_index] = True
<critical-section>
want_cs[current_thread_index] = False
```
**Explicación:** Aunque se presente el **algoritmo** aplicando **variables booleanas**, una para cada proceso, en la práctica se aplica un arreglo, lista o *cualquier* otra **estructura de datos que permita acceder en un programa secuencial a ambas variables en simultáneo**. De esta manera , se comprueba si el proceso contrario quiere acceder o no a la sección crítica, en caso de que quiera acceder, el proceso se bloquea y espera a que el otro salga de la sección crítica para acceder. 

**Problemática:** Incumple la **Exclusión Mutua**; ambos procesos comprueban si el otro quiere acceder; sin embargo, **a causa del intercalado** puede suceder que **ambos procesos** verifiquen la condición de tal manera que **sean capaces de sortear el preprotocolo** y accedan en simultáneo a la sección crítica. Un ejemplo de dicho intercalado sería, que primero un proceso verifique la condición, luego salga del bucle y antes de marcar que quiere acceder a la sección crítica se cede el control al proceso/hilo contrario y este evalúe el bucle completo hasta llegar a la asignación.

### Tercer Intento

**Principio:** **invertir las sentencias del Segundo Intento**, indicando **primero** que **se quiere acceder** antes de comprobar si el proceso contrario tiene intención de hacer lo mismo.

**Pseudocódigo:**
```text
Global Variables: want_cs = [False, False]

<non-critical-section>
want_cs[current_thread_index] = True
while want_cs[other_thread_index] == True:
    await
<critical-section>
want_cs[current_thread_index] = False
```

**Explicación:** Siguiendo el razonamiento del **Segundo Intento**, ambos procesos tratan de acceder a la sección crítica, pero préviamente indicando su intención de entrar antes de corroborar si el proceso opuesto quiere o no entrar. De esta manera, **se solventa el problema de la violación de la exclusión mutua del intento anterior**, garantizando que **solo se puede acceder** a la región crítica cuando el **proceso contrario no quiera acceder** o **se haya accedido préviamente a ella** (se haya indicado que se quiere acceder y se ha sorteado el preprotocolo).

**Problemática:** Incumple la **Ausencia de Interbloqueo**; **a causa del intercalado de los procesos/hilos** puede suceder que ambos procesos indiquen que quieren acceder a la sección crítica, `want_cs = [True, True]`, préviamente a que alguno de los dos evalúe si el otro quiere acceder a la sección crítica. Esto da como resultado en la evaluación y entrada de ambos procesos al bucle de espera donde quedarán esperando de forma indefinida al otro proceso. Esto entre otras cosas se debe a la falta de una regla que determine la prioridad entre los dos procesos en caso de un *empate* en el orden de llegada de los procesos.

### Cuarto Intento

**Principio:** mismos principios que el **Tercer Intento**, incluyendo una alternancia del estado en caso de que ambos procesos queden retenidos en el bucle de verificación del estado del proceso opuesto.

**Pseudocódigo:**
```text
Global Variables: want_cs = [False, False]

<non-critical-section>
want_cs[current_thread_index] = True
while want_cs[other_thread_index] == True:
    want_cs[current_thread_index] = False
    want_cs[current_thread_index] = True
<critical-section>
want_cs[current_thread_index] = False
```

**Explicación:** el proceso indica su intención de querer acceder a la sección crítica y comprueba si el otro proceso quiere o no acceder también a ella. Como en el caso anterior, a causa del intercalado se puede dar el caso de que ambos procesos indiquen que quieren acceder a la sección crítica antes de que ninguno de los dos haya ejecutado las sentencias del preprotocolo y por tanto ambos queden atrapados dentro del bucle de forma indefinida. Para solventar esto último el proceso dentro del bucle alterna su estado, cambiando el valor de booleano asociado a su identificador en `want_cs`. De esta manera, **se consigue eliminar el problema del interbloqueo (deadlock)** ya que en *algún punto de la ejecución* el intercalado hará que uno de los procesos evalúe la condición cuando el otro indica su intención de no acceder a la sección, permitiéndole la entrada a la misma.

**Problemática:** Incumple la **Espera Limitada (Dijkstra)**; la **regla** establecida para decidir el **orden de preferencia** de los procesos **no se define en un número finito de pasos**. Además se produce lo que se conoce como **bloqueo activo (livelock)**, donde los procesos/hilos llevan a cabo un continuo cambio de estado en respuesta mutua sin lograr ningún progreso.

### Algoritmo de Dekker

**Principio:** aplicación de los principios de variable global de turno y variables booleanas de acceso a la sección crítica.

**Pseudocódigo:**
```text
Global Variables: turn = 0, want_cs = [False, False]

<non-critical-section>
want_cs[current_thread_index] = True
while want_cs[other_thread_index] == True:
    if turn != my_turn:                             // my_turn will refer to the current thread id
        want_cs[current_thread_index] = False
        while turn != my_turn:
            await
        want_cs[current_thread_index] = True
<critical-section>
want_cs[current_thread_index] = False
turn = other_thread_turn
```

**Explicación:** el proceso indica su intención de acceder a la sección crítica préviamente a comprobar las intenciones del otro proceso/hilo. En caso de que ambos quieran acceder el proceso/hilo comprueba a quién le corresponde el turno, mediante la variable `turn`. En caso de que sea el **turno del otro proceso** este **desiste de entrar a la sección crítica** y **se mantiene en espera hasta que sea su turno**, momento en el cual **vuelve a indicar su intención de acceder e insiste para entrar** hasta que el otro proceso deja de indicar su intención de entrar (En el caso de que ambos procesos en ese momento tuvieran la intención de entrar).

**Problemática:** a pesar de la correctitud del algoritmo, merece la pena mencionar el **gasto de tiempo de procesador durante las esperas de los procesos (espera activa/busy waiting)** en caso de que ya haya un **proceso dentro de la sección crítica** y deban esperar su turno conforme a la regla de preferencia de acceso a la región crítica.