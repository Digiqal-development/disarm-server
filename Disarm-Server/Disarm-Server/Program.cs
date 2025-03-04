using Disarm_Server;
using System.Diagnostics;

var builder = WebApplication.CreateBuilder(args);


builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddCors();


var app = builder.Build();

app.UseCors(builder => builder
.AllowAnyOrigin()
.AllowAnyMethod()
.AllowAnyHeader()
);


app.UseDeveloperExceptionPage();
app.UseSwagger();
app.UseSwaggerUI();
   

app.MapGet("/", () => "This is the Disarm foundation server");

app.MapGet("/techniques", () =>
{
    return Results.File(Directory.GetCurrentDirectory() + "/techniques.json", "application/json");
});


app.MapGet("/tags", () =>
{
    return Results.File(Directory.GetCurrentDirectory() + "/tags.json", "application/json");
});



app.MapPost("/clauses", async (ToDo input) =>
{

    var proc = new Process
    {
        StartInfo = new ProcessStartInfo
        {
            FileName = "/app/consoleapp/DisarmPythonResultGenerator",
            Arguments = "\"" + input.Sentence + "\"",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            RedirectStandardError = false,
            CreateNoWindow = true
        }
    };

    proc.Start();
    await proc.WaitForExitAsync();

    var output = await proc.StandardOutput.ReadToEndAsync();
    input.Result = output;
    return input;

});


app.Run();