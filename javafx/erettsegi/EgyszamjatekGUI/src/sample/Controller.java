package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;

import java.io.IOException;
import java.nio.Buffer;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.OpenOption;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;

public class Controller {

  private static final String fajlNev = "egyszamjatek2.txt";
  @FXML
  private TextField tippekTextField;
  @FXML
  private TextField jatekosNevTextField;
  @FXML
  private Label tippekLabel;
  @FXML
  private Button listazzButton;
  @FXML
  private ComboBox namesComboBox;
  @FXML
  private ListView nevLista;
  @FXML
  private AnchorPane basePane;

  List<Jatekos> jatekosok;

  public Controller() {
    List<String> fajltartalom = fajlbeolvasas(fajlNev);
    jatekosok = jatekosBeolvasas(fajltartalom);
  }

  @FXML
  private void nevekListazasa() {
    int y = 0;
    for (Jatekos jatekos : jatekosok) {
      namesComboBox.getItems().add(jatekos.name);
      nevLista.getItems().add(jatekos.name);

      Button button = new Button();
      button.setId(jatekos.name);
      button.setText(jatekos.name);
      button.setLayoutY(y);
      button.setOnAction((event) -> buttonAction(event));
      basePane.getChildren().add(button);
      y += 30;
    }
  }

  private void buttonAction(ActionEvent event) {
    Button button = (Button) (event.getSource());
    System.out.println(button.getId());
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

    fajlhozIras(fajlNev, nev + " " + tippekSzoveg.trim() + "\r\n");
    infoUzenet("Az allomany bovitese sikeres volt");
    mezokTartalmanakTorlese();
  }

  private void mezokTartalmanakTorlese() {
    jatekosNevTextField.setText("");
    tippekTextField.setText("");
    tippekLabel.setText("0 db");
  }

  private void infoUzenet(String uzenet) {
    Alert alert = new Alert(Alert.AlertType.INFORMATION);
    alert.setTitle("Uzenet");
    alert.setHeaderText("");
    alert.setContentText(uzenet);
    alert.showAndWait();
  }

  private void fajlhozIras(String fajlNev, String ujSor) {
    try {
      Files.write(Paths.get(fajlNev), ujSor.getBytes(), StandardOpenOption.APPEND);
    } catch (IOException e) {
      System.err.println("Nem sikerult fajba irni");
      System.exit(1);
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
