using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Animal_Identify2
{
    class rules
    {
        int index;
        string rule;

        public int Index
        {
            get { return index; }
            set { index = value; }
        }

        public string Rule
        {
            get { return rule; }
            set { rule = value; }
        }

        public rules()
        {
            index = 0;
            rule="";
        }

        public rules(int n, string str)
        {
            index = n;
            rule = str;
        }

       

    }
}
