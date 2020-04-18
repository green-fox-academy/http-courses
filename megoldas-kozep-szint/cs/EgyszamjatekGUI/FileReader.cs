using System.Collections.Generic;
using System.IO;

namespace EgyszamjatekGUI
{
    class FileReader
    {
        public List<Player> ReadAllPlayers()
        {
            List<Player> players = new List<Player>();
            string[] lines = File.ReadAllLines("egyszamjatek2.txt");

            foreach (var line in lines)
            {
                Player player = CreatePlayer(line);

                players.Add(player);
            }

            return players;
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
