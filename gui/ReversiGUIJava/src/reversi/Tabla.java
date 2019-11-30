package reversi;

import javafx.event.EventHandler;
import javafx.scene.Group;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Tabla {

  private Stage stage;
  private char[][] allas;
  private Korong aktualisJatekos;

  public Tabla(String fajlNev, Stage stage) {
    this.stage = stage;
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
        Korong korong = new Korong(allas[sor][oszlop], sor, oszlop);

        int x = oszlop * mezoMeret + terkoz + korongRadius;
        int y = sor * mezoMeret + terkoz + korongRadius;
        Paint korongSzin = Paint.valueOf(korong.szin.toString());
        Circle kor = new Circle(x, y, korongRadius, korongSzin);
        group.getChildren().add(kor);

        kor.setUserData(korong);
        kor.addEventHandler(MouseEvent.MOUSE_CLICKED, kattintasKezelo());
      }
    }
  }

  private EventHandler<MouseEvent> kattintasKezelo() {
    return event -> {
      Circle kor = ((Circle) event.getSource());
      Korong korong = (Korong) kor.getUserData();
      if (korong.jatekos == '#' && aktualisJatekos != null) {
        szabalyosEllenorzes(korong);
      } else {
        jatekosBeallitasa(korong);
      }
    };
  }

  private void szabalyosEllenorzes(Korong korong) {
    String szabalyosSzoveg = szabalyosLepes(aktualisJatekos.jatekos, korong.sor, korong.oszlop)
            ? " > SZABÁLYOS" : " > SZABÁLYTALAN";
    stage.setTitle("Reversi - " + aktualisJatekos.szinNev + szabalyosSzoveg);
  }

  private void jatekosBeallitasa(Korong korong) {
    aktualisJatekos = korong;
    String jatekosSzine = " - " + korong.szinNev;
    String cim = "Reversi" + jatekosSzine;
    stage.setTitle(cim);
  }

  public boolean szabalyosLepes(char jatekos, int sor, int oszlop) {
    if (allas[sor][oszlop] != '#') return false;
    for (int sorIrany = -1; sorIrany <= 1; sorIrany++) {
      for (int oszlopIrany = -1; oszlopIrany <= 1; oszlopIrany++) {
        if (vanForditas(jatekos, sor, oszlop, sorIrany, oszlopIrany)) {
          return true;
        }
      }
    }
    return false;
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
    while (aktSor > 0 && aktSor < allas.length
            && aktOszlop > 0 && aktOszlop < allas.length
            && allas[aktSor][aktOszlop] == ellenfel) {
      aktSor += iranySor;
      aktOszlop += iranyOszlop;
      nincsEllenfel = false;
    }
    if (nincsEllenfel
            || aktSor < 0 || aktSor > allas.length - 1
            || aktOszlop < 0 || aktOszlop > allas.length - 1
            || allas[aktSor][aktOszlop] != jatekos) {
      return false;
    }
    return true;
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
