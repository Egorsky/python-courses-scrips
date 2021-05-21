using System;

namespace UsingOut
{
    class Program
    {
        static void Main(string[] args)
        {
            string statement = "GARRRR";
            string calling = Whisper(statement, out bool marker);
            Console.WriteLine(calling);
        }
        static string Whisper(string statement, out bool wasWhisperCalled)
        {
            wasWhisperCalled = true;
            return statement.ToLower();
        }
    }
}