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

namespace EgyszamjatekGUI
{
    struct Jatekos
    {
        public string nev;
        public List<Int32> tippek;
    }
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        List<Jatekos> jatekosok = new List<Jatekos>();

        public MainWindow()
        {
            InitializeComponent();
            

        }


        public void JatekosOlvasas()
        {
            StreamReader fajlOlvaso = new StreamReader("egyszamjatek2.txt");
            jatekosok.Clear();
            while (!fajlOlvaso.EndOfStream)
            {
                string jelenlegiSor = fajlOlvaso.ReadLine();
                string[] sorbeliElemek = jelenlegiSor.Split(' ');
                Jatekos jelenlegiSorbolKifejtett = new Jatekos();
                jelenlegiSorbolKifejtett.nev = sorbeliElemek[0];
                jelenlegiSorbolKifejtett.tippek = new List<int>();
                for (int i = 1; i < sorbeliElemek.Length; i++)
                {
                    jelenlegiSorbolKifejtett.tippek.Add(int.Parse(sorbeliElemek[i]));
                }
                jatekosok.Add(jelenlegiSorbolKifejtett);
            }
            fajlOlvaso.Close();
        }

        private void tippBevitel_KeyUp(object sender, KeyEventArgs e)
        {
            string levagott = tippBevitel.Text.Trim();
            int szamossag = levagott.Split(' ').Length;
            if(levagott.Equals(String.Empty))
            {
                szamossag = 0;
            }
            szamossagJelzo.Content = $"{szamossag} db";
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string jatekosNev = jatekosNevInput.Text;
            JatekosOlvasas();
            bool marLetezik = false;
            int tippekSzama = jatekosok[0].tippek.Count;

            foreach(Jatekos jatekos in jatekosok)
            {
                if(jatekos.nev.Equals(jatekosNev))
                {
                    marLetezik = true;
                }
            }
            if(marLetezik)
            {
                MessageBox.Show("Van mar ilzen nevu jatekos", "UPSZI");
            }
            string levagott = tippBevitel.Text.Trim();
            int szamossag = levagott.Split(' ').Length;
            bool mentheto = !marLetezik && (szamossag == tippekSzama);
            if (mentheto)
            {
                FileStream jatekosHozzaAdo = new FileStream("egyszamjatek2.txt", FileMode.Append);
                StreamWriter sw = new StreamWriter(jatekosHozzaAdo);
                string ujJatekos = $"{jatekosNev} {levagott}";
                sw.WriteLine(ujJatekos);
                MessageBox.Show("sikeres hozzaadas ", "UPSZI");
                sw.Close();
                jatekosHozzaAdo.Close();
            }
        }
    }
}
