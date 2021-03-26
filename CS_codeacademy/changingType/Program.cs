using System;

namespace changingType
{
    class Program
    {
        static void Main(string[] args)

        { 
            // boolean into string
            bool boolOp = true;
            string boolToStr = boolOp.ToString();
            Console.WriteLine("this returns {0}", boolToStr);

            // integer into string
            int number = 654;
            string numToStr = number.ToString();
            Console.WriteLine("this {0} is now a string", numToStr);

            // integer into double

            int someNum = 254;
            double someDub = someNum;
            Console.WriteLine("this number {0} is a double now", someDub);

        }
    }
}