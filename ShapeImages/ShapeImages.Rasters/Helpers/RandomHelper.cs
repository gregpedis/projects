using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.Helpers
{
    public static class RandomHelper
    {
        private static Random Random { get; set; }

        public static void Initialize(int? seed = null)
        {
            if (Random is null)
            {
                Random = seed.HasValue ? new(seed.Value) : new();
            }
            else
            {
                throw new ApplicationException("Randomizer has already been seeded");
            }
        }

        public static int Generate(int maxValue) => Random.Next(maxValue);
        public static int Generate(int minValue, int maxValue) => Random.Next(minValue, maxValue);

        public static T Choose<T>(IEnumerable<T> choices) => choices.ElementAt(Random.Next(choices.Count()));
    }
}
