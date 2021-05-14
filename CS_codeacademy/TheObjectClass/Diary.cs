using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace TheObjectClass
{
    class Diary
    {
        public int bPage
        { get; }

        public string title
        { get; protected set; }

        public Diary(int bPage)
        {
            //Console.WriteLine(bPage);
        }
    }
}