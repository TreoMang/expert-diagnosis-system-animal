using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Animal_Identify2
{
    public partial class Xem_hinh_form : Form
    {
        public Xem_hinh_form()
        {
            InitializeComponent();
        }

        public Xem_hinh_form(int n)
        {
            number = n;
            InitializeComponent();
        }

        List<Image> listImage = new List<Image>();
        int number = 0;

        private void AddHinh()
        {
            string source = Application.StartupPath.ToString();
            listImage.Add(Image.FromFile(source + "\\Image\\1ech.jpg")); //0
            listImage.Add(Image.FromFile(source + "\\Image\\2ky-nhong.jpg")); //1
            listImage.Add(Image.FromFile(source + "\\Image\\3ran.jpg")); //2
            listImage.Add(Image.FromFile(source + "\\Image\\4casau.jpg")); //3
            listImage.Add(Image.FromFile(source + "\\Image\\5rua.jpg")); //4 
            listImage.Add(Image.FromFile(source + "\\Image\\6ca_map.jpg")); //5
            listImage.Add(Image.FromFile(source + "\\Image\\7ca.jpg")); //6
            listImage.Add(Image.FromFile(source + "\\Image\\8Chuot-chui.jpg")); //7
            listImage.Add(Image.FromFile(source + "\\Image\\9kanguru.jpg")); //8
            listImage.Add(Image.FromFile(source + "\\Image\\10UNKNOWN.png")); //ĐÂY MỚI LÀ 9
            listImage.Add(Image.FromFile(source + "\\Image\\11tho.jpg")); //9
            listImage.Add(Image.FromFile(source + "\\Image\\12ca-heo.jpg"));//10
            listImage.Add(Image.FromFile(source + "\\Image\\13ca-voi.jpg"));//11
            listImage.Add(Image.FromFile(source + "\\Image\\14Ngua-van.png"));//12
            listImage.Add(Image.FromFile(source + "\\Image\\15tegiac.jpg"));//13
            listImage.Add(Image.FromFile(source + "\\Image\\16lacda.jpg"));//14
            listImage.Add(Image.FromFile(source + "\\Image\\17huou-cao-co.jpg"));//15
            listImage.Add(Image.FromFile(source + "\\Image\\18huou.jpg"));//16
            listImage.Add(Image.FromFile(source + "\\Image\\19Bo.jpg"));//17
            listImage.Add(Image.FromFile(source + "\\Image\\20cuu.jpg"));//18
            listImage.Add(Image.FromFile(source + "\\Image\\21hama.jpg"));//19
            listImage.Add(Image.FromFile(source + "\\Image\\22cho.jpg"));//20
            listImage.Add(Image.FromFile(source + "\\Image\\23meo.jpg"));//21
            listImage.Add(Image.FromFile(source + "\\Image\\24mooc.jpg"));//22
            listImage.Add(Image.FromFile(source + "\\Image\\25ho.jpg"));//23
            listImage.Add(Image.FromFile(source + "\\Image\\26babon.jpg"));//24
            listImage.Add(Image.FromFile(source + "\\Image\\27duoiuoi.jpg"));//25
            listImage.Add(Image.FromFile(source + "\\Image\\28Nguoi.jpg"));//26
            listImage.Add(Image.FromFile(source + "\\Image\\29khi.jpg"));//27
            listImage.Add(Image.FromFile(source + "\\Image\\30doi.jpg"));//28
            listImage.Add(Image.FromFile(source + "\\Image\\31chim.jpg"));//29
        }
        public void DisplayImage(int index)
        {
            AddHinh();
            pictureBox1.Image = listImage[index];
        }
        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        public void GetValue(int value)
        {
            number = value;
        } 

        private void Xem_hinh_form_Load(object sender, EventArgs e)
        {
            DisplayImage(number);
        }
    }
}
