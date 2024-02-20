#include <iostream>
#include <vector>
#include <set>
#include <utility>

int cells, requests, tmp_;

struct Area {
    int size = 0, pos = 0;
    bool free = true;
    Area* prev = nullptr, *next = nullptr;
    ~Area() {
        if (prev) prev->next = next;
        if (next) next->prev = prev;
    }
};

struct APtrComp {
    bool operator()(const Area* lhs, const Area* rhs) const {
        if (lhs->size == rhs->size)
            return lhs->pos > rhs->pos;
        else
            return lhs->size < rhs->size;
    }
};

struct MemoryManager {
    struct AreaNP;
    Area* mem;
    std::multiset <Area*, APtrComp> free_mem;
    std::vector <Area*> req_mem;
    int cur_request = 0;
    MemoryManager(int cells, int requests) {
        mem = new Area;
        free_mem.insert(mem);
        mem->size = cells;
        req_mem.resize(requests);
    }
    std::pair<Area*, Area*> give(Area* th, int sz) {
        free_mem.erase(th);
        auto sec = new Area;
        th->free = false;
        sec->size = th->size - sz;
        sec->pos = sz + th->pos;
        if (th->next) th->next->prev = sec;
        th->size = sz;
        sec->next = th->next;
        th->next = sec;
        sec->prev = th;     
        if (sec->size == 0) {
            th->next = nullptr;
            delete sec;
        } else {
            free_mem.insert(sec);
        }
        return { th, sec };
    }
    void mergeNext(Area* th) {
        free_mem.erase(th);
        free_mem.erase(th->next);
        th->size += th->next->size;
        delete th->next;
        free_mem.insert(th);
        mem = th;
    }
    void mergePrev(Area* th) {
        free_mem.erase(th);
        free_mem.erase(th->prev);
        th->pos = th->prev->pos;
        th->size += th->prev->size;
        delete th->prev;
        free_mem.insert(th);
        mem = th;
    }
    void freeMem(Area* th) {
        free_mem.erase(th);
        th->free = true;
        free_mem.insert(th);
        if (th->next) if (th->next->free) mergeNext(th);
        if (th->prev) if (th->prev->free) mergePrev(th);
    }
    void solveRequest(int input) {
        if (input < 0) {
            if (req_mem[-input - 1]) freeMem(req_mem[-input - 1]);
        } else {
            if (free_mem.empty()) {
                req_mem[cur_request] = nullptr;
                std::cout << -1 << std::endl;
            } else {
                auto place = *free_mem.rbegin();
                if (place->size >= input) {
                    std::cout << place->pos + 1 << std::endl;
                    req_mem[cur_request] = give(place, input).first;
                } else {
                    req_mem[cur_request] = nullptr;
                    std::cout << -1 << std::endl;
                }
            }
        }
        ++cur_request;
    }
};

int main() {
    std::cin >> cells >> requests;
    MemoryManager MM(cells, requests);
    for (int i_ = 0; i_ < requests; ++i_) {
        std::cin >> tmp_;
        MM.solveRequest(tmp_);
    }
}
