using System;
using System.Collections.Generic;
using System.Text;

namespace BasicClasses
{
    class Forest
    {
        // Fields

        public string name;
        public int trees;
        public int age;
        private string biome;

        // Properties 


        public string Name
        {
            get { return name; }
            set { name = value; }
        }
        public int Trees
        {
            get { return trees; }

            set { trees = value; }
        }
        public string Biome
        {
            get { return biome; }
            set
            {
                if (value == "Tropical" ||
                value == "Temperate" ||
                value == "Boreal")
                {
                    biome = value;
                }
                else
                {
                    biome = "Unknown";
                }

            }
        }
        public int Age
        {
            get { return age; }
            private set { age = value; }
        }
        public int Grow()
        {
            Trees += 30;
            Age++;
            return Trees;
        }
        public int Burn()
        {
            Trees -= 20;
            Age++;
            return Trees;
        }
        public Forest(int age)
        {
            this.Age = age;
            ForestsCreated ++;
        }
        private static int forestsCreated;
        public static int ForestsCreated
        {
            get { return forestsCreated; }
            private set { forestsCreated = value; }
        }

    }
}
