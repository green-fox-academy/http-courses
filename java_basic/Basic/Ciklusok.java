package Basic;

public class Ciklusok {
  public static void main(String[] args) {

    showForLoop(4);
    //nestedForLopop(4, 5);
    //showWhileLoop(9);
   // doWhile(9);
  }


  private static void showForLoop(int i) {
    int counter = 0;
    for (int j = 0; j < i ; j++) {
      System.out.println(counter);
      counter++;
    }
  }

 /* private static void nestedForLopop(int k, int l) {
    for (int i = 0; i <k ; i++) {
     System.out.println("PAFF");
      for (int j = 0; j < l; j++) {
        System.out.print("puff");
      }
      // System.out.println("PAFF");
    }
  }*/

 /* private static void showWhileLoop(int p) {
    int counter = 0;
    while (counter < p){
      System.out.println("kisebb vagyok " + counter);
    }
  }*/

 /* private static void doWhile(int k) {
    int counter = 0;
    do {
      System.out.println("Still smaller");
      counter++;
    }
    while (counter < k);
  }*/

}
