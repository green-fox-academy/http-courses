package SimpleClassHuman;

public class Main {
  public static void main(String[] args) {
    Human human = new Human();
   /* System.out.println(human.getName());
    System.out.println(Main.class.getName());
    System.out.println(" A te neved leszen " + human.name);
    System.out.println("A te korod legyen" + human.age);
    System.out.println(" Ezzel foglalkozzal" + human.getOccupation());*/

    Human human2 = new Human("olga", 44, "orgazda");
    System.out.println(human2.name);
    human2 = new Human();
    System.out.println(human2.name);


  //STATIC + FINAL

/*
    Counter counter = new Counter();
    Counter counter2 = new Counter();
    Counter counter3 = new Counter();*/


  }


}
