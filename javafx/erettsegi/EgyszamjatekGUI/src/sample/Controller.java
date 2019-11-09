package sample;

import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Controller {

  @FXML
  private TextField tippekTextField;
  @FXML
  private TextField jatekosNevTextField;
  @FXML
  private Label tippekLabel;

  List<Jatekos> jatekosok;

  public Controller() {
    List<String> fajltartalom = fajlbeolvasas("egyszamjatek2.txt");
    jatekosok = jatekosBeolvasas(fajltartalom);
  }

  @FXML
  private void tippSzamlalo() {
    String tippekSzoveg = tippekTextField.getText();
    if (tippekSzoveg.isEmpty()) {
      tippekLabel.setText("0 db");

    } else {
      String[] tippekDarabolva = tippekSzoveg.split(" ");
      tippekLabel.setText(tippekDarabolva.length + " db");
    }
  }

  @FXML
  private void jatekosMentese() {
    String nev = jatekosNevTextField.getText();
    for (Jatekos jatekos : jatekosok) {
      if (jatekos.name.equals(nev)) {
        errorUzenet("Van mar ilyen nevu jatekos!");
        return;
      }
    }

    String tippekSzoveg = tippekTextField.getText();
    int tippekSzama = tippekSzoveg.split(" ").length;
    if (tippekSzama != jatekosok.get(0).tippek.length) {
      errorUzenet("A tippek szama nem megfelelo");
      return;
    }
  }

  private void errorUzenet(String uzenet) {
    Alert alert = new Alert(Alert.AlertType.ERROR);
    alert.setTitle("Hiba!");
    alert.setHeaderText("");
    alert.setContentText(uzenet);
    alert.showAndWait();
  }


  private List<Jatekos> jatekosBeolvasas(List<String> fajlTartalom) {
    List<Jatekos> jatekosok = new ArrayList<>();
    for (String jatekosSzoveg : fajlTartalom) {
      String[] jatekosAdatok = jatekosSzoveg.split(" ");
      String nev = jatekosAdatok[0];
      int[] tippek = jatekosTippekBegyujtese(jatekosAdatok);
      Jatekos jatekos = new Jatekos(nev, tippek);
      jatekosok.add(jatekos);
    }
    return jatekosok;
  }

  private int[] jatekosTippekBegyujtese(String[] jatekosAdatok) {
    int[] tippek = new int[jatekosAdatok.length - 1];
    for (int i = 1; i < jatekosAdatok.length; i++) {
      tippek[i - 1] = Integer.parseInt(jatekosAdatok[i]);
    }
    return tippek;
  }

  private List<String> fajlbeolvasas(String fajlNev) {
    try {
      return Files.readAllLines(Paths.get(fajlNev), Charset.forName("utf-8"));
    } catch (IOException e) {
      System.err.println("Nem sikerult beolvasni a fajlt.");
      return new ArrayList<>();
    }
  }

}
