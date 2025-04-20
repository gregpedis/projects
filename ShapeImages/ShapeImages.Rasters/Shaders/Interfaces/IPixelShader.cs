using SixLabors.ImageSharp.PixelFormats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.Shaders.Interfaces
{
    public interface IPixelShader : IShader
    {
        Rgba32 Apply(Rgba32 pixel);
    }
}
