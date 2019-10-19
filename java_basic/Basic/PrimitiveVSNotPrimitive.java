package Basic;

public class PrimitiveVSNotPrimitive {
  public static void main(String[] args) {

    //VALTOZOK
    // tipus - nev - deklaralas - ertekadas - pontos vesszo
    //int kl;
   // System.out.println(kl);

    // Integer a = 3324324;
    ///long b = 432234343432433423l;
    //// System.out.println(a + 1);

    //  String c  = "20";

    //SCOPE -
    /*int oo = 99;
    for (int i = 0; i < 5; i++) {

     // int oo = 99;
      oo++;
      if (oo == 102){
        System.out.println("egyenlo");
        return;
       // break;
      }
      System.out.println(oo);
    }
    System.out.println("vege");
*/
  /*  int kulso = 100;
    for (int i = 0; i <2 ; i++) {
      int belso = 50;
      System.out.println(belso + kulso);
    }
    System.out.println(belso + kulso);*/


    // System.out.println(k);


    // CASTING - TRANSZFORMALAS
    //c = k.toString();
    //int k = Integer.parseInt(c);
    //Integer k = Integer.parseInt(c);
    ///Integer k = 99999999;
    /// System.out.println(k.compareTo(a));

    //CHAINING - OSSZEFUZES
    // System.out.println(a.toString().toUpperCase().toCharArray().length);

    // STRING OSSZEFUZES

   /* String itemOne = "fdfsdf";
    String itemTwo = "ll";

    //STATIC - NON-STATIC
    // PrimitiveVSNotPrimitive primitiveVSNotPrimitive = new PrimitiveVSNotPrimitive();
    //primitiveVSNotPrimitive.TwoString(itemOne, itemTwo);*/


    whatIf(99);
    whatIfSwitch(99);
  }




 /* void TwoString(String a, String b) {
    System.out.println(a + " " + b);
  }*/

  /*String twoStringReturnValueString(String a, String b){
   // System.out.println();
    int app = 9;
    return a +b;*/

  static void whatIf(int n) {
    if (n < 10) {
      System.out.println("kisebb tiznel");
    } else if (n < 20) {
      System.out.println("kisebb husznal");
    } else {
      System.out.println("nagyobb husznal");
      //else nelkul
    }
  }

  private static void whatIfSwitch(int i) {
    switch (i)
    {
      case 10:
        System.out.println(10);
      case 20:
        System.out.println(20);
      default:
        System.out.println("default");
    }
  }
}



