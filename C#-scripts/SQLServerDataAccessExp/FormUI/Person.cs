using System;
using System.Collections.Generic;
using System.Text;

namespace FormUI
{
    public class Person
    {
        public int id { get; set; }

        public string first_name { get; set; }

        public string last_name { get; set; }

        public string email { get; set; }

        public string gender { get; set; }

        public string ip_address { get; set; }

        public string city { get; set; }

        public string FullInfo
        {
            get {
                //format of return entry
                return $"{ first_name } {last_name }, | ({ email }) | { city }";
                }
        }
    }
}
