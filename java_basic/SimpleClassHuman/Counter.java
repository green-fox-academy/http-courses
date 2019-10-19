package SimpleClassHuman;

public class Counter {
  int counterNotStatic = 0;
  static int counter = 0;
  //final static int counterFinal = 0;

  public Counter() {
    this.counterNotStatic++;
    this.counter++;
   // this.counterFinal++;
    System.out.println(counterNotStatic);
    System.out.println(counter);
  }

  public int getCounterNotStatic() {
    return counterNotStatic;
  }

  public void setCounterNotStatic(int counterNotStatic) {
    this.counterNotStatic = counterNotStatic;
  }

  public static int getCounter() {
    return counter;
  }

  public static void setCounter(int counter) {
    Counter.counter = counter;
  }
}
