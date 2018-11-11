using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Threading;

namespace Animal_Identify2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        #region Variables
        List<int> Known = new List<int>();
        List<rules> Rulelist = new List<rules>();
        List<List<int>> facts_in_rules = new List<List<int>>();

        Dictionary<int, string> Questions = new Dictionary<int,string>();
        Stack<string> astack = new Stack<string>();

        List<string> list_cau_hoi = new List<string>();
        List<string> list_tra_loi = new List<string>();

        int lan_thu = 1;
        public static int imageNum = 0;

        #endregion
        private void Form1_Load(object sender, EventArgs e)
        {
            Load_Fact();
        }


        private void btnRun_Click(object sender, EventArgs e)
        {
            Load_Rule();
            Tao_Danh_Sach_Cau_Hoi();
            Tao_danh_sach_Facts();
            
            
            Deduction2(1);
            btnRun.Enabled = false;
            btnS.Enabled = true;
        }

        #region Functions
        private void Asking(Dictionary<int, string> Q, int thutu)
        {
            //rtb2.Text += Q[thutu]+"\r\n";
            txttxt.Text = Q[thutu] + "\r\n";
            list_cau_hoi.Add(Q[thutu]);
        }

        private void Tao_danh_sach_Facts()
        {
            for (int i = 0; i < Rulelist.Count; i++)
            {
                facts_in_rules.Add(Get_Tokens(Rulelist[i].Rule));
            }
        }
        private bool CheckFinish()
        {
            //Kiem tra trong Known chua chua
            bool finish = false;
            for (int i = 0; i < Rulelist.Count; i++)
            {
                if (Check_Concide(Known, facts_in_rules[i]) == true)
                {
                    finish = true;
                    lblkq.Text = Display_Result(i)+" ====>>";

                    //Giai thich
                    Explanation(i);
                    imageNum = i;
                }
            }
            return finish;
        }

        private void Explanation(int index)
        {
            rtbGiaiThich.Text += Display_Result(index)+" vì:\r\n";
            for (int i = 0; i < list_cau_hoi.Count; i++)
            {
                rtbGiaiThich.Text += "Cho câu hỏi \"" + list_cau_hoi[i] + "\" bạn trả lời: "+list_tra_loi[i]+"\r\n";
            }
        }
        private void Tao_Danh_Sach_Cau_Hoi()
        {
            Questions.Add(1, "Nó là động vật máu nóng?");
            
            Questions.Add(3, "Nó luôn sống dưới nước?");
            
            Questions.Add(5, "Da nó có vảy không?");

            Questions.Add(7, "Nó biết nhảy không?");

            Questions.Add(9, "Vay nó tròn không?");

            Questions.Add(11, "Nó có chân không?");

            Questions.Add(13, "Nó là động vật bú sữa?");

            Questions.Add(15, "Nó là động vật ăn thịt?");

            Questions.Add(17, "Nó biết bay không?");

            Questions.Add(19, "Đuôi nó có thể dùng để nắm không?");

            Questions.Add(21, "Ngón cái của nó có đối diện các ngón khác không?");

            Questions.Add(23, "Nó có móng guốc không?");

            Questions.Add(25, "Nó có 2 móng?");

            Questions.Add(27, "Nó có sừng không?");

            Questions.Add(29, "Nó có một sừng đúng không?");

            Questions.Add(31, "Nó có lông xốp đúng không?");

            Questions.Add(33, "Nó có cánh tay khỏe?");

            Questions.Add(35, "Nó gần như không có lông?");

            Questions.Add(37, "Nó có nhiều xương không?");

            Questions.Add(39, "Nó có tai to không?");

            Questions.Add(41, "Nó sống dưới nước?");

            Questions.Add(43, "Nó sống trên mặt đất?");

            Questions.Add(45, "Nó nặng hơn 150 kg?");

            Questions.Add(47, "Nó có đuôi mỏng?");

            Questions.Add(49, "Nó đã được thuần hóa?");

            Questions.Add(51, "Có lớp mạ bảo vệ?");

            Questions.Add(53, "Nó ở sa mạc?");

            Questions.Add(55, "Có răng cửa lớn?");

            Questions.Add(57, "Có lớp mạ bảo vệ?");

            Questions.Add(59, "Nó được săn bắn cho mục đích thương mại?");
            
        }


       
        private void btnS_Click(object sender, EventArgs e)
        {
            //int index = lan;
            if (radioYes.Checked == false && radioNo.Checked == false)
                MessageBox.Show("Bạn chưa chọn câu trả lời nào. Vui lòng chọn lại!","Lỗi rồi",MessageBoxButtons.OK,MessageBoxIcon.Asterisk);
            else 
            {
                if (radioYes.Checked == true)
                {
                    Known.Add(lan_thu);
                    list_tra_loi.Add("có");
                }
                else if (radioNo.Checked == true)
                {
                    Known.Add(lan_thu + 1);
                    list_tra_loi.Add("không");
                }

                if (CheckFinish() == true)
                {
                    btnS.Enabled = false;
                    btnXemHinh.Enabled = true;
                }
                else
                {
                    switch (lan_thu)
                    {
                        case 1:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 3;
                            else lan_thu = 13;
                            break;
                        case 3:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 5;
                            else lan_thu = 37;
                            break;
                        case 5:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 7;
                            else lan_thu = 9;
                            break;
                        case 9:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 11;
                            //else lan_thu = 37;
                            break;
                        case 13:
                            if (radioYes.Checked == true) //yes
                                lan_thu = 15;
                            //else lan_thu = 37;
                            break;
                        case 15:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 23;
                            else lan_thu = 17;
                            break;
                        case 17:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 21;
                            //else lan_thu = 37;
                            break;
                        case 21:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 45;
                            else lan_thu = 19;
                            break;
                        case 45:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 47;
                            else lan_thu = 43;
                            break;
                        case 19:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 35;
                            //else lan_thu = 43;
                            break;
                        case 35:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 33;
                            break;
                        case 23:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 41;
                            else lan_thu = 25;
                            break;
                        case 25:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 51;
                            else lan_thu = 27;
                            break;
                        case 27:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 53;
                            else lan_thu = 29;
                            break;
                        case 29:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 31;
                            //else lan_thu = 43;
                            break;
                        case 31:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 49;
                            //else lan_thu = 43;
                            break;
                        case 41:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 55;
                            else lan_thu = 59;
                            break;
                        case 55:
                            if (radioNo.Checked == true) //yes
                                lan_thu = 57;
                            else lan_thu = 39;
                            break;
                    }

                    Deduction2(lan_thu);
                }
            }
        }

        private void Deduction2(int id)
        {
            Asking(Questions, id);
        }




        private void Load_Fact()
        {
            string path = "";
            path = @"\Su_kien.txt";
            StreamReader StrReader = new StreamReader(Application.StartupPath + path);

            string line;
            while (!StrReader.EndOfStream)
            {
                line = StrReader.ReadLine().Trim();
                rtb1.Text += line.ToString() + "\r\n";
            }
            StrReader.Close();
        }
        private void Load_Rule()
        {
            string path = "";
            path = @"\Luat.txt";
            StreamReader StrReader = new StreamReader(Application.StartupPath + path);

            string line;
            int indexbegin = 0;
            while (!StrReader.EndOfStream)
            {
                line = StrReader.ReadLine().Trim();
                if (line == "" || line.Contains("Begin") || line.Contains("End")) continue;
                rules rule = new rules(indexbegin, line);
                Rulelist.Add(rule);
                indexbegin++;
            }
            StrReader.Close();
        }

        //Get facts in right hand side rules
        private List<int> Get_Tokens(string str)
        {
            List<int> temp = new List<int>();

            string[] split = str.Split(':').ToArray();
            string str2 = split[1].ToString();


            string[] split2 = str2.Split(',').ToArray();

            for (int i = 0; i < split2.Length; i++)
            {
                if (!temp.Contains(Int32.Parse(split2[i])))
                    temp.Add(Int32.Parse(split2[i]));
            }
            return temp;
        }

        ////Nếu A trùng B
        private bool Check_Concide(List<int> A, List<int> B)
        { 
            bool ok = true;

            if (A.Count == B.Count)
            {
                foreach (int val in A)
                {
                    if (!B.Contains(val))
                        ok = false;
                }
            }
            else ok = false;
            
            return ok;
        }


        private string Display_Result(int vitri)
        {
            string str = "";
            switch (vitri)
            {
                case 0:
                    str = "Đó là con ếch";
                    break;
                case 1:
                    str = "Đó là con kì nhông";
                    break;
                case 2:
                    str = "Đó là con rắn";
                    break;
                case 3:
                    str = "Đó là con cá sấu";
                    break;
                case 4:
                    str = "Đó là con rùa";
                    break;
                case 5:
                    str = "Đó là con cá mập hoặc cá đuối";
                    break;
                case 6:
                    str = "Đó là con cá";
                    break;
                case 7:
                    str = "Đó là con chuột chũi / chuột chù hoặc voi";
                    break;
                case 8:
                    str = "Đó là con kangooro hoặc gấu Goala";
                    break;
                case 9:
                    str = "Con này chưa xác định được";
                    break;
                case 10:
                    str = "Đó là con thỏ";
                    break;
                case 11:
                    str = "Đó là con cá heo";
                    break;
                case 12:
                    str = "Đó là con cá voi";
                    break;
                case 13:
                    str = "Đó là con ngựa hoặc ngựa vằn";
                    break;
                case 14:
                    str = "Đó là con tê giác";
                    break;
                case 15:
                    str = "Đó là con lạc đà";
                    break;
                case 16:
                    str = "Đó là con hươu cao cổ";
                    break;
                case 17:
                    str = "Đó là con hươu hoặc nai hoặc hoẵng";
                    break;
                case 18:
                    str = "Đó là con bò";
                    break;
                case 19:
                    str = "Đó là con cừu";
                    break;
                case 20:
                    str = "Đó là con hà mã";
                    break;
                case 21:
                    str = "Đó là con sói hoặc chó";
                    break;
                case 22:
                    str = "Đó là con mèo";
                    break;
                case 23:
                    str = "Đó là con móoc";
                    break;
                case 24:
                    str = "Đó là con hổ hoặc sư tử hoặc gấu";
                    break;
                case 25:
                    str = "Đó là con babon";
                    break;
                case 26:
                    str = "Đó là con đười ươi hoặc khỉ đột";
                    break;
                case 27:
                    str = "Đó là con người";
                    break;
                case 28:
                    str = "Đó là con khỉ";
                    break;
                case 29:
                    str = "Đó là con dơi";
                    break;
                case 30:
                    str = "Đó là con chim";
                    break;
                
                default:
                    str = "Không tìm thấy";
                    break;

            }
            return str;
        }

        #endregion
        #region Event Handling

        private void btnReset_Click(object sender, EventArgs e)
        {
            Known.Clear();
            Rulelist.Clear();
            facts_in_rules.Clear();
            Questions.Clear();
            lan_thu = 1;
            list_cau_hoi.Clear();
            list_tra_loi.Clear();
            imageNum = 0;

            btnRun.Enabled = true;
            //btnS.Enabled = true;
            btnXemHinh.Enabled = false;
            

            txttxt.Text = "";
            radioYes.Checked = true;
            radioNo.Checked = false;
            rtbGiaiThich.ResetText();
            lblkq.Text = "Kết luận: " ;
        }



        private void btnXemHinh_Click(object sender, EventArgs e)
        {
            Xem_hinh_form xh = new Xem_hinh_form(imageNum);
            xh.ShowDialog();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void imageToolStripMenuItem_Click(object sender, EventArgs e)
        {
            btnXemHinh_Click(sender, e);
        }

        private void resetToolStripMenuItem_Click(object sender, EventArgs e)
        {
            btnReset_Click(sender, e);
        }

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            frmAbout f = new frmAbout();
            f.Show();
        }
        #endregion


    }
}
