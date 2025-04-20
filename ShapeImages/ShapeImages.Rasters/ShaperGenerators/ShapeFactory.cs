using ShapeImages.Rasters.Helpers;
using ShapeImages.Rasters.ShaperGenerators.Generators;
using SixLabors.ImageSharp.Drawing;

namespace ShapeImages.Rasters.ShaperGenerators
{
    public class ShapeFactory
    {
        protected static IShapeGenerator[] Generators => Enum.GetValues<ShapeType>().Select(x => CreateGenerator(x)).ToArray();

        protected int Width { get; init; }
        protected int Height { get; init; }
        protected IShapeGenerator? Generator { get; init; }
        protected bool RandomizeShape { get; init; }

        public ShapeFactory(int width, int height, ShapeType? shapeType = null)
        {
            Width = width;
            Height = height;
            RandomizeShape = !shapeType.HasValue;
            Generator = shapeType.HasValue ? CreateGenerator(shapeType.Value) : default;
        }

        public IPath Create()
        {
            var generator = RandomizeShape ? RandomHelper.Choose(Generators) : Generator!;
            return generator.Generate(Width, Height);
        }

        protected static IShapeGenerator CreateGenerator(ShapeType shapeType) =>
            shapeType switch
            {
                ShapeType.Square => new SquareGenerator(),
                ShapeType.Circle => new CircleGenerator(),
                ShapeType.Triangle => new TriangleGenerator(),
                ShapeType.Rectangle => new RectangleGenerator(),
                _ => throw new NotImplementedException(),
            };
    }
}
