using System;

namespace CSbasicsGraceHopper
{
    class Program
    {
        static void Main(string[] args)
        {
            int sum = 0;
            int max = 0;

            do
            {
                Console.Write("Szam: ");
                int number = int.Parse(Console.ReadLine());
                sum += number;

                if (number > max)
                {
                    max = number;
                }

                Console.WriteLine();

            } while (sum <= 20);

            Console.WriteLine($"A legnagyobb szam: {max}");
        }
    }
}
