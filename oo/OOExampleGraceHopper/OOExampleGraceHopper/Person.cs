using System;
namespace OOExampleGraceHopper
{
    public class Person
    {
        public static int IDGenerator = 1;

        public int Id;
        public string Name;
        public int Age;

        public Person(string name, int age)
        {
            Id = IDGenerator++;
            Name = name;
            Age = age;
        }

        public virtual void Welcome()
        {
            Console.WriteLine($"Hello, {Name} vagyok, szemely");
        }

        public override string ToString()
        {
            return $"Id: {Id}, name: {Name}, age: {Age}";
        }
    }
}
