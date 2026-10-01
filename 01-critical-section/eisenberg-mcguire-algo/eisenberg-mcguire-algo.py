import threading
import random

MAX_VALUE = 1_000_000
NUM_THREADS = 10

counter = 0

threads_status = ["IDLE" for _ in range(NUM_THREADS)]
turn = random.randint(0, NUM_THREADS - 1)

def count(tid: int) -> None:
    global turn, counter

    for _ in range(MAX_VALUE // NUM_THREADS):
        # Entry protocol
        repeat = True
        while repeat:
            threads_status[tid] = "WAITING"

            idx = turn
            while idx != tid:
                if threads_status[idx] != "IDLE":
                    idx = turn
                else:
                    idx = (idx + 1) % NUM_THREADS

            threads_status[tid] = "ACTIVE"

            idx = 0
            while idx < NUM_THREADS and (idx == tid or threads_status[idx] != "ACTIVE"):
                idx = idx + 1

            if idx >= NUM_THREADS and (turn == tid or threads_status[turn] == "IDLE"):
                repeat = False
        turn = tid

        # Critical Section
        counter += 1

        # Exit protocol
        idx = (turn + 1) % NUM_THREADS
        while threads_status[idx] == "IDLE":
            idx = (idx + 1) % NUM_THREADS
        turn = idx
        threads_status[tid] = "IDLE"

def main() -> None:
    threads = []

    for i in range(NUM_THREADS):
        t = threading.Thread(target=count, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Counter value: {counter} | Expected value: {MAX_VALUE}")

if __name__ == "__main__":
    main()