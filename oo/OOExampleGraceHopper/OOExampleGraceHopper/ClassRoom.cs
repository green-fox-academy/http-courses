using System;
using System.Collections.Generic;

namespace OOExampleGraceHopper
{
    public class ClassRoom
    {

        public Teacher Teacher;
        public List<Student> Students = new List<Student>();
        public List<Person> Persons = new List<Person>();

        public ClassRoom()
        {
            //students = new List<Student>();
        }

        public void AddTeacher(Teacher teacher)
        {
            Teacher = teacher;
            Persons.Add(teacher);
        }

        public void AddStudent(Student student)
        {
            Students.Add(student);
            Persons.Add(student);
        }

        public void Welcome()
        {
            foreach (var person in Persons)
            {
                person.Welcome();
            }
        }

    }
}
