#include <vector>

extern "C" {
    std::vector<int64_t>* _create(){
        return new std::vector<int64_t>;
    }
    std::vector<int64_t>* _from_arr(int64_t* p, int size) {
        std::vector<int64_t>* v = new std::vector<int64_t>;
        for (int i = 0; i < size; i++) {
            v->push_back(p[i]);
        }
        return v;
    }
    void _delete(std::vector<int64_t>* v){
        delete v;
    }
    int64_t _size(std::vector<int64_t>* v){
        return v->size();
    }
    int64_t _get(std::vector<int64_t>* v, int i){
        return v->at(i);
    }
    void _push_back(std::vector<int64_t>* v, int64_t i){
        v->push_back(i);
    }
}