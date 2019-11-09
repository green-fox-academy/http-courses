using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Egyszamjatek
{
    struct Jatekos
    {
        public string nev;
        public List<Int32> tippek;
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Jatekos> jatekosok = new List<Jatekos>();
            StreamReader fajlOlvaso = new StreamReader("egyszamjatek1.txt");
            while(!fajlOlvaso.EndOfStream)
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
            
            Console.WriteLine($"3. feladat: Játékosok  száma: {jatekosok.Count}");

            Console.WriteLine("Adjon meg egz szamot a fordulonak vagz ilyesmi");
            int fordulo = int.Parse(Console.ReadLine());

            int tippekOsszegeEbbenAForduloban = 0;
            foreach(Jatekos jatekos in jatekosok)
            {
                tippekOsszegeEbbenAForduloban += jatekos.tippek[fordulo-1];
            }
            double atlag = (double) tippekOsszegeEbbenAForduloban / jatekosok.Count;


            Console.WriteLine("5. feladat: Tippek atlaga  száma: {0:0.00}", atlag);

            fajlOlvaso.Close();
            Console.ReadKey();
        }
    }
}
