using ShapeImages.Rasters.Shaders.Base;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.Shaders
{
    public class OneBitShader : PixelShader
    {
        public override Rgba32 Apply(Rgba32 pixel)
        {
            byte avg = (byte)((pixel.R + pixel.G + pixel.B) / 3);
            byte res = (byte)(avg >= 255 / 2 ? 255 : 0);
            return new Rgba32(res, res, res, pixel.A);
        }
    }
}
