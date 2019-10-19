package Basic;

import java.util.Scanner;

public class StringParancsok {
  public static void main(String[] args) {

    String a = "cica kutya";
    String b = "cica";


    System.out.println(a.length());
    System.out.println(a.substring(0, 2));
    System.out.println(a.charAt(0));
    System.out.println(a.equals(b));
   /* System.out.println(a.toUpperCase());
    System.out.println(a.contains("cic"));
    System.out.println(a.endsWith("a"));
    System.out.println(a.startsWith("c"));
    System.out.println(a.startsWith("ca"));
    System.out.println(a.indexOf("c"));*/
    String [] splitArray = a.split(" ", 3);
    System.out.println(splitArray.toString());
    for (String c: splitArray) {
      System.out.println(c);
    }


 /*   System.out.println("Mi a neved?");
    Scanner scanner = new Scanner(System.in);
    String answer = scanner.nextLine();
    System.out.println("Te neved mar pedig az. hogy " + answer);*/


  }
}
