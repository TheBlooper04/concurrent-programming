public class Main {
    private static final int MAX_VALUE = 1_000_000;
    private static final int NUM_THREADS = 10;

    public static void main(String[] args) throws InterruptedException {
        Main application = new Main();
        application.run();
    }

    private void run() throws InterruptedException {
        Thread[] threads = new Thread[NUM_THREADS];

        final int iterations = MAX_VALUE / NUM_THREADS;
        final Counter counter = new AtomicCounter();

        for(int i = 0; i < threads.length; i++) {
            threads[i] = new Thread(new Worker(i, iterations, counter));
            threads[i].start();
        }

        for(Thread t : threads) {
            t.join();
        }

        System.out.printf("Counter value: %d | Expected value: %d\n", counter.getCounterValue(), MAX_VALUE);
    }
}