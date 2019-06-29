using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HuffmanCoding
{
    public class Program
    {
        public static void Main(string[] args)
        {
            if (!args.Any())
            {
                Console.WriteLine("An input string was not provided.");
                return;
            }

            var stringInput = args.Aggregate((res, next) => res + ' ' + next);

            var frequencyTable = Huffman.CreateFrequencyTable(stringInput);

            var nodeList = Huffman.CreateNodeList(stringInput, frequencyTable);
            var nodeTree = Huffman.CreateTreeStructure(nodeList);
            var encodingTable = new Dictionary<string, string>();
            Huffman.CreateEncodingTable(encodingTable, nodeTree, "");

            var binaryOutput = "";

            foreach (var symbol in stringInput)
            {
                binaryOutput += encodingTable[symbol.ToString()] + ' ';
            }

            PrintCompressionProcess(stringInput, frequencyTable, encodingTable, binaryOutput);
        }

        public static void PrintCompressionProcess(
            string stringInput,
            Dictionary<string, int> frequencyTable,
            Dictionary<string, string> encodingTable,
            string binaryOutput
            )
        {
            Console.WriteLine("Input for Huffman Coding");
            Console.WriteLine(stringInput + Environment.NewLine);

            Console.WriteLine("Symbol Frequencies");

            foreach (var kv in frequencyTable)
            {
                Console.WriteLine($"Value {kv.Key} has frequency of magnitude {kv.Value}");
            }

            Console.WriteLine();

            Console.WriteLine("Encoding Values");

            foreach (var kv in encodingTable)
            {
                Console.WriteLine($"Symbol {kv.Key} is encoded as {kv.Value}");
            }

            Console.WriteLine(Environment.NewLine + "Huffman Coded Output");
            Console.WriteLine(binaryOutput);
        }
    }
}
