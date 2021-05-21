using System;

namespace IsNullOrEmptyTyped
{
    class Program
    {
        static void Main(string[] args)
        {
            string a = Console.ReadLine();
            Console.WriteLine(a);
            if (String.IsNullOrEmpty(a))
            {
                Console.WriteLine("You didn't enter anything!");
            }
            else
            {
                Console.WriteLine("Thank you for your submission!");
            }

        }
    }
}
