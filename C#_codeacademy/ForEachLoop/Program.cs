using System;

namespace ForEachLoop
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] todo = { "respond to email", "make wireframe", "program feature", "fix bugs" };
            foreach (string task in todo)
            {
                CreateTodoItem(task);
            }

        }

        static void CreateTodoItem(string item)
        {
            Console.WriteLine($"[] {item}");
        }
    }
}