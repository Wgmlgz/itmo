import java.util.Random;

class Lab1 {
  public static void main(String[] args) {
    short[] a = new short[8];
    for (short t = 4, idx = 0; t <= 18; t += 2, ++idx)
      a[idx] = t;

    double[] x = new Random().doubles(19, -12, 13).toArray();

    double[][] b = new double[a.length][x.length];
    for (int i = 0; i < a.length; ++i) {
      for (int j = 0; j < x.length; ++j) {
        if (a[i] == 16)
          b[i][j] = Math.log(Math.abs(Math.log(Math.pow(Math.tan(x[j]), 2))));
        else if (a[i] == 10 || a[i] == 12 || a[i] == 14 || a[i] == 18)
          b[i][j] = Math.pow(
              (Math.sin(Math.atan((x[j] + 0.5) / 25.0))) /
                  (Math.cbrt(Math.pow(x[j], x[j])) - 1),
              Math.sin(Math.pow(x[j], x[j] * (x[j] + 2.0 / 3.0))));
        else
          b[i][j] = Math.sin(Math.asin(Math.cos(Math.tan(Math.cos(x[j])))));
      }
    }

    for (int i = 0; i < a.length; ++i) {
      for (int j = 0; j < b.length; ++j)
        System.out.format("%9.5f ", b[i][j]);
      System.out.println();
    }
  }
}
