using System.Collections.Generic;

namespace EgyszamjatekGUI
{
    class Player
    {
        public string Name { get; set; }
        public List<int> Tips { get; set; }

        public Player()
        {
            Tips = new List<int>();
        }
    }
}
