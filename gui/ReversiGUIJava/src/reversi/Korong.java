package reversi;

import javafx.scene.paint.Color;

public class Korong {

  char jatekos;
  int sor;
  int oszlop;
  Color szin;
  String szinNev;

  public Korong(char jatekos, int sor, int oszlop) {
    this.jatekos = jatekos;
    this.sor = sor;
    this.oszlop = oszlop;
    this.szin = korongSzin(jatekos);
    this.szinNev = szinNev(jatekos);
  }

  private String szinNev(char c) {
    switch (c) {
      case 'F':
        return "FEHÉR";
      case 'K':
        return "KÉK";
      default:
        return  "";
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

}
