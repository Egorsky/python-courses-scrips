using System;

namespace LearnInheritance
{
    class Program
    {
        static void Main(string[] args)
        {

            Bicycle b = new Bicycle(10);

            Console.WriteLine(b.Describe());

        }
    }
}