using ShapeImages.Rasters.Helpers;
using SixLabors.ImageSharp.Drawing;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.ShaperGenerators.Generators
{
    public class CircleGenerator : IShapeGenerator
    {
        public IPath Generate(int width, int height)
        {
            var center = PointHelper.Generate(width, height);
            var radius = RandomHelper.Generate(10, width); // here both values are arbitrary
            return new EllipsePolygon(center, radius);
        }
    }
}
