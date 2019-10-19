package InheritanceOroklodes;

public class Hangszer {
  private String nev;
  private String hang;
  private int ar;

  public Hangszer() {
    this.nev = "hangszer";
    this.hang = "brumbrum";
    this.ar= 500;
  }

  public Hangszer(String nev, String hang, int ar) {
    this.nev = nev;
    this.hang = hang;
    this.ar = ar;
  }

  public String getNev() {
    return nev;
  }

  public void setNev(String nev) {
    this.nev = nev;
  }

  public String getHang() {
    return hang;
  }

  public void setHang(String hang) {
    this.hang = hang;
  }

  public int getAr() {
    return ar;
  }

  public void setAr(int ar) {
    this.ar = ar;
  }

  public void zeneljVelem(){
    System.out.println("Az en hangom brumbrum es " + this.hang );
  }

}
