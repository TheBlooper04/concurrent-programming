# Manna-Pnueli Algorithm

## Description

**Principle:** an **integer** global variable used as a mechanism to **decide process access** to the critical section

**Pseudocode:**
```text
Global Variables: want_cs = [0, 0]

<non-critical-section>
if current_thread_id == 0:
    if want_cs[other_thread_id] == -1:
        want_cs[current_thread_id] = -1
    else:
        want_cs[current_thread_id] = 1

    while want_cs[other_thread_id] == want_cs[current_thread_id]:
        pass

if current_thread_id == 1:
    if want_cs[other_thread_id] == -1:
        want_cs[current_thread_id] = 1
    else:
        want_cs[current_thread_id] = -1
    
    while want_cs[other_thread_id] == -want_cs[current_thread_id]:
        pass
<critical-section>
want_cs[current_thread_id] = 0
```

**Explanation:** process p0 checks whether p1 **already claimed priority first**, i.e., whether `want_cs[1]` equals **-1**. If so, p0 sets its own value to **-1** as well, which makes p1's wait condition (`want_cs[0] == -want_cs[1]`) evaluate to `False`, letting p1 proceed without blocking. If instead `want_cs[1]` is not **-1** — either because p1 is not yet contending, or because it already yielded to p0 in a previous attempt — p0 marks itself with **1**, acknowledging that it did not arrive first.

Process p1 follows the symmetric but inverted logic: if it detects that p0 already claimed priority (`want_cs[0] == -1`), p1 marks itself with **1** to yield, which makes p0's wait condition (`want_cs[1] == want_cs[0]`) evaluate to `False` and releases it. If `want_cs[0]` is not **-1**, p1 goes ahead and claims priority by marking itself with **-1** — this covers both the case where p0 was already waiting with `want_cs[0] == 1`, and the case where neither process has started contending yet.

> Note: the instructions branch depending on whether this is the first or second process, due to the asymmetry present in the Manna-Pnueli algorithm.

# Algoritmo de Manna-Pnueli

## Descripción

**Principio:** variable global **entera** como mecanismo para **decidir el acceso de los procesos** a la sección crítica

**Pseudocódigo:**
```text
Global Variables: want_cs = [0, 0]

<non-critical-section>
if current_thread_id == 0:
    if want_cs[other_thread_id] == -1:
        want_cs[current_thread_id] = -1
    else:
        want_cs[current_thread_id] = 1

    while want_cs[other_thread_id] == want_cs[current_thread_id]:
        pass

if current_thread_id == 1:
    if want_cs[other_thread_id] == -1:
        want_cs[current_thread_id] = 1
    else:
        want_cs[current_thread_id] = -1
    
    while want_cs[other_thread_id] == -want_cs[current_thread_id]:
        pass
<critical-section>
want_cs[current_thread_id] = 0
```

**Explicación:** el proceso p0 comprueba si p1 **ya reclamó la prioridad primero**, es decir, si `want_cs[1]` vale **-1**. Si es así, p0 iguala su propio valor a **-1**, lo que hace que la condición de espera de p1 (`want_cs[0] == -want_cs[1]`) se evalúe a `False` y p1 pueda entrar sin bloquearse. Si por el contrario `want_cs[1]` no vale **-1** — porque p1 todavía no está contendiendo, o porque ya cedió el turno a p0 en un intento anterior — p0 se marca a sí mismo con **1**. 

El proceso p1 sigue la lógica simétrica pero invertida: si detecta que p0 ya reclamó prioridad (`want_cs[0] == -1`), p1 se marca con **1** para ceder, lo cual hace que la condición de espera de p0 (`want_cs[1] == want_cs[0]`) se evalúe a `False` y lo libere. Si `want_cs[0]` no vale **-1**, p1 se adelanta y reclama la prioridad marcándose con **-1** — esto resuelve tanto el caso en que p0 ya esperaba con `want_cs[0] == 1`, como el caso en que ninguno de los dos ha empezado todavía a contender.

> Nota: se construye una ramificación de las instrucciones en función de si se trata del primer o segundo proceso a causa de la asimetría presentada por el algoritmo de Manna-Pnueli.