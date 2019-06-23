using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HuffmanCoding
{
    public class PriorityQueue<T>
    {
        private SortedList<int, Queue<T>> _priorityQueue;

        public PriorityQueue()
        {
            _priorityQueue = new SortedList<int, Queue<T>>();
        }

        public void Enqueue(int priority, T value)
        {
            if (_priorityQueue.Any(kv => kv.Key == priority))
            {
                _priorityQueue[priority].Enqueue(value);
            }
            else
            {
                var newQueue = new Queue<T>();
                newQueue.Enqueue(value);
                _priorityQueue.Add(priority, newQueue);
            }
        }

        public T Dequeue()
        {
            var first_queue = _priorityQueue.First().Value;
            var value = first_queue.Dequeue();

            if (!first_queue.Any())
            {
                _priorityQueue.RemoveAt(0);
            }
            return value;
        }

        public int Count() =>  _priorityQueue.SelectMany(kv => kv.Value).Count();
    }
}
