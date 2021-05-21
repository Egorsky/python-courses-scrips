using System;

namespace stringInterpolation
{
    class Program
    {
        // Declare the variables
        string beginning = "Once upon a time,";
        string middle = "The kid climbed a tree";
        string end = "Everyone lived happily ever after.";

        // Interpolate the string and the variables
        string story = $"{beginning} {middle} {end}";
        Console.WriteLine(story);


      // Print the story to the console 

    }
}
