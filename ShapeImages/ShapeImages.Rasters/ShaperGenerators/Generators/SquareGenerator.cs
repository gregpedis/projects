using ShapeImages.Rasters.Helpers;
using SixLabors.ImageSharp.Drawing;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.ShaperGenerators.Generators
{
    public class SquareGenerator : IShapeGenerator
    {
        public IPath Generate(int width, int height)
        {
            var center = PointHelper.Generate(width, height);
            var radius = RandomHelper.Generate(10, width); // here both values are arbitrary
            var angle = RandomHelper.Generate(180);
            return new RegularPolygon(center, 4, radius, angle);
        }
    }
}
