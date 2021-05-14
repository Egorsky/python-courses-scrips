using System;

namespace LearnInheritance
{
    abstract class Vehicle
    {
        public string LicensePlate
        { get; private set; }

        public double Speed
        { get; protected set; }

        public int Wheels
        { get; protected set; }

        public Vehicle(double speed)
        {
            Speed = speed;
            LicensePlate = "123ab13";
        }

        public virtual void SpeedUp()
        {
            Speed += 5;
        }

        public virtual void SlowDown()
        {
            Speed -= 5;
        }

        public void Honk()
        {
            Console.WriteLine("HONK!");
        }
        public abstract string Describe();

    }
}