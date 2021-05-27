using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace FormUI
{
    public partial class Dashboard : Form
    {
        List<Person> peopleFn = new List<Person>();

        public Dashboard()
        {
            InitializeComponent();

            UpdateBinding();
        }

        private void UpdateBinding()
        {
            peopleFoundListbox.DataSource = peopleFn;
            peopleFoundListbox.DisplayMember = "FullInfo";
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void searchButton_Click(object sender, EventArgs e)
        {
            DataAccess db = new DataAccess();

            peopleFn = db.GetHuman(firstNameText.Text, lastNameText.Text);

            if (peopleFn.Count() == 0)
                {
                DialogResult dr = MessageBox.Show("No search results found", "Confirm",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
                if (dr == DialogResult.OK)
                    {
                    }
                }

            peopleFoundListbox.Refresh();

            UpdateBinding();


        }

        private void peopleFoundListbox_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void closeButton_Click(object sender, EventArgs e)
        {
            DialogResult dr = MessageBox.Show("Do you want to close search bar?", "Confirm",
               MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (dr == DialogResult.Yes)
            {
                this.Close();
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged_1(object sender, EventArgs e)
        {

        }
    }
}
