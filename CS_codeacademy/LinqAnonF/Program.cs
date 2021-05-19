using System;
using System.Collections.Generic;
using System.Linq;

namespace LinqAnonF
{
    class Program
    {
        static void Main()
        {
            string[] heroes = { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };

            var heroesWithI = heroes.Where(h => h.Contains("i"));

            foreach (string s in heroesWithI)
            {
                Console.WriteLine(s);
            }
        }
    }
}