package SOLID.LiskovSubstitution;

public class ElectricCar implements Car {

  // NEM TUDJA a MOTORCAR helyettesiteni a CAR-t, mert nem minden subclassban van motor -> ujra gondolni
  public void turnOnEngine() {
    throw new AssertionError("I don't have an engine!");
  }

  public void accelerate() {
    //this acceleration is crazy!
  }
}
