using System;
using System.Collections.Generic;
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

namespace Proba
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private int szamlal = 0;
        public MainWindow()
        {
            InitializeComponent();
            for (int i = 1; i < 100000; i *= 10)
            {
                Button adjEnnyit = new Button();
                adjEnnyit.Content = i;
                adjEnnyit.Click += DinamikusHozzaAdas;
                panel.Children.Add(adjEnnyit);
            }

        }

        private void DinamikusHozzaAdas(object sender, RoutedEventArgs e)
        {
            if(sender is Button)
            {
                Button forras = (Button)sender;
                try
                {
                    szamlal += (int)forras.Content;
                    szamlalo.Content = szamlal;

                }
                catch (FormatException)
                {

                }
            }
            
        }

        private void gomb_Click(object sender, RoutedEventArgs e)
        {
            szamlal++;
            szamlalo.Content = szamlal;
        }

        private void gomb_1_Click(object sender, RoutedEventArgs e)
        {
            if(szamlal > 0)
            {
                szamlal--;
                szamlalo.Content = szamlal;
            }
        }
    }
}
