using System;

namespace OverridingObjectMembers
{
    class Program
    {
        static void Main(string[] args)
        {
            Book bk = new Book("Ta-Nehisi Coates", "Between the World and Me");
            Console.WriteLine(bk.ToString());

        }
    }
}
