using System;

namespace ComparingLoops
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] websites = { "twitter", "facebook", "gmail" };


            foreach (string site in websites)
            {
                Console.WriteLine(site);
            }
        }
    }
}
