import threading

MAX_VALUE = 1_000_000
NUM_THREADS = 2

want_cs = [False, False]
counter = 0

def count(tid: int) -> None:
    global want_cs, counter
    for _ in range(MAX_VALUE // NUM_THREADS):
        # Entry protocol
        other_thread_id = (tid + 1) % NUM_THREADS
        while want_cs[other_thread_id] == True:
            pass
        want_cs[tid] = True

        # Critical Section
        counter += 1

        # Exit protocol
        want_cs[tid] = False

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