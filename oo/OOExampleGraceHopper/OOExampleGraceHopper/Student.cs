using System;
namespace OOExampleGraceHopper
{
    public class Student : Person
    {
        
        public Student(string name, int age) : base(name, age)
        {
            
        }

        public override void Welcome()
        {
            Console.WriteLine($"Hello, {Name} vagyok, diak");
        }
    }
}
