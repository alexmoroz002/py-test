namespace CsharpSquare.Tests;

public class TriangleTests
{
    [Theory]
    [InlineData(3, 4, 5, 6)]
    [InlineData(0.5, 8, 8.49, 0.41)]
    [InlineData(4, 4, 4, 6.9282)]
    public void TriangleSquareOk(double a, double b, double c, double exp)
    {
        var triangle = new Triangle(a, b, c);
        Assert.Equal(exp, triangle.Square(), 0.0001);
    }

    [Fact]
    public void TriangleRight()
    {
        var triangle = new Triangle(3, 4, 5);
        Assert.True(triangle.IsRight);
    }

    [Fact]
    public void TriangleSidesIncorrectThrow()
    {
        Assert.Throws<ArgumentException>(() => new Triangle(1, 2, 3));
    }

    [Fact]
    public void TriangleSidesNegativeThrow()
    {
        Assert.Throws<ArgumentException>(() => new Triangle(-1, 2, 3));
    }
}