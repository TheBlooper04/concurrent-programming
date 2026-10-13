#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

#define MAX_VALUE   1000000
#define NUM_THREADS 2

typedef struct tdata_t {
    int tid;
    int *counter;
} tdata_t;

int want_cs[NUM_THREADS] = {0, 0};
int turn = 0;

void *count(void *ptr) {
    tdata_t *tdata = ptr;
    int tid = tdata->tid;
    int *counter = tdata->counter;

    for(int i = 0; i < MAX_VALUE / NUM_THREADS; i++) {
        want_cs[tid] = 1;
        int other_tid = (tid + 1) % NUM_THREADS;
        while(want_cs[other_tid]) {
            if(turn != tid) {
                want_cs[tid] = 0;
                while(turn != tid);
                want_cs[tid] = 1;
            }
        }
        
        printf("Thread %d: adding 1 to the counter.\n", tid);
        *counter += 1;

        want_cs[tid] = 0;
        turn = other_tid;
    }
    return NULL;
}

int main() {
    int counter = 0;

    pthread_t threads[NUM_THREADS];
    tdata_t pthreads_data[NUM_THREADS];
    for(int i = 0; i < NUM_THREADS; i++) {
        pthreads_data[i].tid = i;
        pthreads_data[i].counter = &counter;
        pthread_create(&threads[i], NULL, count, &pthreads_data[i]);
    }

    for(int i =0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Counter value: %d | Expected value: %d\n", counter, MAX_VALUE);

    return 0;
}