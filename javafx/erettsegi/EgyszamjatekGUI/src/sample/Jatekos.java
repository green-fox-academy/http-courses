package sample;

import java.util.Arrays;

public class Jatekos {

  String name;
  int[] tippek;

  public Jatekos(String name, int[] tippek) {
    this.name = name;
    this.tippek = tippek;
  }

  @Override
  public String toString() {
    return "Jatekos{" +
            "name='" + name + '\'' +
            ", tippek=" + Arrays.toString(tippek) +
            '}';
  }

}
