using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Text;
using Dapper;
using System.Data;

namespace FormUI
{
    public class DataAccess
    {
        public List<Person> GetHuman(string first_name, string last_name)
        {
            using (IDbConnection connection = new System.Data.SqlClient.SqlConnection(Helper.CnnVal("TestDatabase")))
            {
                var output = connection.Query<Person>($"select * from [TestDatabase].[dbo].[TestBase] " +
                    $"where (first_name = '{ first_name }' and last_name = '{ last_name }') " +
                    $"or (last_name = '{ last_name }' or first_name = NULL) " +
                    $"or (first_name = '{ first_name }' or last_name = NULL)").ToList();
                return output;
            }

        }
    }
}
