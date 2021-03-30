using System;

namespace NameGrab
{
    class Program
    {
        static void Main(string[] args)
        {
            // User Name
            string name = "Farhad Hesam Abbasi";

            // Get first letter
            int letterPos = name.IndexOf("F");
            char firstLetter = name[letterPos];



            // Get last name
            int lastNCh = name.IndexOf("Abbasi");
            string lastName = name.Substring(lastNCh);


            // Print results
            Console.WriteLine(firstLetter);
            Console.WriteLine(lastName);


        }
    }
}