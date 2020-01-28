package reversi;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Tabla {

  char[][] allas;

  public Tabla(String fajlNev) {
    List<String> fajlTartalom = fajlBeolvasas(fajlNev);
    allas = kezdoAllas(fajlTartalom);
  }

  private char[][] kezdoAllas(List<String> fajlTartalom) {
    if (fajlTartalom.isEmpty()) return new char[8][8];

    char[][] allas = new char[fajlTartalom.size()][fajlTartalom.get(0).length()];
    for (int i = 0; i < fajlTartalom.size(); i++) {
      allas[i] = fajlTartalom.get(i).toCharArray();
    }
    return allas;
  }

  private List<String> fajlBeolvasas(String fajlNev) {
    try {
      return Files.readAllLines(Paths.get(fajlNev));
    } catch (IOException e) {
      System.err.println("Nem sikerult beolvasni a fajlt :(");
      return new ArrayList<>();
    }
  }

}
