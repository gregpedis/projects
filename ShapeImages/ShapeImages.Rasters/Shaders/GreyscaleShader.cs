using ShapeImages.Rasters.Shaders.Base;
using SixLabors.ImageSharp.PixelFormats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.Shaders
{
    public class GreyscaleShader : PixelShader
    {
        public override Rgba32 Apply(Rgba32 pixel)
        {
            byte res= (byte)((pixel.R + pixel.G + pixel.B) / 3);
            return new Rgba32(res, res, res, pixel.A);
        }
    }
}
