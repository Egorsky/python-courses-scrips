using System;
using System.Collections.Generic;

namespace ListInitialization
{
    class Program
    {
        static void Main()
        {
            List<double> marathons = new List<double> 
            { 
                144.07,
                143.12,
                146.73,
                146.33
            };

            // Do not delete the code below
            double time = Math.Min(marathons[0], marathons[1]);
            int i = 1;

            Console.WriteLine($"The 2012 marathon was ran in {time} minutes!");

            //Adding a new participant
            Console.WriteLine("\nPrinting maraton data...");
            Console.WriteLine($"The number of participants is {marathons.Count}");
            marathons.Add(143.23);
            Console.WriteLine(marathons.Contains(143.23));
            Console.WriteLine($"New number of participants is {marathons.Count}");

            //Getting top 3 participants
            List<double> topMarathons = marathons.GetRange(0, 3);
            Console.WriteLine("\nPrinting runner results...");
            foreach (double n in topMarathons)
            {

                Console.WriteLine($"Result {i} is {n}");
                i ++;
            }

            //Removing participant
            Console.WriteLine(marathons[1]);
            bool removed = marathons.Remove(143.12);
            Console.WriteLine(marathons[1]);
            Console.WriteLine(removed);

            //Removing all values from the list
            Console.WriteLine();
            marathons.Clear();
            Console.WriteLine(marathons.Count);

            
        }
    }
}
