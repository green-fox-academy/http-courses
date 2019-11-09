package sample;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;

public class Controller {

  @FXML
  TextField usernameTextField;
  @FXML
  PasswordField passwordField;
  @FXML
  Label successLabel;

  @FXML
  private void signIn() {
    String userName = usernameTextField.getText();
    String password = passwordField.getText();
    if (userName.isEmpty()) {
      showError("Nincs felhasznalonev megadva");
    } else if (!password.equals("jelszo")) {
      showError("Nem megfelelo jelszo");
    } else {
      successLabel.setText("Sikeres bejelentkezes: " + userName);
    }
  }

  private void showError(String message) {
    Alert alert = new Alert(Alert.AlertType.ERROR);
    alert.setTitle("Hiba!!!");
    alert.setHeaderText("");
    alert.setContentText(message);
    alert.showAndWait();
  }

}