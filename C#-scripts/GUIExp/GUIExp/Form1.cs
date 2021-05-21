using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;


namespace GUIExp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DialogResult dr =  MessageBox.Show("Do you want to close this form?", "Confirm", 
                MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (dr == DialogResult.Yes)
            {
                this.Close();
            }
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button1.Text = "Exit";
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            DialogResult dr = MessageBox.Show("Do you want to sign in?", "Confirm",
                MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            string username = textBox2.Text;
            string password = textBox1.Text;
            string folder = @" "; // type path to the files here
            string fileName = "UserName.txt";
            string filePass = "Password.txt";
            string fullPath = folder + fileName;
            string fullPathP = folder + filePass;
            File.WriteAllText(fullPath, username);
            fileName = folder + "Pass.txt";     
            
            using (StreamWriter sw = File.AppendText(fullPath))
            {
                sw.WriteLine(username);
            }

            using (StreamWriter sw = File.AppendText(fullPathP))
            {
                sw.WriteLine(password);
            }

            //File.WriteAllText(fileName, password);
            if (dr == DialogResult.Yes)
            {
                this.Close();
            }

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
                
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
