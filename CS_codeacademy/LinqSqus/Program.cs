using System;
using System.Collections.Generic;
using System.Linq;

namespace LinqSqus
{
    class Program
    {
        static void Main()
        {
            string[] heroes = { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };

            var introduct = heroes
            .Select(h => $"Introducing...[{h.ToUpper()}]!");

            var indx = from h in heroes
                       where h.Contains(" ")
                       select h.IndexOf(" ");

            Console.WriteLine("\nresult 1:");
            foreach (var s in introduct)
            {
                Console.WriteLine(s);
            }
            Console.WriteLine("\nresult 2:");
            foreach (var s in indx)
            {
                Console.WriteLine(s);
            }
        }
    }
}