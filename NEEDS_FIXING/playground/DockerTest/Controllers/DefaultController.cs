using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace DockerTest.Controllers
{
    [ApiController]
    [Route("")]
    public class DefaultController : ControllerBase
    {
        private static readonly string[] Summaries = new[]
        {
            "Freezing",
            "Bracing",
            "Chilly",
            "Cool",
            "Mild",
            "Warm",
            "Balmy",
            "Hot",
            "Sweltering",
            "Scorching"
        };

        private readonly ILogger<DefaultController> _logger;

        public DefaultController(
            ILogger<DefaultController> logger)
        {
            _logger = logger;
        }

        [HttpGet("welcome")]
        public ContentResult GetWelcome()
        {
            return new ContentResult
            {
                ContentType = "text/html",
                StatusCode = 200,
                Content = "<html><body>Welcome <b>idiot</b></body></html>"
            };
        }

        [HttpGet("weather")]
        public IActionResult GetWeather()
        {
            var rng = new Random();
            var idx = rng.Next(0, Summaries.Length);
            return new OkObjectResult(Summaries[idx]);
        }

        [HttpGet("dice")]
        public int GetDice()
        {
            var rng = new Random();
            return rng.Next(1, 7);
        }

    }
}
