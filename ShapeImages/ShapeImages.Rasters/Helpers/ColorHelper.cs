using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages.Rasters.Helpers
{
    public static class ColorHelper
    {
        public static Color GenerateGreyscale(byte a = 255)
        {
            var v = (byte)RandomHelper.Generate(256);
            return Color.FromRgba(v, v, v, a);
        }

        public static Color GenerateColor(byte a = 255)
        {
            var r = (byte)RandomHelper.Generate(256);
            var g = (byte)RandomHelper.Generate(256);
            var b = (byte)RandomHelper.Generate(256);
            return Color.FromRgba(r,g,b,a);
        }

        public static double ComparePixel(Rgba32 x, Rgba32 y)
        {
            var res = Math.Pow(x.R - y.R, 2) + Math.Pow(x.G - y.G, 2) + Math.Pow(x.B - y.B, 2) + Math.Pow(x.A - y.A, 2);
            return Math.Sqrt(res);
        }
    }
}
