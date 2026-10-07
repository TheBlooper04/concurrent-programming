import java.util.concurrent.atomic.AtomicInteger;

public class AtomicCounter implements Counter {
    private final AtomicInteger counterValue;

    public AtomicCounter() {
        this.counterValue = new AtomicInteger();
    }

    @Override
    public void add(int value) {
        counterValue.getAndAdd(value);
    }

    @Override
    public int getCounterValue() {
        return counterValue.get();
    }
}
