using System;

namespace StringCheck
{
    class Program
    {
        static void Main(string[] args)
        {

            string anyStr = "sdfsdfk111";
            int anInd = anyStr.Length;

            Console.WriteLine(anInd);

            string poem = "just like in a dream";
            int whInd = poem.IndexOf("d");
            Console.WriteLine(whInd);
            Console.WriteLine(poem.Substring(whInd));
            Console.WriteLine(poem.Substring(whInd).ToUpper());


        }
    }
}
