using Microsoft.Win32;
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

namespace WpfDemoApp
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
        
            InitializeComponent();
        }

        private void Btn_Valtoztatas_Click(object sender, RoutedEventArgs e)
        {
            var feladatNev = tbx_FeladatNev.Text;
            lbx_Feladatok.Items.Add(feladatNev);
            tbx_FeladatNev.Clear();
        }

     
        private void Tbx_FeladatNev_KeyDown(object sender, KeyEventArgs e)
        {
            if(e.Key == Key.Enter)
            {
                Btn_Valtoztatas_Click(sender, e);
            }
        }

        private void Btn_Torles_Click(object sender, RoutedEventArgs e)
        {
       
            var index = lbx_Feladatok.SelectedIndex;
            if(index == -1)
            {
                MessageBox.Show("Kérem válassza ki a törlendő elemet!","Hiba!");
            }
            else
            {
                lbx_Feladatok.Items.RemoveAt(index);
                MessageBox.Show("Sikeres törlés", "Siker!");
            }
           
        }

        private void Btn_Mentes_Click(object sender, RoutedEventArgs e)
        {
            SaveFileDialog mentesDialogus = new SaveFileDialog();

            if(mentesDialogus.ShowDialog() == true)
            {
                try
                {
                    using (StreamWriter writer = new StreamWriter(mentesDialogus.FileName))
                    {
                        foreach (var feladat in lbx_Feladatok.Items)
                        {
                            writer.WriteLine(feladat);
                        }
                    }
                }catch(IOException ex)
                {
                    MessageBox.Show(ex.Message, "Hiba");
                    return;
                }
                MessageBox.Show("Sikeres mentés!", "Siker!");
            }

        }
    }
}
