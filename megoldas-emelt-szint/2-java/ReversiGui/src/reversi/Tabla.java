package reversi;

import javafx.scene.Group;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;
import javafx.scene.shape.Circle;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Tabla {

  public static final int MEZO_MERET = 50;
  public static final int KOR_MERET = 40;

  char[][] allas;

  public Tabla(String fajlNev) {
    List<String> fajlTartalom = fajlBeolvasas(fajlNev);
    allas = kezdoAllas(fajlTartalom);
  }

  public void megjelenit(Group tablaElemek) {
    for (int i = 0; i < allas.length; i++) {
      for (int j = 0; j < allas[i].length; j++) {
        Paint korSzin = korSzin(allas[i][j]);
        Circle kor = new Circle(
                j * MEZO_MERET + MEZO_MERET / 2,
                i * MEZO_MERET + MEZO_MERET / 2,
                KOR_MERET / 2,
                korSzin
        );
        tablaElemek.getChildren().add(kor);
      }
    }
  }

  public boolean vanForditas(char jatekos, int sor, int oszlop, int iranySor, int iranyOszlop) {
    int aktSor, aktOszlop;
    char ellenfel;
    boolean nincsEllenfel;
    aktSor = sor + iranySor;
    aktOszlop = oszlop + iranyOszlop;
    ellenfel = 'K';
    if (jatekos == 'K') {
      ellenfel = 'F';
    }
    nincsEllenfel = true;
    while (aktSor > 0 && aktSor < 8 && aktOszlop > 0 && aktOszlop < 8 &&
            allas[aktSor][aktOszlop] == ellenfel) {
      aktSor += iranySor;
      aktOszlop += iranyOszlop;
      nincsEllenfel = false;
    }
    if (nincsEllenfel || aktSor < 0 || aktSor > 7 || aktOszlop < 0 || aktOszlop > 7 ||
            allas[aktSor][aktOszlop] != jatekos) {
      return false;
    }
    return true;
  }

  public boolean szabalyosLepes(char jatekos, int lepesSor, int lepesOszlop) {
    for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        if (vanForditas(jatekos, lepesSor, lepesOszlop, i, j)) return true;
      }
    }
    return false;
  }

  private Paint korSzin(char karakter) {
    if (karakter == '#') {
      return Color.DARKGRAY;
    } else if (karakter == 'F') {
      return Color.WHITE;
    } else if (karakter == 'K') {
      return Color.BLUE;
    } else {
      return Color.LIGHTGRAY;
    }
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
