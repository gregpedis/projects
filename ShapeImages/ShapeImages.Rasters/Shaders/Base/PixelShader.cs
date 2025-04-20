using ShapeImages.Rasters.Shaders.Interfaces;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;

namespace ShapeImages.Rasters.Shaders.Base
{
    public abstract class PixelShader : IPixelShader
    {
        public abstract Rgba32 Apply(Rgba32 pixel);

        public Image<Rgba32> Execute(Image<Rgba32> image)
        {
            var res = new  Image<Rgba32>(image.Width, image.Height);

            for (int i = 0; i < image.Height; i++)
            {
                for (int j = 0; j < image.Width; j++)
                {
                    var before= image[j, i];
                    var after = Apply(before);
                    res[j, i] = after;
                }
            }

            return res;
        }
    }
}
