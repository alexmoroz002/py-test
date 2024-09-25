namespace CsharpSquare.Tests;

public class CircleTests
{
    [Theory]
    [InlineData(0.1, 0.0314)]
    [InlineData(5, 78.5398)]
    [InlineData(10000.003, 314159453.8546)]
    public void CircleSquare_Ok(double r, double exp)
    {
        var circle = new Circle(r);
        Assert.Equal(exp, circle.Square(), 0.0001);
    }

    [Fact]
    public void CircleRadiusZeroThrow()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => new Circle(0));
    }

    [Fact]
    public void CircleRadiusNegativeThrow()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => new Circle(-5));
    }
}