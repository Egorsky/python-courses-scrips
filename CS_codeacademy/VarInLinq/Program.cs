using System;
using System.Collections.Generic;
using System.Linq;


namespace VarInLinq
{
    class Program
    {
        static void Main()
        {
            List<string> heroes = new List<string> { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };

            var shortHeroes = from h in heroes
                              where h.Length < 8
                              select h;
            foreach (string n in shortHeroes)
            {
                Console.WriteLine(n);
            }
            var longHeroes = heroes.Where(n => n.Length > 8);
            Console.WriteLine(longHeroes.Count());
        }
    }
}