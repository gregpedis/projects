using System.Collections.Generic;
using System.Linq;

namespace HuffmanCoding
{
    public static class Huffman
    {
        public class HuffmanNode
        {
            public string Symbol { get; set; }

            public int Weight { get; set; }

            public HuffmanNode Left { get; set; }

            public HuffmanNode Right { get; set; }
        }

        public static Dictionary<string, int> CreateFrequencyTable(string input)
        {
            var frequencyTable = new Dictionary<string, int>();

            foreach (var c in input)
            {
                if (frequencyTable.ContainsKey(c.ToString()))
                {
                    frequencyTable[c.ToString()]++;
                }
                else
                {
                    frequencyTable.Add(c.ToString(), 1);
                }
            }

            return frequencyTable;
        }

        public static SortedList<int, HuffmanNode> CreateNodeList(string input, Dictionary<string, int> frequencyTable)
        {
            var nodeList = new SortedList<int, HuffmanNode>();

            foreach (var kv in frequencyTable)
            {
                var huffmanNode = new HuffmanNode()
                {
                    Symbol = kv.Key,
                    Weight = kv.Value
                };

                nodeList.Add(kv.Value, huffmanNode);
            }

            return nodeList;
        }

        public static HuffmanNode CreateTreeStructure(SortedList<int, HuffmanNode> nodeList)
        {
            while (nodeList.Count() > 1)
            {
                var nodeLeft = nodeList.Take(1).First().Value;
                nodeList.RemoveAt(0);
                var nodeRight = nodeList.Take(1).First().Value;
                nodeList.RemoveAt(0);

                var internalNode = new HuffmanNode()
                {
                    Left = nodeLeft,
                    Right = nodeRight,
                    Symbol = nodeLeft.Symbol + nodeRight.Symbol,
                    Weight = nodeLeft.Weight + nodeRight.Weight,
                };

                nodeList.Add(nodeLeft.Weight + nodeRight.Weight, internalNode);
            }

            return nodeList[0];
        }
    }
}
