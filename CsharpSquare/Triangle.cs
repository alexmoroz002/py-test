public class Triangle : IShape
{
    public double A { get; }
    public double B { get; }
    public double C { get; }
    public bool IsRight { get; }

    public Triangle(double a, double b, double c)
    {
        if (a < 0 || b < 0 || c < 0) 
        {
            throw new ArgumentException("All sides must be positive");
        }

        if (a < b) (a, b) = (b, a);
        if (a < c) (a, c) = (c, a);

        if (a - (b + c) > -0.000001) 
        {
            throw new ArgumentException("Invalid triangle");
        }
        A = a;
        B = b;
        C = c;
        IsRight = Math.Pow(A, 2) == Math.Pow(B, 2) + Math.Pow(C, 2);
    }

    public double Square()
    {
        if (IsRight) 
        {
            return B * C / 2;
        }
        double pHalved = (A + B + C) / 2;
        return Math.Sqrt(pHalved * (pHalved - A) * (pHalved - B) * (pHalved - C));
    }
}