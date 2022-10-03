import java.util.Random;

class Lab1 {
  short[] a;
  double[] x;
  double[][] b;

  static double f1(double x) {
    return Math.log(Math.abs(Math.log(Math.pow(Math.tan(x), 2))));
  }

  static double f2(double x) {
    return Math.pow(
        (Math.sin(Math.atan((x + 0.5) / 25.0))) /
            (Math.cbrt(Math.pow(x, x)) - 1),
        Math.sin(Math.pow(x, x * (x + 2.0 / 3.0))));
  }

  static double f3(double x) {
    return Math.sin(Math.asin(Math.cos(Math.tan(Math.cos(x)))));
  }

  public Lab1() {
    a = new short[8];
    for (short t = 4, idx = 0; t <= 18; t += 2, ++idx)
      a[idx] = t;

    x = new Random().doubles(19, -12, 13).toArray();

    b = new double[a.length][x.length];
    for (int i = 0; i < a.length; ++i) {
      for (int j = 0; j < x.length; ++j) {
        if (a[i] == 16)
          b[i][j] = f1(x[j]);
        else if (a[i] == 10 || a[i] == 12 || a[i] == 14 || a[i] == 18)
          b[i][j] = f2(x[j]);
        else
          b[i][j] = f3(x[j]);
      }
    }
  }

  void print() {
    for (int i = 0; i < b.length; ++i) {
      for (int j = 0; j < b[i].length; ++j)
        System.out.format("%10.5f ", b[i][j]);
      System.out.println();
    }
  }

  public static void main(String[] args) {
    var lab1 = new Lab1();
    lab1.print();
  }
}
