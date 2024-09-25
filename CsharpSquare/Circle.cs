public class Circle : IShape
{
    public double Radius { get; }

    public Circle(double radius)
    {
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(radius, nameof(radius));
        Radius = radius;
    }

    public double Square()
    {
        return Math.PI * Math.Pow(Radius, 2);
    }
}