using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics.Eventing.Reader;
using System.Drawing;
using System.IO;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using EasyModbus;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //string[] comPorts = SerialPort.GetPortNames();
            //for (int i = 0; i < comPorts.Length; i++)
            //{
            //    richTextBox1.Text = comPorts[i] + " ;";
            //}

            //ModbusClient modbusClient = new ModbusClient("COMP4");
            //modbusClient.Connect();
            //int[] readHoldingRegisters = modbusClient.ReadHoldingRegisters(0, 125);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ModbusClient modbusClient = new ModbusClient("COM4");
            modbusClient.Connect();
            int[] readHoldingRegisters = modbusClient.ReadHoldingRegisters(0, 125);
            // i/o狀態
            richTextBox1.Text += "Value of Holding Reg" + modbusClient.ReadHoldingRegisters(105, 1)[0].ToString();
            checkBox1.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2001, 1)[0].ToString());
            checkBox2.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2002, 1)[0].ToString());
            checkBox3.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2003, 1)[0].ToString());
            checkBox4.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2004, 1)[0].ToString());
            checkBox5.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2005, 1)[0].ToString());
            checkBox6.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2006, 1)[0].ToString());
            checkBox7.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2007, 1)[0].ToString());
            checkBox8.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2008, 1)[0].ToString());
            checkBox9.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2009, 1)[0].ToString());
            checkBox10.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2010, 1)[0].ToString());
            checkBox11.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2011, 1)[0].ToString());
            checkBox12.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2012, 1)[0].ToString());
            ////爐溫
            label3.Text = modbusClient.ReadHoldingRegisters(100, 1)[0].ToString();
            label4.Text = modbusClient.ReadHoldingRegisters(101, 1)[0].ToString();
            label5.Text = modbusClient.ReadHoldingRegisters(102, 1)[0].ToString();
            label6.Text = modbusClient.ReadHoldingRegisters(103, 1)[0].ToString();
            label7.Text = modbusClient.ReadHoldingRegisters(104, 1)[0].ToString();
            label8.Text = modbusClient.ReadHoldingRegisters(105, 1)[0].ToString();
            label9.Text = modbusClient.ReadHoldingRegisters(106, 1)[0].ToString();
            label10.Text = modbusClient.ReadHoldingRegisters(107, 1)[0].ToString();
            modbusClient.Disconnect();
            int A = 0;
            for (int i=1;i<=10;i++)
            {
                if(i%2==0)
            {
                 A = A + i;
            }
            }
            button1.Text = A.ToString();
            //richTextBox1.Text = "7.24";
            //button1.Text = "7.24";
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }
        int a = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            ModbusClient modbusClient = new ModbusClient("COM4");
            modbusClient.Connect();
            int[] readHoldingRegisters = modbusClient.ReadHoldingRegisters(0, 125);
            // i/o狀態
            richTextBox1.Text = "Value of Holding Reg" + modbusClient.ReadHoldingRegisters(105, 1)[0].ToString();
            checkBox1.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2001, 1)[0].ToString());
            checkBox2.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2002, 1)[0].ToString());
            checkBox3.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2003, 1)[0].ToString());
            checkBox4.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2004, 1)[0].ToString());
            checkBox5.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2005, 1)[0].ToString());
            checkBox6.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2006, 1)[0].ToString());
            checkBox7.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2007, 1)[0].ToString());
            checkBox8.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2008, 1)[0].ToString());
            checkBox9.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2009, 1)[0].ToString());
            checkBox10.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2010, 1)[0].ToString());
            checkBox11.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2011, 1)[0].ToString());
            checkBox12.Checked = Convert.ToBoolean(modbusClient.ReadCoils(2012, 1)[0].ToString());
            ////爐溫
            label3.Text = modbusClient.ReadHoldingRegisters(100, 1)[0].ToString();
            label4.Text = modbusClient.ReadHoldingRegisters(101, 1)[0].ToString();
            label5.Text = modbusClient.ReadHoldingRegisters(102, 1)[0].ToString();
            label6.Text = modbusClient.ReadHoldingRegisters(103, 1)[0].ToString();
            label7.Text = modbusClient.ReadHoldingRegisters(104, 1)[0].ToString();
            label8.Text = modbusClient.ReadHoldingRegisters(105, 1)[0].ToString();
            label9.Text = modbusClient.ReadHoldingRegisters(106, 1)[0].ToString();
            label10.Text = modbusClient.ReadHoldingRegisters(107, 1)[0].ToString();
            modbusClient.Disconnect(); //a = a + 1;
                                       //if(a%2==1

            //)
            //richTextBox1.Text = a.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //內容
            string data =DateTime.Now.ToString("HH:mm:ss")+","+"變數2"+"\r\n";
            //路徑
            string NAME = "LOG.csv";
            System.IO.File.AppendAllText(NAME,data,Encoding.Default);
        }
        public DataTable TxtConvertToDataTable(string File, string TableName, string delimiter)
        {
            DataTable dt = new DataTable();
            DataSet ds = new DataSet();

            StreamReader s = new StreamReader(File, System.Text.Encoding.Default);
            /* 
             使用 StreamReader 時，可指定字元編碼方式，StreamReader 建構函式(Stream, Encoding) : 
             使用指定的字元編碼方式，針對指定的資料流初始化 StreamReader 類別的新執行個體。
             EX:指定 Encoding 為 System.Text.Encoding.Default (作業系統目前 ANSI 字碼頁的編碼方式)
            */

            //string ss = s.ReadLine();//skip the first line

            string[] columns = s.ReadLine().Split(delimiter.ToCharArray());
            /*
             用 Console.ReadLine 方法來讀取檔案中的每一行
             String.Split 方法會根據一或多個分隔符號來分割輸入字串，以建立子字串陣列。 
             這個方法通常是在文字界限上分隔字串的最簡單方式。 它也可用來分割其他特定字元或字串上的字串。
            */
            ds.Tables.Add(TableName);
            foreach (string col in columns)
            {
                //int i = 0;                //string next = "";

                //bool added = false;
                //while (!added)
                //{
                //    string columnname = col + next;
                //   // Console.WriteLine("前" + columnname); 
                //    columnname = columnname.Replace("#", "");
                //   // Console.WriteLine("1" + columnname);
                //    columnname = columnname.Replace("'", "");
                //   // Console.WriteLine("2" + columnname);
                //    columnname = columnname.Replace("&", "");
                //   // Console.WriteLine("3"+columnname);
                //    /*
                //     這方法是將整個字串掃過只要搜索到指定字元(第一個參數)用指定字元(第二個參數)全部取代掉
                //     所以刪除特定字元只是應用取代這個功能特性來達成
                //    */

                //if (!ds.Tables[TableName].Columns.Contains(columnname))
                //{
                ds.Tables[TableName].Columns.Add("");
                //    added = true;
                //}
                //else
                //{
                //    i++;
                //    next = "_" + i.ToString();
                //}
                //}
            }

            string AllData = s.ReadToEnd();
            string[] rows = AllData.Split("\n".ToCharArray());

            foreach (string r in rows)
            {
                string[] items = r.Split(delimiter.ToCharArray());
                ds.Tables[TableName].Rows.Add(items);
            }

            s.Close();

            dt = ds.Tables[0];

            return dt;
        }


        private void button4_Click(object sender, EventArgs e)
        {
            DataTable dt = TxtConvertToDataTable("LOG.csv","tmp",".");//讀取檔案
            richTextBox1.Text= Convert.ToString(dt.Rows[0].ItemArray[1]);//讀取檔案欄
        }
    }
}
