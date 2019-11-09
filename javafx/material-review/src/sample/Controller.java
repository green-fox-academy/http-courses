package sample;

import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;

public class Controller {

  @FXML
  AnchorPane loginPane;
  @FXML
  AnchorPane profilePane;
  @FXML
  TextField usernameTextField;
  @FXML
  PasswordField passwordField;
  @FXML
  Label successLabel;
  @FXML
  Label profileUserNameLabel;
  @FXML
  CheckBox termsOfUseCheckbox;

  @FXML
  private void signIn() {
    String userName = usernameTextField.getText();
    String password = passwordField.getText();
    if (userName.isEmpty()) {
      showError("Nincs felhasznalonev megadva");
    } else if (!password.equals("jelszo")) {
      showError("Nem megfelelo jelszo");
    } else if (!termsOfUseCheckbox.isSelected()) {
      showError("Nem fogadtad el a felhasznalasi felteteleket!");
    } else {
      loginPane.setVisible(false);
      profileUserNameLabel.setText(userName);
      profilePane.setVisible(true);
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