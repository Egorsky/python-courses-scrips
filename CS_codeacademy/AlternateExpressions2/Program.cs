using System;

namespace AlternateExpressions2
{
    class Program
    {
        // Method to be used as second argument
        public static bool IsLong(string word)
        {
            return word.Length > 8;
        }

        static void Main(string[] args)
        {
            string[] adjectives = { "rocky", "mountainous", "cosmic", "extraterrestrial" };

            string firstLongAdjective = Array.Find(adjectives, IsLong);

            Console.WriteLine($"The first long word is: {firstLongAdjective}.");
        }
    }
}
