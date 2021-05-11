using System;

namespace BasicClasses
{
    class Program
    {
        static void Main(string[] args)
        {
            Forest f = new Forest(55000000);
            f.Name = "Amazon";
            f.Trees = 39000000;
            //f.age = ;
            f.Biome = "Tropical";
            Console.WriteLine($"This forest is called the {f.Name}.");
            Console.WriteLine(f.Biome);
            Console.WriteLine(f.trees);
            Console.WriteLine($"It's {f.age} years old");
            f.Grow();
            Console.WriteLine($"The number of trees increased. New number of trees is {f.Trees}");
            f.Grow();
            Console.WriteLine($"The number of trees increased. New number of trees is {f.Trees}");
            f.Burn();
            Console.WriteLine($"The number of trees decreased. New number of trees is {f.Trees}");

        }
    }
}
