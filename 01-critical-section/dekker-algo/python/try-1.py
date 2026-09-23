import threading

NUM_THREADS = 2
MAX_VALUE = 1_000_000

counter = 0
turn = 0

def count(tid: int) -> None:
    global turn, counter
    for _ in range(MAX_VALUE // NUM_THREADS):
        # Entry protocol: wait for its turn
        while turn != tid:      
            pass

        # Critical Section
        counter += 1

        # Exit protocol: pass turn to the other thread
        turn = (tid + 1) % NUM_THREADS

def main() -> None:
    threads = []

    for i in range(NUM_THREADS):
        t = threading.Thread(target=count, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Counter value: {counter} | Expected Value: {MAX_VALUE}")

if __name__ == "__main__":
    main()
