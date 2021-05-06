using System;

namespace DocumentationHunt
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] summerStrut;

            summerStrut = new string[] { "Juice", "Missing U", "Raspberry Beret", "New York Groove", "Make Me Feel", "Rebel Rebel", "Despacito", "Los Angeles" };

            int[] ratings = { 5, 4, 4, 3, 3, 5, 5, 4 };

            string[] summerStrutCopy = new string[8];
            Array.Copy(summerStrut, summerStrutCopy, 8);
            Console.WriteLine(summerStrutCopy[0]);

            Array.Reverse(summerStrut);
            Console.WriteLine($"The frist song on the list is {summerStrut[0]}, and the last one is {summerStrut[summerStrut.Length - 1]}");

            //Clearing ratings
            Array.Clear(ratings, 0, 7);
            Console.WriteLine(ratings[0]);
        }
    }
}
