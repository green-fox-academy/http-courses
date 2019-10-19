package InheritanceOroklodes;

public class Hegedu extends Hangszer {
  private int hurokSzama;

  public Hegedu() {
    this.setHang("nyenye");
    this.setNev("gitar");
    this.setAr(1222);
    this.hurokSzama = 6;
  }

  public Hegedu(String nev, String hang, int ar, int hurokSzama) {
    super(nev, hang, ar);
    this.hurokSzama = hurokSzama;
  }

  public int getHurokSzama() {
    return hurokSzama;
  }

  public void setHurokSzama(int hurokSzama) {
    this.hurokSzama = hurokSzama;
  }

}
