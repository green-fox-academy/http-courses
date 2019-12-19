import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Egyszamjatek {

  private static final String gameFile = "assets/egyszamjatek1.txt";

  public static void main(String[] args) {

    // 2. feladat
    List<String> fileContent = readFile(gameFile);
    List<Player> players = parsePlayers(fileContent);

    // 3. feladat
    System.out.printf("3. feladat: Jatekosok szama: %d fo\n", players.size());

    // 4. feladat
    Scanner scanner = new Scanner(System.in);
    System.out.print("4. feladat: Kerem a fordulo sorszamat: ");
    int turnIndex = scanner.nextInt() - 1;

    // 5. feladat
    float average = calculateAverage(players, turnIndex);
    System.out.printf("5. feladat: A megadott fordulo tippjeinek atlaga: %.2f\n", average);

  }

  private static float calculateAverage(List<Player> players, int turnIndex) {
    int sumTips = 0;
    for (Player player : players) {
      sumTips += player.tips.get(turnIndex);
    }
    float average = (float) sumTips / players.size();
    return average;
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
