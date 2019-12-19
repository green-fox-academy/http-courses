import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Egyszamjatek {

  private static final String gameFile = "assets/egyszamjatek1.txt";

  public static void main(String[] args) {

    // 1. feladat
    List<String> fileContent = readFile(gameFile);
    List<Player> players = parsePlayers(fileContent);

  }

  private static List<Player> parsePlayers(List<String> fileContent) {
    List<Player> players = new ArrayList<>();

    for (String row : fileContent) {
      String[] playerData = row.split(" ");
      String playerName = playerData[0];

      Player player = new Player(playerName);

      for (int i = 1; i < playerData.length; i++) {
        int tip = Integer.parseInt(playerData[i]);
        player.tips.add(tip);
      }

      players.add(player);
    }

    return players;
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
