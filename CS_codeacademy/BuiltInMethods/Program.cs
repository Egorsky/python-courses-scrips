using System;

namespace BuiltInMethods
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] summerStrut;

            summerStrut = new string[] { "Juice", "Missing U", "Raspberry Beret", "New York Groove", "Make Me Feel", "Rebel Rebel", "Despacito", "Los Angeles" };

            int[] ratings = { 5, 4, 4, 3, 3, 5, 5, 4 };

            int ratInd = Array.IndexOf(ratings, 3);
            Console.WriteLine($"Song number {ratInd + 1} is rated three stars");
            string longSong = Array.Find(summerStrut, x => x.Length > 10);
            Console.WriteLine($"The first song that has more than 10 charecters in the title is {longSong}");

            Array.Sort(summerStrut);
            Console.WriteLine($"The first song in alphabetic order is {summerStrut[0]} and the last song is {summerStrut[summerStrut.Length - 1]}");


        }
    }
}