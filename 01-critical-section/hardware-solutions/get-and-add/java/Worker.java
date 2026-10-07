public class Worker implements Runnable {
    private static final int ADDED_VALUE = 1;

    private final int id;
    private final int iterations;
    private final Counter counter;

    public Worker(int id, int iterations, Counter counter) {
        this.id = id;
        this.iterations = iterations;
        this.counter = counter;
    }

    @Override
    public void run() {
        for (int i = 0; i < iterations; i++) {
            System.out.printf("Thread %d: adding 1 to the counter.\n", id);
            counter.add(ADDED_VALUE);
        }
    }
}
