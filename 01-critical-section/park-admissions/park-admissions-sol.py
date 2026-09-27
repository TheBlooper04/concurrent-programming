from datetime import datetime
import threading
import random
import time

MIN_DELAY = 0       # in ms 
MAX_DELAY = 5000    # in ms
MAX_ACCESSES = 10
NUM_THREADS = 2

time_dif = [0.0, 0.0]
want_cs = [False, False]
turn = 0
counter = 0
def enter(tid: int) -> None:
    global counter, turn

    first_access_time: datetime | None = None
    for i in range(MAX_ACCESSES):
        delay = random.randint(MIN_DELAY, MAX_DELAY)
        time.sleep(delay / 1000.0)

        # Entry protocol
        want_cs[tid] = True
        other_thread_id = (tid + 1) % NUM_THREADS
        turn = other_thread_id
        while want_cs[other_thread_id] and turn == other_thread_id:
            pass

        # Critical section
        access_time = datetime.now()

        if i == 0:
            first_access_time = access_time

        counter += 1
        print(f"Door number: {tid} | Accesses: {i + 1} | Time {counter}: {access_time.strftime('%H:%M:%S:%f')[:-3]}")

        # Exit protocol
        want_cs[tid] = False

    difference = access_time - first_access_time
    time_dif[tid] = difference.total_seconds()

def main() -> None:
    threads = []

    for i in range(NUM_THREADS):
        t = threading.Thread(target=enter, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Total accesses: {counter}")
    for i in range(NUM_THREADS):
        avg_time = time_dif[i] / (MAX_ACCESSES - 1)
        print(f"Door {i} - Average Time: {avg_time:.3f} s")

if __name__ == "__main__":
    main()