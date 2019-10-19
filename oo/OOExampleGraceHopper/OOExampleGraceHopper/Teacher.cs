using System;
namespace OOExampleGraceHopper
{
    public class Teacher : Person
    {
        public Teacher() : base("teacher", 40) {}

        public Teacher(string name, int age) : base(name, age) {}

        public Teacher(string name) : base(name, 40) {}

        public override void Welcome()
        {
            Console.WriteLine($"Hello, {Name} vagyok, tanar");
        }
    }
}
