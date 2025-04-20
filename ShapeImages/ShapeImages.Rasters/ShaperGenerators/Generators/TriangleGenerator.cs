using ShapeImages.Rasters.Helpers;
using SixLabors.ImageSharp.Drawing;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.ShaperGenerators.Generators
{
    public class TriangleGenerator : IShapeGenerator
    {
        public IPath Generate(int width, int height)
        {
            var point1 = PointHelper.Generate(width, height);
            var point2 = PointHelper.Generate(width, height);
            var point3 = PointHelper.Generate(width, height);

            var line1 = new LinearLineSegment(point1, point2);
            var line2 = new LinearLineSegment(point2, point3);
            var line3 = new LinearLineSegment(point3, point1);

            return new Polygon(line1, line2, line3);
        }
    }
}
