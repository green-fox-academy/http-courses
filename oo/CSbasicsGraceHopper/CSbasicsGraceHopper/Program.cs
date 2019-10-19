using System;
using System.Collections.Generic;

namespace CSbasicsGraceHopper
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello " + "world");

            List<int> numbers = getNumbersUntil(20);
            int max = findMax(numbers);
            Console.WriteLine($"A legnagyobb szam: {max}");

            switchExample("asdasd");
            string alma = "alma";

            int[][] matrix = {
                new int[] { 1, 2, 3 },
                new int[] { 4, 5, 6, 7 }
            };
            Console.WriteLine(matrix[1][2]);

            int[,] matrix2 = {
                { 1, 2, 3 },
                { 4, 5, 6 },
            };
            Console.WriteLine(matrix2[1, 2]);
            
        }

        private static void switchExample(string text)
        {
            switch (text)
            {
                case "alma":
                case "korte":
                    Console.WriteLine("gyumolcs");
                    break;
                case "repa":
                case "karfiol":
                    Console.WriteLine("zoldseg");
                    break;
                default:
                    Console.WriteLine("nem tudni");
                    break;
            }
        }

        private static int findMax2(List<int> numbers)
        {
            // O(nlogn)
            numbers.Sort();
            return numbers[numbers.Count - 1];
        }

        private static int findMax(List<int> numbers)
        {
            int max = 0;

            // O(n)
            foreach (int number in numbers)
            {
                if (number > max)
                {
                    max = number;
                }
            }
            
            return max;
        }

        private static List<int> getNumbersUntil(int limit)
        {
            List<int> numbers = new List<int>();
            int sum = 0;

            do
            {
                Console.Write("Szam: ");
                int number = int.Parse(Console.ReadLine());
                sum += number;
                numbers.Add(number);

                Console.WriteLine();

            } while (sum <= limit);

            return numbers;
        }
    }
}
