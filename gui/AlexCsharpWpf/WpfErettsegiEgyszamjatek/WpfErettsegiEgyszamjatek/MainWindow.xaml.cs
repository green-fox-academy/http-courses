using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfErettsegiEgyszamjatek
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    /// 

    public partial class MainWindow : Window
    {
        public List<Jatekos> Jatekosok { get; set; }
        public string Utvonal { get; set; }
        public MainWindow()
        {
            Utvonal = "egyszamjatek.txt";
            Jatekosok = new List<Jatekos>();
            JatekosokBeolvasasa();
            InitializeComponent();
        }

        private void Btn_Hozzaad_Click(object sender, RoutedEventArgs e)
        {
            var nev = tbx_Nev.Text;
            var tippek = tbx_Tippek.Text;
            var tordeltTippek = tippek.Split();

            if (!HibaKezeles(nev, tordeltTippek))
            {
                using (StreamWriter writer = new StreamWriter(Utvonal, true))
                {
                    writer.WriteLine(nev + " " + tippek);
                }
                JatekosokBeolvasasa();
            }
        }


        private void JatekosokBeolvasasa()
        {
            var sorok = File.ReadAllLines(Utvonal);
            foreach (var sor in sorok)
            {
                var tortAdat = sor.Split(' ');
                var nev = tortAdat[0];
                var tippek = TippFormazas(tortAdat);

                Jatekosok.Add(new Jatekos()
                {
                    Nev = nev,
                    Tippek = tippek
                });
            }
        }

        private List<int> TippFormazas(string[] tomb)
        {
            List<int> formazottLista = new List<int>();
            var num = 0;
            for (int i = 1; i < tomb.Length; i++)
            {
                //megváltozott
                if (int.TryParse(tomb[i], out num))
                {
                    formazottLista.Add(num);
                }
            }
            return formazottLista;
        }

        private bool HibaKezeles(string nev, string[] tippek)
        {
            //return Jatekosok.Exists(x => x.Nev == nev);

            if (VanEIlyenNevuJatekos(nev))
            {
                MessageBox.Show("Van már ilyen nevű játékos!", "Hiba!");
                return true;
            }
            else if (tippek.Length != Jatekosok[0].Tippek.Count)
            {
                MessageBox.Show("Nem megfelelő a tippek száma!", "Hiba!");
                return true;
            }
            MessageBox.Show("Az állomány bővítése sikeres volt!", "Siker!");
            return false;
        }

        private bool VanEIlyenNevuJatekos(string nev)
        {
            foreach (var jatekos in Jatekosok)
            {
                if (jatekos.Nev == nev)
                {
                    return true;
                }
            }
            return false;
        }


        private void Tbx_Tippek_TextChanged(object sender, TextChangedEventArgs e)
        {
            var tippek = tbx_Tippek.Text.Trim();
            //lb_Fordulo.Content = tippek == "" ? "0 db" : tippek.Split(' ').Length + " db";

            if (tippek == "")
            {
                lb_Fordulo.Content = "0 db";
            }
            else
            {
                var tomb = tippek.Split(' ');
                lb_Fordulo.Content = tomb.Length + " db";
            }
        }
    }
}
