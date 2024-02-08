#include<iostream>
#include <vector>

int main() {
    int n_, k_;
    std::cin >> n_ >> k_;
    std::vector<int> m_;
    for (int i = 0; i < n_; ++i) {
        int tmp_;
        std::cin >> tmp_;
        m_.push_back(tmp_);
    }
    int ehs = 1;
    int rhs = m_[n_ - 1];
    while (rhs - ehs > 1) {
        int mid = (rhs + ehs) / 2;
        bool b_ = true;
        int tmp = m_[0];
        int cl = k_;
        for (int i = 1; i < n_; ++i) {
            if (m_[i] - tmp >= mid) {
                tmp = m_[i];
                --cl;
            }
        }
        if (cl > 1) {
            b_ = false;
        }
        if (b_) {
            ehs = mid;
        } else {
            rhs = mid;
        }
    }
    std::cout << ehs;
}