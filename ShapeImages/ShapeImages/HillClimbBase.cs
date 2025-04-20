using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeImages
{
    ///Let s = s0
    ///For k = 0 through kmax(exclusive):
    ///T ← temperature( 1 - (k+1)/kmax)
    ///Pick a random neighbour, snew ← neighbour(s)
    ///If P(E(s), E(snew), T) ≥ random(0, 1) :
    ///s ← snew
    ///Output: the final state s
    public abstract class HillClimbBase<T>
    {
        protected abstract T Mutate(T before);
        protected abstract double CalculateDistance(T before, T after);
        protected abstract void SaveResult(T value, int step);

        protected int TotalSteps { get; init; }
        protected int StepSize { get; init; }
        protected int SaveInterval { get; init; }

        protected T State { get; set; }
        protected T Target { get; init; }
        protected double CurrentDistance { get; set; }

        protected Stopwatch Stopwatch { get; init; } = new Stopwatch();

        protected HillClimbBase(T initial, T target, int totalSteps, int stepSize, int saveInterval)
        {
            StepSize = stepSize;
            TotalSteps = totalSteps;
            State = initial;
            Target = target;
            SaveInterval = saveInterval;

            CurrentDistance = CalculateDistance(State, Target);
        }

        protected async Task ExecuteStep(int step)
        {
            var tasks = Enumerable.Range(0, StepSize).Select(_ => Task.Run(() => Climb())).ToArray();
            var newStates = await Task.WhenAll(tasks);
            var (Distance, Value) = newStates.MinBy(state => state.Distance);

            if (Distance < CurrentDistance)
            {
                State = Value;
                CurrentDistance = Distance;
            }

            if ((step + 1) % SaveInterval == 0)
            {
                Console.WriteLine($"[{Stopwatch.Elapsed}] Saving state for step: {step+1}");
                SaveResult(State, step+1);
            }
        }

        protected (double Distance, T Value) Climb()
        {
            var mutated = Mutate(State);

            var distance = CalculateDistance(mutated, Target);
            return (distance, mutated);
        }

        public async Task<T> Execute()
        {
            Stopwatch.Restart();
            foreach (var step in Enumerable.Range(0, TotalSteps))
            {
                Console.WriteLine($"[{Stopwatch.Elapsed}] Executing step: {step}");
                await ExecuteStep(step);
            }

            return State;
        }
    }
}
