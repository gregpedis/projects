using SixLabors.ImageSharp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.Helpers
{
    public static class PointHelper
    {
        public static PointF Generate(int width, int height)
        {
            var x = RandomHelper.Generate(width);
            var y = RandomHelper.Generate(height);
            return new PointF(x, y);
        }
    }
}
