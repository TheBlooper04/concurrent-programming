# CAS Hardware Instruction

## Description

**Atomic** instruction that compares an expected value, provided as a parameter, with the value held at a given memory location.

It replaces the value held at that memory location if both compared values are equal.

The instruction returns 1 if both values are equal and 0 if they differ.

Because the operation is atomic, both the comparison and the write are executed as a single, indivisible operation.

## Pseudocode

```text
CAS(value_addr, expected_value, new_value):

if *value_addr == expected_value:
    *value_addr = new_value;
    return 1;
else:
    return 0;
```

# CAS Instrucción Hardware

## Descripción

Instrucción **atómica** que compara un valor esperado, proporcionado como parámetro, con un valor contenido en una posición de memoria dada.

Sustituye el valor contenido en dicha posición de memoria en caso de que ambos valores comparados sean iguales.

La instrucción devuelve uno si ambos valores son iguales y 0 si difieren.

El hecho de que la operación sea atómica hace que tanto la comparación como la escritura se ejecuten como una única operación indivisible.

## Pseudocódigo

```text
CAS(value_addr, expected_value, new_value):

if *value_addr == expected_value:
    *value_addr = new_value;
    return 1;
else:
    return 0;
```