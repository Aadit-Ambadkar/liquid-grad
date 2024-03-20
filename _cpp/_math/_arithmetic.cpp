#include <vector>
#include <string>
#include <algorithm>

extern "C" {

    void* _add(void* v1, void* v2, char* param, size_t param_length) {
        if (strcmp(param, "int32") == 0) {
            std::vector<int32_t>* vec1 = (std::vector<int32_t>*) v1;
            std::vector<int32_t>* vec2 = (std::vector<int32_t>*) v2;

            size_t max_size = std::max(vec1->size(), vec2->size());
            std::vector<int32_t>* vec3 = new std::vector<int32_t>(max_size);

            for (int i = 0; i < max_size; i++) {
                if (i < vec1->size()) {
                    vec3->at(i) += vec1->at(i);
                }
                if (i < vec2->size()) {
                    vec3->at(i) += vec2->at(i);
                }
            }
            
            return vec3;
        } else if (strcmp(param, "int64") == 0) {
            std::vector<int64_t>* vec1 = (std::vector<int64_t>*) v1;
            std::vector<int64_t>* vec2 = (std::vector<int64_t>*) v2;

            size_t max_size = std::max(vec1->size(), vec2->size());
            std::vector<int64_t>* vec3 = new std::vector<int64_t>(max_size);

            for (int i = 0; i < max_size; i++) {
                if (i < vec1->size()) {
                    vec3->at(i) += vec1->at(i);
                }
                if (i < vec2->size()) {
                    vec3->at(i) += vec2->at(i);
                }
            }
            
            return vec3;
        }
    }
}



/*
lgrad.math.add(array1, array2)
array1.vec, array2.vec
need void pointer with array type :D

*/