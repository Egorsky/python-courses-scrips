using System;

namespace JumpStatements
{
    class Program
    {
        static void Main(string[] args)
        {
            bool buttonClick = true;
            int i = 0;
            do
            {
                Console.WriteLine("BLARRRRR");
                i++;
                if (i == 3)
                {
                    break;
                }
            } while (!buttonClick);
        }
    }
}
