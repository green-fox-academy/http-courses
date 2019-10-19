using System;
namespace PokemonGraceHopper
{
    public class Pokemon
    {
        public string nev;
        string tipus;
        string ellenfel;

        public Pokemon(string nev, string tipus, string ellenfel)
        {
            this.nev = nev;
            this.tipus = tipus;
            this.ellenfel = ellenfel;
        }

        public bool hatasosEllene(Pokemon masik)
        {
            return this.ellenfel.Equals(masik.tipus);
        }

    }
}
