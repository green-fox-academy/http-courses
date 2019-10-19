package InheritanceOroklodes;

import java.util.ArrayList;
import java.util.List;

public class MainInheritance {
  public static void main(String[] args) {
    Gitar gitar = new Gitar();
    Hegedu hegedu = new Hegedu();
    Furulya furulya = new Furulya();

    System.out.println(gitar.getHang());
    System.out.println(hegedu.getHang());
    System.out.println(furulya.getHang());
    System.out.println();

    furulya.zeneljVelem();
    hegedu.zeneljVelem();
    gitar.zeneljVelem();
    System.out.println();

    Hangszer hangszer = new Gitar();
    List<Hangszer> hangszerek = new ArrayList<>();

    System.out.println(hangszer.getHang());
    System.out.println();
    hangszerek.add(hegedu);
    hangszerek.add(gitar);
    hangszerek.add(hangszer);
    hangszerek.add(furulya);

    for (Hangszer hangszer2: hangszerek) {
      System.out.println(hangszer2.getHang());
    }
  }


}
