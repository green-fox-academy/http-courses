package egyszamjatek;

import javafx.fxml.FXML;
import javafx.scene.control.*;

public class Controller {

  @FXML private TextField tipsTextField;
  @FXML private Label tipsLabel;

  @FXML
  public void updateTipsCount() {
    String tipsText = tipsTextField.getText();
    if (tipsText.isEmpty()) {
      tipsLabel.setText("0 db");
      return;
    }

    int tipsCount = tipsText.split(" ").length;
    tipsLabel.setText(tipsCount + " db");
  }

}
