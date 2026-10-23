# Get-And-Add Hardware Instruction

## Description

**Atomic** instruction that reads the value held at a given memory location and adds to it a value provided as a parameter.

It returns the value held before the addition.

Atomicity guarantees that the read and the update of that location are executed as a single, indivisible operation.

## Pseudocode

```text
GetAndAdd(value_addr, added_value):
    old_value = *value_addr;
    *value_addr = old_value + added_value;
    return old_value;
```

# Instrucción hardware Get-And-Add

## Descripción

Instrucción **atómica** que obtiene el valor contenido en una posición de memoria determinada y suma a su contenido un valor dado como parámetro.

Devuelve el valor previo a la operación de suma.

La atomicidad garantiza que la lectura y la actualización de dicha posición se ejecuten como una única operación indivisible.

## Pseudocódigo

```text
GetAndAdd(value_addr, added_value):
    old_value = *value_addr;
    *value_addr = old_value + added_value;
    return old_value;
```