using ShapeImages;
using ShapeImages.Rasters;
using ShapeImages.Rasters.Helpers;
using ShapeImages.Rasters.Shaders;
using ShapeImages.Rasters.Shaders.Interfaces;
using ShapeImages.Rasters.ShaperGenerators;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;

var inputPaths = new string[]
{
@"C:\Users\trafa\Desktop\lena.jpg",
@"C:\Users\trafa\Desktop\earing.jpg",
@"C:\Users\trafa\Desktop\madeline.png",
@"C:\Users\trafa\Desktop\cristian.jpg",
};

var inputPath = inputPaths[3];
var outputPath = @"C:\Users\trafa\Desktop\result.png";
var outputDir = @"C:\Users\trafa\Desktop\HillClimb";

//ApplyShader(new GreyscaleShader());
//ApplyShader(new OneBitShader());

var seed = new Random().Next(420);
Console.WriteLine($"Seed: {seed}");
RandomHelper.Initialize(seed);
//ApplyShader(new OneBitShader());
await DoHillClimb();


void ApplyShader(IPixelShader shader)
{
    var initial = Image.Load<Rgba32>(inputPath);
    var result = shader.Execute(initial);
    result.SaveAsPng(outputPath);
}

async Task DoHillClimb()
{
    var target = Image.Load<Rgba32>(inputPath);
    var initial = new Image<Rgba32>(target.Width, target.Height);

    byte a = 123;
    var greyscale = false;
    ShapeType? shapeType = ShapeType.Rectangle;

    var steps = 1_000;
    var stepSize = 50;
    var savePer = 10;

    var editor = new ImageEditor(initial.Width, initial.Height, a, greyscale, shapeType);
    var hillClimb = new ImageHillClimb(initial, target, editor, steps, stepSize, savePer, outputDir);

    await hillClimb.Execute();
}
