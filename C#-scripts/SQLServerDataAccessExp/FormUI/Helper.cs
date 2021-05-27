using System;
using System.Collections.Generic;
using System.Text;
using System.Configuration;


namespace FormUI
{
    public static class Helper
    {
        public static string CnnVal(string name)
        {
            return ConfigurationManager.ConnectionStrings[name].ConnectionString;
        }
    }
}
