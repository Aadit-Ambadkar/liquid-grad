#include <vector>

extern "C" {
    std::vector<double>* _create(){
        return new std::vector<double>;
    }
    std::vector<double>* _from_arr(double* p, int size) {
        std::vector<double>* v = new std::vector<double>;
        for (int i = 0; i < size; i++) {
            v->push_back(p[i]);
        }
        return v;
    }
    void _delete(std::vector<double>* v){
        delete v;
    }
    int64_t _size(std::vector<double>* v){
        return v->size();
    }
    double _get(std::vector<double>* v, int i){
        return v->at(i);
    }
    void _push_back(std::vector<double>* v, double i){
        v->push_back(i);
    }
}