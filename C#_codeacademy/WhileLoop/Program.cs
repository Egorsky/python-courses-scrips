using System;

namespace WhileLoop
{
    class Program
    {
        static void Main(string[] args)
        {
            int emails = 20;
            while (emails > 1)
            {
                emails = emails - 1;
                Console.WriteLine($"Emails are deleting. {emails} left.");

            }
            Console.WriteLine("INBOX ZERO ACHIEVED!");
        }
    }
}
