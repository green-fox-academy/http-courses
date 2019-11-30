package reversi;

import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Tabla {

  private char[][] allas;

  public Tabla(String fajlNev) {
    List<String> fajlTartalom = fajlBeolvasas(fajlNev);
    allas = allasInicializalas(fajlTartalom);

  }

  public void megjelenit(Group group, int szelesseg, int magassag) {
    Paint hatterSzin = Paint.valueOf(Color.LIGHTGRAY.toString());
    Rectangle hatter = new Rectangle(szelesseg, magassag, hatterSzin);
    group.getChildren().add(hatter);

    int mezoMeret = Math.min(szelesseg, magassag) / allas.length;
    int terkoz = 5;
    int korongRadius = (mezoMeret - 2 * terkoz) / 2;

    for (int sor = 0; sor < allas.length; sor++) {
      for (int oszlop = 0; oszlop < allas[sor].length; oszlop++) {
        int x = oszlop * mezoMeret + terkoz + korongRadius;
        int y = sor * mezoMeret + terkoz + korongRadius;
        Color szin = korongSzin(allas[sor][oszlop]);
        Paint korongSzin = Paint.valueOf(szin.toString());
        Circle korong = new Circle(x, y, korongRadius, korongSzin);
        group.getChildren().add(korong);
      }
    }
  }

  private Color korongSzin(char c) {
    if (c == 'F') {
      return Color.WHITE;
    } else if (c == 'K') {
      return Color.BLUE;
    } else {
      return Color.DARKGRAY;
    }
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
