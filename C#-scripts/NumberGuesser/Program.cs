using System;

namespace NumberGuesser
{
    class Program
    {
        static void Main(string[] args)
        {
            GetAppIfo();

            // Input username

            GreetUser();


            while (true)
            {
            
            //Init correct number
            
            Random random = new Random();

            int correctNumber = random.Next(1, 10);

            //Init guess var
            int guess = 0;

            Console.WriteLine("Guess a number between 1 and 10");

          
            while (guess != correctNumber)
            {
                string input = Console.ReadLine();

                // Ceck if it's a number

            if (!int.TryParse(input, out guess))
                {
                    PrintColorMessage(ConsoleColor.Red, "Please use an actual number");

                    continue;
                }

                    guess = Int32.Parse(input);

                if (guess != correctNumber)
                {
                        //Print error message
                        PrintColorMessage(ConsoleColor.Red, "Wrong number, try again");    
                }
            }

                //Output success message
                PrintColorMessage(ConsoleColor.Yellow, "You are correct!");

                //Ask to play again

                Console.WriteLine("Play again? [Y/ N]");

                string answer = Console.ReadLine().ToUpper();

                if (answer == "Y")
                {
                    continue;
                }
                else if (answer == "N")
                {
                    return;
                }
                else
                {
                    return;
                }
            }
        }

        static void GetAppIfo()
        {
            string appName = "Number Guesser";
            string appVersion = "1.0.0";
            string appAuthor = "Egor Kolpakov";

            // Change text color
            Console.ForegroundColor = ConsoleColor.Green;

            // Write out app info with color
            Console.WriteLine("{0}: Version {1}, by {2}", appName, appVersion, appAuthor);

            Console.ResetColor();
        }

        //Get and display user's name
        static void GreetUser()
        {
            Console.WriteLine("What is your name?");

            string inputName = Console.ReadLine();


            Console.WriteLine("Hello {0}, let's play a game...", inputName);
        }

        //Print color message
        static void PrintColorMessage(ConsoleColor color, string message)
        {
            Console.ForegroundColor = color;

            // Write out app info with color
            Console.WriteLine(message);

            Console.ResetColor();
        }
    }
}
