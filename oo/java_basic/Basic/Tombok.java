package Basic;

import java.util.ArrayList;
import java.util.List;

public class Tombok {
  public static void main(String[] args) {
    //TOMB

    
    String[] arrayRefVar = new String[4];

    double[] myList = {1.9, 2.9, 3.4, 3.5};
    myList[1] = 9;
    System.out.println(myList[1]);
    System.out.println(myList.length);


    //LISTAK

    /*java.util.List <Integer> practiceList = new ArrayList<>();
    for (int i = 10; i <20 ; i++) {
      practiceList.add(i);
    }
    System.out.println(practiceList);

    practiceList.remove(new Integer(19));
    practiceList.remove(0);
    System.out.println(practiceList);



    List <Integer> addMe = practiceList;
    practiceList.addAll(addMe);
    System.out.println(practiceList);

    practiceList.set(practiceList.size() -1, 999);
    System.out.println(practiceList);

    System.out.println();
    System.out.println(practiceList.isEmpty());

    System.out.println();
    System.out.println(practiceList.contains(15));


    for (Integer integer: practiceList) {
      System.out.print(String.valueOf(integer) + "aa");
    }

    practiceList.clear();

    System.out.println(practiceList);

    printAlphabet();

  }

  private static void printAlphabet() {
    int j= 1;
    List <Character> listChars = new ArrayList<>();

    for (char i='a';i<='z';i++) {
      listChars.add(i);
    }
    System.out.print("ABC : ");
    Object [] a=listChars.toArray();
    System.out.println();
    for(int i=0 ;i<a.length;i++){
      System.out.println( j++ +": "+ a[i]);
    }
  }*/
}

