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
    allas = allasInicializalas(fajlTartalom);

  }

  private char[][] allasInicializalas(List<String> fajlTartalom) {
    char[][] allas = new char[fajlTartalom.size()][];
    for (int i = 0; i < fajlTartalom.size(); i++) {
      allas[i] = fajlTartalom.get(i).toCharArray();
    }
    return allas;
  }

  private List<String> fajlBeolvasas(String fajlNev) {
    try {
      return Files.readAllLines(Paths.get(fajlNev));
    } catch (IOException e) {
      System.out.println("Nem sikerult beolvasni a fajlt :(");
      return new ArrayList<>();
    }
  }
}
