/**
 * shis shit kinda wirks, but have some bugs, so you need to check manually
 */
#include <bitset>
#include <iostream>
#include <regex>
#include <string>
#include <vector>
using namespace std;

unsigned int bit_count(unsigned int n) {
  unsigned int count = 0;
  while (n) {
    count += n & 1;
    n >>= 1;
  }
  return count;
}

void f(int A, int B) {
  int8_t a = A, b = B;

  int R = A - B;
  int8_t r = a - b;
  int8_t n = abs(r);

  bitset<8> xa(a), xb(b), xr(r), xn(n);
  string sa = regex_replace(
             regex_replace(xa.to_string(), std::regex("0"), "0 & "),
             std::regex("1"), "1 & "),
         sb = regex_replace(
             regex_replace(xb.to_string(), std::regex("0"), "0 & "),
             std::regex("1"), "1 & "),
         sr = regex_replace(
             regex_replace(xr.to_string(), std::regex("0"), "0 & "),
             std::regex("1"), "1 & "),
         sn = regex_replace(
             regex_replace(xn.to_string(), std::regex("0"), "0 & "),
             std::regex("1"), "1 & "),
         car = xa.to_string();

  car.erase(car.begin());

  car = regex_replace(regex_replace(car, std::regex("0"), "\\rcar & "),
                      std::regex("1"), "\\ncar & ");

  car += " &";

  cout << R"(
$$\begin{array}{ccc|cccccccccccccc}
            \SPACE & \INT                                                                                        \\
                   & &)"
       << car << R"( & \SIGN &     & \USIGN               \\
)";
  cout << "\\MINUS  & A_{\\MM{пр.}} & " << sa << " & \\MINUS &  " << A
       << " & & \\MINUS & " << (int)(uint8_t)A << R"(  \\)" << endl;
  cout << "& B_{\\MM{пр.}} &" << sb << " & & " << B << " &  & & "
       << (int)(uint8_t)B
       << R"(  \\ \cline{2-2} \cline{5-10} \cline{12-13} \cline{15-16})"
       << endl;

  if (r > 0) {
    cout << "& C_{\\MM{пр.}} &" << sr << " & & " << R << " & & & "
         << (int)(uint8_t)R << R"(  \\)" << endl;
  } else {
    cout << "& C_{\\MM{пр.}} &" << sr << " & "
         << "  "
         << " & & & & " << (int)(uint8_t)R
         << R"(  \\ \cline{2-2} \cline{5-10} \cline{12-13} \cline{15-16})"
         << endl;
    cout << "& C_{\\MM{об.}} &" << sn << " & & " << R << " & & &"
         << "  "
         << R"(  \\)" << endl;
  }

  cout << R"(
\end{array}
    $$
    $$ )";
  int CF = xa[7] < xb[7], ZF = r == 0, PF = !(bit_count(r) % 2), AF = 0,
      SF = r != n, OF = r != R;
  cout << "CF=" << CF << ",\\ "
       << "ZF=" << ZF << ",\\ "
       << "PF=" << PF << ",\\ "
       << "AF=" << AF << ",\\ "
       << "SF=" << SF << ",\\ "
       << "OF=" << OF << ",\\ "
       << "$$" << endl;
}
int main() {
  int A = 80, B = 48;
  f(-A, B);
  f(A, -B);
}