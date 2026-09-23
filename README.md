# Concurrent Programming
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04.5_LTS-E95420?style=plastic&logo=ubuntu)
![Go](https://img.shields.io/badge/Go-1.27.1-00ADD8?style=plastic&logo=go)
![Python](https://img.shields.io/badge/Python-3.12.3-3776AB?style=plastic&logo=python)
![Ada](https://img.shields.io/badge/Ada-13.3.0-000000?style=plastic&logo=ada)
![C](https://img.shields.io/badge/C-13.3.0-A8B9CC?style=plastic&logo=c)
![Java](https://img.shields.io/badge/Java-OpenJDK_27-000000?style=plastic&logo=openjdk)
## Description

Solutions to the exercises and practical assignments of the **Concurrent Programming** course at the **University of the Balearic Islands (UIB)**, taught by **Dr. Miquel Mascaró Oliver**.

The **implementations** for the proposed problems are presented in the following languages: **Python**, **Go**, **Ada**, **C**, and **Java**. 

The use of multiple programming languages allows for **approaching the problem from different angles** depending on the capabilities each language offers to tackle the concurrent management of processes and threads.

## Contents 

### 1. The Critical Section Problem
Classic algorithms for problems with **2 processes**:
- *Dekker's* Algorithm
- *Peterson's* Algorithm
- *Doran-Thomas* Algorithm

Classic algorithms for problems with **N processes**:
- *Lamport's* Algorithm (**Bakery**)
- Lamport's *Fast* Algorithm

**Hardware Support (Primitives)**:
- *Test-and-Set*
- *Swap* 
- *Compare-and-Swap* (CAS)

### 2. Process Synchronization Mechanisms
- **Semaphores:** Binary semaphores, counting semaphores, and barriers
- **Monitors:** Condition variables and signaling
- **Channels:** Channels in Go, Rendezvous model

### 3. Solutions to Classic Concurrency Problems
- Producer-Consumer
- Readers-Writers
- Dining Philosophers

## Repository Considerations

**Development Environment:**

- **OS:** `Ubuntu`; release 24.04.5 LTS
- **IDEs:** `Visual Studio Code` and `IntelliJ` (Java implementations)

**Compilers and interpreters used:**
- **Python:** `python3` - v3.12.3
- **Java:** `OpenJDK` - v27
- **Ada:** `gnat` - v13.3.0
- **Go:** `go` - v1.27.1
- **C:** `gcc` - v13.3.0

>**Note:** The solutions have been developed individually for **purely educational purposes** and **personal study**.

# Programación Concurrente
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04.5_LTS-E95420?style=plastic&logo=ubuntu)
![Go](https://img.shields.io/badge/Go-1.27.1-00ADD8?style=plastic&logo=go)
![Python](https://img.shields.io/badge/Python-3.12.3-3776AB?style=plastic&logo=python)
![Ada](https://img.shields.io/badge/Ada-13.3.0-000000?style=plastic&logo=ada)
![C](https://img.shields.io/badge/C-13.3.0-A8B9CC?style=plastic&logo=c)
![Java](https://img.shields.io/badge/Java-OpenJDK_27-000000?style=plastic&logo=openjdk)

## Descripción

Soluciones a los ejercicios y prácticas del curso de **Programación Concurrente** de la **Universidad de las Islas Baleares (UIB)**, impartido por el **Dr. Miquel Mascaró Oliver**.

Las **implementaciones** a los problemas propuestos se presentan en los siguientes lenguajes: **Python**, **Go**, **Ada**, **C** y **Java**. 

El uso de múltiples tipos de lenguajes permite el **acercamiento desde diferentes ángulos al problema** en función de las capacidades que ofrece el lenguaje para enfrentar la gestión concurrente de procesos e hilos.

## Contenido 

### 1. El problema de la Región Crítica
Algoritmos clásicos para problemas con **2 procesos**:
- Algoritmo de *Dekker*
- Algoritmo de *Peterson*
- Algoritmo de *Doran-Thomas*

Algoritmos clásicos para problemas con **N procesos**:
- Algoritmo de *Lamport* (**Panadería**)
- Algoritmo *Rápido* de Lamport

**Soporte Hardware (Primitivas)**:
- *Test-and-Set*
- *Swap* 
- *Compare-and-Swap* (CAS)

### 2. Mecanismos para la Sincronización de Procesos
- **Semáforos:** Semáforos binarios, contadores y barreras
- **Monitores:** Variables de condición y señalización
- **Canales:** Canales en Go, modelo Rendezvous

### 3. Soluciones a Problemas Clásicos de Concurrencia
- Productor-Consumidor
- Lectores-Escritores
- Cena de los Filósofos

## Consideraciones del Repositorio

**Entorno de desarrollo:**

- **OS:** `Ubuntu`; release 24.04.5 LTS
- **IDEs:** `Visual Studio Code` e `IntelliJ` (Implementaciones en Java)

**Compiladores e intérpretes utilizados:**
- **Python:** `python3` - v3.12.3
- **Java:** `OpenJDK` - v27
- **Ada:** `gnat` - v13.3.0
- **Go:** `go` - v1.27.1
- **C:** `gcc` - v13.3.0

>**Nota:** Las soluciones han sido desarrolladas de forma individual con **fines puramente educativos** y de **estudio personal**.