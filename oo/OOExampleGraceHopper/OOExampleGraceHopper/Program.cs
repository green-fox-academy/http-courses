using System;
using System.Collections.Generic;

namespace OOExampleGraceHopper
{
    class Program
    {
        static void Main(string[] args)
        {
            Student jozsi = new Student("Jozsi", 10);

            Student jolan = new Student("Jolan", 16);

            Student pisti = new Student("Pisti", 9);

            Teacher gizi = new Teacher();
            Teacher agi = new Teacher("Agi", 42);
            Teacher eszter = new Teacher("Eszter");
            //gizi.Name = "Gizi";
            //gizi.Age = 30;

            var persons = new List<Person>();
            persons.Add(jozsi);
            persons.Add(jolan);
            persons.Add(pisti);
            persons.Add(gizi);

            foreach (Person p in persons)
            {
                Console.WriteLine(p);
            }

            Console.WriteLine(Person.IDGenerator);

            ClassRoom graceHopper = new ClassRoom();
            graceHopper.AddTeacher(gizi);
            graceHopper.AddStudent(pisti);
            graceHopper.AddStudent(jozsi);

            graceHopper.Welcome();
            foreach (var person in graceHopper.Persons)
            {
                Console.WriteLine(person);
            }

        }
    }
}
