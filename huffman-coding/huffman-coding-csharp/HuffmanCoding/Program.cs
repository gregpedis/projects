using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HuffmanCoding
{
    public class Program
    {
        static void Main(string[] args)
        {
            var input = "aabbccc";
            var frequencyTable = Huffman.CreateFrequencyTable(input);
            var nodeList = Huffman.CreateNodeList(input, frequencyTable);
            var nodeTree = Huffman.CreateTreeStructure(nodeList);



        }
    }
}
