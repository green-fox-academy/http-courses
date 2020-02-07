package egyszamjatek;

import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Controller {

  private static final String gameFile = "assets/egyszamjatek2.txt";
  private static List<Player> players;

  public Controller() {
    List<String> fileContent = readFile(gameFile);
    players = parsePlayers(fileContent);
  }

  @FXML private TextField playerNameTextField;
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

  @FXML
  public void addPlayer() {
    String playerName = playerNameTextField.getText();
    String playerTipStrings = tipsTextField.getText();

    boolean isPlayerNameValid = validatePlayerName(playerName);
    if (!isPlayerNameValid) return;

    boolean isTipsCountValid = validateTipsCount(playerTipStrings.split(" "));
    if (!isTipsCountValid) return;

    boolean isFileWriteSuccessful = writeFile(gameFile, playerName + " " + playerTipStrings);
    if (isFileWriteSuccessful) {
      showInfo("Az allomany bovitese sikeres volt!");
      clearFields();
    }

  }

  private void clearFields() {
    playerNameTextField.clear();
    tipsTextField.clear();
    tipsLabel.setText("0 db");
  }

  private boolean writeFile(String fileName, String newLine) {
    List<String> newContent = Arrays.asList(newLine);
    try {
      Files.write(Paths.get(fileName), newContent, StandardOpenOption.APPEND);
      return true;
    } catch (IOException e) {
      System.err.println("Nem sikerult a file irasa.");
      return false;
    }
  }

  private boolean validateTipsCount(String[] playerTipStrings) {
    int necessaryTips = players.get(0).tips.size();
    if (playerTipStrings.length != necessaryTips) {
      showError("A tippek szama nem megfelelo!");
      return false;
    }
    return true;
  }

  private boolean validatePlayerName(String playerName) {
    for (Player player : players) {
      if (player.name.equals(playerName)) {
        showError("Van mar ilyen nevu jatekos!");
        return false;
      }
    }
    return true;
  }

  private void showInfo(String content) {
    Alert alert = new Alert(Alert.AlertType.INFORMATION);
    alert.setTitle("Uzenet");
    alert.setHeaderText("");
    alert.setContentText(content);
    alert.showAndWait();
  }

  private void showError(String content) {
    Alert alert = new Alert(Alert.AlertType.ERROR);
    alert.setTitle("Hiba!");
    alert.setHeaderText("");
    alert.setContentText(content);
    alert.showAndWait();
  }

  private static List<Player> parsePlayers(List<String> fileContent) {
    List<Player> players = new ArrayList<>();

    for (String row : fileContent) {
      String[] playerData = row.split(" ");
      String playerName = playerData[0];

      Player player = new Player(playerName);

      List<Integer> tips = parseTips(Arrays.copyOfRange(playerData, 1, playerData.length));
      player.tips = tips;

      players.add(player);
    }

    return players;
  }

  private static List<Integer> parseTips(String[] tipStrings) {
    List<Integer> tips = new ArrayList<>();
    for (int i = 0; i < tipStrings.length; i++) {
      int tip = Integer.parseInt(tipStrings[i]);
      tips.add(tip);
    }
    return tips;
  }

  private static List<String> readFile(String fileName) {
    try {
      return Files.readAllLines(Paths.get(fileName));
    } catch (IOException e) {
      System.err.println("Nem sikerult beolvasni a filet.");
      return new ArrayList<>();
    }
  }

}
