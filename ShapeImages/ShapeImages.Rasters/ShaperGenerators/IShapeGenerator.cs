using SixLabors.ImageSharp.Drawing;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.ShaperGenerators
{
    public interface IShapeGenerator
    {
        IPath Generate(int width, int height);
    }
}
