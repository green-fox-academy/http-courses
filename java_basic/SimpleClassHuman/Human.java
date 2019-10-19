package SimpleClassHuman;

public class Human {
  //OSZTALYVALTOZOK
  public String name;
  int age;
  private String occupation;
  protected String hobby;


  //CONSTRUCTOROK - KELL MINDIG EGY URES IS


  public Human() {
    name = "kata";
    age = 55;
    occupation = "szerencsejatekos";
  }

  public Human(String name, int age, String occupation) {
    this.name = name;
    this.age = age;
    this.occupation = occupation;
  }

  //GETTER es SETTER


  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }

  public String getOccupation() {
    return occupation;
  }

  public void setOccupation(String occupation) {
    this.occupation = occupation;
  }

  //FUGGVENYEK - NEM AJANLOTT - SINGLE RESPONSIBILITY
  protected String writeName(){
    return this.name;
  }
}
