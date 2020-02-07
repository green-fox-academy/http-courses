package egyszamjatek;

import java.util.ArrayList;
import java.util.List;

public class Player {

  String name;
  List<Integer> tips;

  public Player(String name) {
    this.name = name;
    tips = new ArrayList<>();
  }

}
