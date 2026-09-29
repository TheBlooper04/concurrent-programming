import threading

MAX_VALUE = 1_000_000
NUM_THREADS = 2

want_cs = [0, 0]
counter = 0

def count(tid: int) -> None:
    global counter
    for _ in range(MAX_VALUE // NUM_THREADS):
        # Entry protocol
        other_thread_id = (tid + 1) % NUM_THREADS
        if tid == 0:
            if want_cs[other_thread_id] == -1:
                want_cs[tid] = -1
            else:
                want_cs[tid] = 1

            while want_cs[tid] == want_cs[other_thread_id]:
                pass

        if tid == 1:
            if want_cs[other_thread_id] == -1:
                want_cs[tid] = 1
            else:
                want_cs[tid] = -1

            while want_cs[other_thread_id] == -want_cs[tid]:
                pass
            
        # Critical Section
        counter += 1

        # Exit protocol
        want_cs[tid] = 0



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
