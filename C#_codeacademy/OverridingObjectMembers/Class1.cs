using System;


namespace OverridingObjectMembers
{
    class Book
    {
        public string Author
        { get; private set; }

        public string Title
        { get; private set; }

        public Book(string author = "Unknown", string title = "Untitled")
        {
            Author = author;
            Title = title;
        }

        public virtual string Stringify()
        {
            return "This is a Book object!";
        }
        public override string ToString()
        {
            return $"The author of this book is {Author}. Title is: {Title}";
        }
    }
}