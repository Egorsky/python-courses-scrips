using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace TheObjectClass
{
    class Book
    {
        public int bPage
        { get; }

        public string title
        { get; protected set; }
    }
}