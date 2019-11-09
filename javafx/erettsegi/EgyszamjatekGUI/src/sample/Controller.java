package sample;

import javafx.fxml.FXML;
import javafx.scene.control.*;

public class Controller {

  @FXML
  private TextField tippekTextField;
  @FXML
  private Label tippekLabel;

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

}
