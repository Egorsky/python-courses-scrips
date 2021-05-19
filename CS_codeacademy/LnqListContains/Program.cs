using System;
using System.Collections.Generic;
using System.Linq;

namespace LnqListContains
{
    class Program
    {
        static void Main()
        {
            List<string> heroesList = new List<string> { "D. Va", "Lucio", "Mercy", "Soldier 76", "Pharah", "Reinhardt" };

            var heronames = heroesList
            .Where(h => h.Contains(".") || h.Contains("7"))
            .Select(h => h);

            foreach (var s in heronames)
            {
                Console.WriteLine(s);
            }
        }
    }
}
