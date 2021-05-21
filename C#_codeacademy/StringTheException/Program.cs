using System;

namespace StringTheException
{
    class Program
    {
        static void Main(string[] args)
        {
            string a = "immutable";
            string b = "immutable";
            Console.WriteLine(a == b);
            Object c = new Object();
            Object d = new Object();
            Console.WriteLine(c == d);
        }
    }
}
