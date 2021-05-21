using System;
using System.Collections.Generic;
using System.Linq;

namespace WhereSelectTypes
{
    class Program
    {
        static void Main()
        {
            string[] heroes = { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };
            var hrwc = heroes.Where(h => h.Contains("c"));
            var lowerHeroesWithC = hrwc.Select(h => h.ToLower());

            var sameResult = heroes
            .Where(h => h.Contains("c"))
            .Select(h => h.ToLower());

            foreach (string s in sameResult)
            {
                Console.WriteLine(s);
            }
        }
    }
}
