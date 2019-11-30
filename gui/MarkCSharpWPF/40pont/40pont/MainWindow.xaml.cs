using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Drawing;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace _40pont
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>

    public enum Allapot
    {
        URES,
        TEHETSZ,
        VILAGOS,
        SOTET,
    }
    public struct Elem
    {
        public Allapot allapot;
        public int x;
        public int y;
        public Elem(Allapot a, int b, int c)
        {
            this.allapot = a;
            this.x = b;
            this.y = c;
        }
    }

    public class Jatek
    {
        int dim = 8; 
        public bool vilagosVanE;
        public List<List<Elem>> jatekTer;

        public Jatek()
        {
            jatekTer = new List<List<Elem>>();
            for (int sor = 0; sor < dim; sor++)
            {
                List<Elem> sorbanLevoElemek = new List<Elem>();

                for (int oszlop = 0; oszlop < dim; oszlop++)
                {
                    if(sor == oszlop)
                    {
                        sorbanLevoElemek.Add(new Elem(Allapot.SOTET,sor, oszlop) );
                    }
                    else
                    {
                        sorbanLevoElemek.Add(new Elem(Allapot.URES, sor, oszlop));
                    }
                }
                jatekTer.Add(sorbanLevoElemek);
            }
        }
    }

    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            Jatek jatek = new Jatek();
            foreach(List<Elem> sor in jatek.jatekTer)
            {
                foreach(Elem e in sor)
                {
                    Rectangle rect = new Rectangle();
                    rect.Width = 10;
                    rect.Height = 10;
                    jatekTer.SetValue(Canvas.TopProperty, $"{e.y * 10 +1}.0");
                    jatekTer.Children.Add(rect);
                }
            }
        }
    }
}
