using System;
using System.Collections.Generic;
using System.Text;

namespace LearnInheritance
{
    class Bicycle : Vehicle
    {
        public Bicycle(double Speed) : base(Speed)
        {
            Wheels = 2;
        }
        public override void SpeedUp()
        {
            Speed += 5;
            if (Speed > 15)
            {
                Speed = 15;
            }
        }
        public override void SlowDown()
        {
            Speed -= 5;
            if (Speed < 0)
            {
                Speed = 0;
            }
        }
        public override string Describe()
        {
            return $"This Bicycle is moving on {Wheels} wheels at {Speed} km/h, with license plate {LicensePlate}.";
        }
    }
}