using ShapeImages.Rasters;
using ShapeImages.Rasters.Helpers;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;

namespace ShapeImages
{
    public class ImageHillClimb : HillClimbBase<Image<Rgba32>>
    {
        protected string SaveDirectory { get; init; }
        protected ImageEditor ImageEditor { get; init; }

        public ImageHillClimb(Image<Rgba32> initial, Image<Rgba32> target, ImageEditor editor, int totalSteps, int stepSize, int saveInterval, string saveDirectory)
            : base(initial, target, totalSteps, stepSize, saveInterval)
        {
            SaveDirectory = saveDirectory;
            ImageEditor = editor;
        }


        protected override double CalculateDistance(Image<Rgba32> before, Image<Rgba32> after)
        {
            double total = 0;

            before.ProcessPixelRows(after, (sourceAccessor, targetAccessor) =>
            {
                for (int i = 0; i < before.Height; i++)
                {
                    Span<Rgba32> sourceRow = sourceAccessor.GetRowSpan(i);
                    Span<Rgba32> targetRow = targetAccessor.GetRowSpan(i);

                    for (int j = 0; j < before.Width; j++)
                    {
                        var energyBefore = sourceRow[j];
                        var energyAfter = targetRow[j];
                        total += ColorHelper.ComparePixel(energyBefore, energyAfter);
                    }
                }
            });

            return total;
        }

        protected override Image<Rgba32> Mutate(Image<Rgba32> before) =>
            ImageEditor.Draw(before);

        protected override void SaveResult(Image<Rgba32> value, int step)
        {
            Directory.CreateDirectory(SaveDirectory);
            value.SaveAsPng(Path.Combine(SaveDirectory, $"{step}.png"));
        }
    }
}
