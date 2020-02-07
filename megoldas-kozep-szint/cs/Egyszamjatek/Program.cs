using System;
using System.Collections.Generic;
using System.IO;

namespace Egyszamjatek
{
    class Player
    {
        public string Name { get; set; }
        public List<int> Tips { get; set; }

        public Player()
        {
            Tips = new List<int>();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Player> players = new List<Player>();
            string[] lines = File.ReadAllLines("egyszamjatek1.txt");

            foreach (var line in lines)
            {
                Player player = CreatePlayer(line);

                players.Add(player);
            }

            Console.WriteLine($"3. feladat: Játékosok száma: {players.Count} fő");

            Console.Write("4. feladat: Kérem a forduló sorszámát: ");
            string userInput = Console.ReadLine();

            int gameTurn = int.Parse(userInput);

            int sumOfTips = 0;

            foreach (var player in players)
            {
                int tip = player.Tips[gameTurn - 1];
                sumOfTips += tip;
            }

            double avgOfTips = (double) sumOfTips / players.Count;

            Console.WriteLine($"5. feladat: A megadott feladat tippjeinek átlaga: {avgOfTips:F2}");
        }

        private static Player CreatePlayer(string line)
        {
            Player player = new Player();

            string[] lineParts = line.Split(' ');

            player.Name = lineParts[0];

            for (int i = 1; i < lineParts.Length; i++)
            {
                player.Tips.Add(int.Parse(lineParts[i]));
            }

            return player;
        }
    }
}
