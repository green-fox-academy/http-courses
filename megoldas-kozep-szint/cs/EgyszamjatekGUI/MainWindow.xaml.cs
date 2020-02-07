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
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private List<Player> players;

        public MainWindow()
        {
            InitializeComponent();

            FileReader reader = new FileReader();

            players = reader.ReadAllPlayers();
        }

        private void txtTips_TextChanged(object sender, TextChangedEventArgs e)
        {
            int[] tips = ParseTips();

            lblNumerOfTips.Content = $"{tips.Length} db";
        }

        private int[] ParseTips()
        {
            string[] parts = txtTips.Text.Split(' ', StringSplitOptions.RemoveEmptyEntries);

            int[] tips = new int[parts.Length];

            for (int i = 0; i < parts.Length; i++)
            {
                tips[i] = int.Parse(parts[i]);
            }

            return tips;
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string name = txtName.Text;

            foreach (var player in players)
            {
                if (player.Name == name)
                {
                    MessageBox.Show("Van már ilyen nevű játékos!");
                    return;
                }
            }

            int[] tips = ParseTips();

            if (players[0].Tips.Count != tips.Length)
            {
                MessageBox.Show("A tippek száma nem megfelelő!");
                return;
            }

            SavePlayerToFile(new Player
            {
                Name = txtName.Text,
                Tips = new List<int>(tips)
            });
        }

        private void SavePlayerToFile(Player player)
        {
            string tipsWithSpaces = string.Join(' ', player.Tips);
            File.AppendAllText("egyszamjatek2.txt", $"{player.Name} {tipsWithSpaces}" + Environment.NewLine);
            MessageBox.Show("Az állomány bővítése sikeres volt!");

            txtName.Text = "";
            txtTips.Text = "";
        }
    }
}
