using System;

namespace MethodOverloading
{
    class Program
    {
        static void Main(string[] args)
        {
            NamePets("Laika", "Albert");
            NamePets("Mango", "Puddy", "Bucket");
            NamePets();
        }
        static void NamePets(string pet1, string pet2)
        {
            Console.WriteLine($"Your pets {pet1} and {pet2} will be joining your voyage across space!");
        }
        static void NamePets(string pet3, string pet4, string pet5)
        {
            Console.WriteLine($"Your pets {pet3}, {pet4}, and {pet5} will be joining your voyage across space!");
        }
        static void NamePets()
        {
            Console.WriteLine("Aw, you have no spacefaring pets :(");
        }
    }
}