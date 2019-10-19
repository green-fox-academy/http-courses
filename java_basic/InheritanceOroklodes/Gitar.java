package InheritanceOroklodes;

public class Gitar extends Hangszer {
  private int hurokSzama;

//OVERLOAD

  public Gitar() {
    this.setHang("nyenye");
    this.setNev("gitar");
    this.setAr(1222);
    this.hurokSzama = 6;

  }

  public Gitar(int hurokSzama) {
    this.hurokSzama = hurokSzama;
  }

  public Gitar(String nev, String hang, int ar, int hurokSzama) {
    super(nev, hang, ar);
    this.hurokSzama = hurokSzama;
  }

  @Override
  public void zeneljVelem() {
    System.out.println("Az en hangom nem brumbrum, hanem " + this.getHang());
  }

}
