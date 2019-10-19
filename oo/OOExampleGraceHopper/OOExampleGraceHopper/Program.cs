using System;
using System.Collections.Generic;

namespace OOExampleGraceHopper
{
    class Program
    {
        static void Main(string[] args)
        {
            Student jozsi = new Student();
            jozsi.Name = "Jozsi";
            jozsi.Age = 10;

            Student pisti = new Student();
            pisti.Name = "Pisti";
            pisti.Age = 9;

            Teacher gizi = new Teacher();
            gizi.Name = "Gizi";
            gizi.Age = 30;

            var persons = new List<Person>();
            persons.Add(jozsi);
            persons.Add(pisti);
            persons.Add(gizi);

            foreach (Person p in persons)
            {
                Console.WriteLine(p.Name);
            }
        }
    }
}
