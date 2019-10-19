using System;
using System.Collections.Generic;

namespace CSbasicsGraceHopper
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = getNumbersUntil(20);
            int max = findMax2(numbers);

            Console.WriteLine($"A legnagyobb szam: {max}");
        }

        private static int findMax2(List<int> numbers)
        {
            numbers.Sort();
            return numbers[numbers.Count - 1];
        }

        private static int findMax(List<int> numbers)
        {
            int max = 0;

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
