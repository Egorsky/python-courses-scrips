using System;

namespace ReplaceMethod
{
    class Program
    {
        static void Main(string[] args)
        {
            string lyrics =
              "Dollie, Dollie, bo-bollie,\n" +
              "Banana-fana fo-follie\n" +
              "Fee-fi-mo-mollie\n" +
              "Dollie!";

           
            string newLyrics = lyrics.Replace("ollie", "ana");

            Console.WriteLine(newLyrics);
            Console.WriteLine();
            Console.WriteLine(lyrics);
        }
    }
}
