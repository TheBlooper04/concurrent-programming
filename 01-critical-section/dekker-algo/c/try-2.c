#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

#define MAX_VALUE 1000000
#define NUM_THREADS 2

typedef struct tdata_t { 
    int tid;
    int *counter;
} tdata_t;

int want_cs[NUM_THREADS] = {0, 0};

void *count(void * ptr) {
    tdata_t *thread_data = ptr;
    int tid = thread_data->tid;
    int *counter = thread_data->counter;

    for(int i = 0; i < MAX_VALUE / NUM_THREADS; i++) {
        int other_tid = (tid + 1) % NUM_THREADS;
        while(want_cs[other_tid]);
        want_cs[tid] = 1;
        
        (*counter)++;
       
        want_cs[tid] = 0;
    }
    return NULL;
}

int main() {
    int counter = 0;

    pthread_t threads[NUM_THREADS];
    tdata_t threads_data[NUM_THREADS];

    for(int i = 0; i < NUM_THREADS; i++) {
        threads_data[i].tid = i;
        threads_data[i].counter = &counter;
        pthread_create(&threads[i], NULL, count, &threads_data[i]);
    }

    for(int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Counter value: %d | Expected value: %d\n", counter, MAX_VALUE);
    return 0;
}