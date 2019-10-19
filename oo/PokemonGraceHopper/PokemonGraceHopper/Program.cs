using System;
using System.Collections.Generic;

namespace PokemonGraceHopper
{
    class Program
    {
        public static void Main(string[] args)
        {
            List<Pokemon> ashPokemonjai = initializePokemons();

            // Minden pokémonnak van neve és típusa.
            // Bizonyos tipusok hatásosak más típusokkal szemben, pl. víz hatásos tűz ellen.

            // Ash-nek van néhány pokémonja.
            // Felbukkant egy vad pokémon!

            Pokemon vadPokemon = new Pokemon("Oddish", "fű", "víz");

            // Melyik pokémonját válassza Ash a küzdelemhez?

            var hatasosPokemon = chosePokemon(ashPokemonjai, vadPokemon);
            if (hatasosPokemon == null)
            {
                Console.WriteLine("O-o :(");
            } else
            {
                Console.WriteLine($"{hatasosPokemon.nev}, téged választalak!");
            }
        }

        private static Pokemon chosePokemon(List<Pokemon> pokemons, Pokemon vadPokemon)
        {
            foreach (Pokemon pokemon in pokemons)
            {
                if (pokemon.hatasosEllene(vadPokemon))
                {
                    return pokemon;
                }
            }
            return null;
        }

        private static List<Pokemon> initializePokemons()
        {
            List<Pokemon> pokemon = new List<Pokemon>();

            pokemon.Add(new Pokemon("Balbasaur", "fű", "víz"));
            pokemon.Add(new Pokemon("Pikatchu", "elektromos", "víz"));
            pokemon.Add(new Pokemon("Masik Charizard", "tűz", "fű"));
            pokemon.Add(new Pokemon("Charizard", "tűz", "fű"));
            pokemon.Add(new Pokemon("Balbasaur", "víz", "tűz"));
            pokemon.Add(new Pokemon("Kingler", "víz", "tűz"));

            return pokemon;
        }
    }
}
