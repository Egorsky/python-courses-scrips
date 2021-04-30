using System;

namespace Return
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(DecoratePlanet(planet: "Mars"));
        }

        static string DecoratePlanet(string planet)
        {
            return $"*..*..* Welcome to {planet} *..*..*";
        }
    }
}
