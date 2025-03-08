// See https://aka.ms/new-console-template for more information

using System.Diagnostics;
using CoinRepresentation;

var correct = new List<int>(TestGenerator.Count());
var incorrect = new List<int>(TestGenerator.Count());
var scores = 0;

for (var i = 0; i < TestGenerator.Count(); i++)
    try
    {
        long sum = 0;
        var result = TestGenerator.Generate(i, out sum);
        Console.WriteLine("\nAttempting test instance {0} with {1} as the argument and {2} as the expected answer", i,
            sum, result);
        var watch = new Stopwatch();
        watch.Start();
        var answer = Solver.Solve(sum);

        if (result == answer)
        {
            scores++;
            correct.Add(i);
            Console.WriteLine(" :: SUCCESS (Time elapsed {0})", watch.Elapsed);
        }
        else
        {
            incorrect.Add(i);
            Console.WriteLine(" :: FAILED with an incorrect answer of {0}", answer);
        }
    }
    catch (Exception e)
    {
        incorrect.Add(i);
        Console.WriteLine(" :: FAILED with the runtime error {1}", i, e);
    }

Console.WriteLine("\nSummary: {0} tests out of {1} passed", scores, TestGenerator.Count());
Console.WriteLine("Tests passed ({1} to {2}): {0}", correct.Count == 0 ? "none" : string.Join(", ", correct), 0,
    TestGenerator.Count());
Console.WriteLine("Tests failed ({1} to {2}): {0}", incorrect.Count == 0 ? "none" : string.Join(", ", incorrect), 0,
    TestGenerator.Count());