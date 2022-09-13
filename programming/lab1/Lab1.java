import java.util.Random;

class Lab1 {
  public static void main(String[] args) {
    Random rng = new Random();

    int[] a = rng.ints(10, -10, 10).toArray();
    double[] b = rng.doubles(10, -10, 10).toArray();

    double[][] c = new double[a.length][b.length];

    for (int i = 0; i < a.length; ++i) {
      for (int j = 0; j < b.length; ++j) {
        c[i][j] = a[i] * b[j];
      }
    }

    for (int i = 0; i < a.length; ++i) {
      for (int j = 0; j < b.length; ++j)
        System.out.format("%1.4f ", c[i][j]);
      System.out.println();
    }
  }
}
