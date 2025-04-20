using SixLabors.ImageSharp;
using SixLabors.ImageSharp.ColorSpaces;
using SixLabors.ImageSharp.PixelFormats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.Shaders.Interfaces
{
    public interface IShader
    {
        Image<Rgba32> Execute(Image<Rgba32> image);
    }
}
