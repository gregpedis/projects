using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Processing;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Processing;
using SixLabors.ImageSharp.Drawing.Processing;
using SixLabors.ImageSharp.PixelFormats;
using SixLabors.ImageSharp.Drawing;
using SixLabors.ImageSharp.Processing.Processors;
using ShapeImages.Rasters.Shaders.Interfaces;
using ShapeImages.Rasters.ShaperGenerators;
using ShapeImages.Rasters.Helpers;

namespace ShapeImages.Rasters
{
    public class ImageEditor
    {
        protected bool Greyscale { get; init; }
        protected byte ChannelA { get; init; }
        protected ShapeFactory Factory { get; init; }
        protected DrawingOptions DrawingOptions { get; init; }

        public ImageEditor(int width, int height, byte channelA, bool greyscale = false, ShapeType? shapeType = null, DrawingOptions options = null)
        {
            ChannelA = channelA;
            Greyscale = greyscale;
            Factory = new ShapeFactory(width, height, shapeType);
            DrawingOptions = options ?? new DrawingOptions { GraphicsOptions = new GraphicsOptions { ColorBlendingMode = PixelColorBlendingMode.Normal } };
        }

        public Image<Rgba32> Draw(Image<Rgba32> image)
        {
            var shape = Factory.Create();
            var color = Greyscale ? ColorHelper.GenerateGreyscale(ChannelA) : ColorHelper.GenerateColor(ChannelA);
            var brush = Brushes.Solid(color);

            var next = image.Clone();

            next.Mutate(x => x.Fill(DrawingOptions, brush, shape));
            return next;
        }
    }
}