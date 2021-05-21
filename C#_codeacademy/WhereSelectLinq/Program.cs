using System;
using System.Collections.Generic;
using System.Linq;

namespace WhereSelectLinq
{
    class Program
    {
        static void Main()
        {
            string[] heroes = { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };
            var heroesWithI = from hr in heroes
                              where hr.Contains("i")
                              select hr;

            var underscored = from hu in heroes
                              select hu.Replace(" ", "_");

            foreach (string s in heroesWithI)
            {
                Console.WriteLine(s);
            }

            Console.WriteLine("\nPrinting underscored: \n");

            foreach (string s in underscored)
            {
                Console.WriteLine(s);
            }
        }
    }
}
