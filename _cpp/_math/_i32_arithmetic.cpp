#include <vector>
#include <functional>


std::vector<int32_t>* v_opp_i32(std::vector<int32_t>* f, std::vector<int32_t>* s, std::function<int32_t(int32_t,int32_t)> func, int32_t val){
    std::vector<int32_t>* rvec = new std::vector<int32_t>;
    int sz1 = std::min(f->size(), s->size());
    int sz2 = std::max(f->size(), s->size());
    for (int i = 0; i < sz2; i++) {
        if (i < sz1) rvec->push_back(func(f->at(i),s->at(i)));
        else if (f->size() == sz1) rvec->push_back(func(val,s->at(i)));
        else if (s->size() == sz1) rvec->push_back(func(f->at(i),val));
    }
    return rvec;
}

std::vector<int32_t>* z_opp_i32(std::vector<int32_t>* f, std::vector<int32_t>* s, std::function<int32_t(int32_t,int32_t)> func){
    return v_opp_i32(f, s, func, 0);
}

std::vector<int32_t>* o_opp_i32(std::vector<int32_t>* f, std::vector<int32_t>* s, std::function<int32_t(int32_t,int32_t)> func){
    return v_opp_i32(f, s, func, 1);
}

// Z_OPPS
extern "C" {

    std::vector<int32_t>* z_add_i32(std::vector<int32_t>* f, std::vector<int32_t>* s){
        return z_opp_i32(f, s, std::plus<int32_t>());
    }

    std::vector<int32_t>* z_sub_i32(std::vector<int32_t>* f, std::vector<int32_t>* s){
        return z_opp_i32(f, s, std::minus<int32_t>());
    }
    
    std::vector<int32_t>* z_mul_i32(std::vector<int32_t>* f, std::vector<int32_t>* s){
        return z_opp_i32(f, s, std::multiplies<int32_t>());
    }

    std::vector<int32_t>* z_fdiv_i32(std::vector<int32_t>* f, std::vector<int32_t>* s){
        return z_opp_i32(f, s, std::divides<int32_t>());
    }

}

// O_OPPS
extern "C" {
    std::vector<int32_t>* o_add_i32(std::vector<int32_t>* f, std::vector<int32_t>* s){
        return o_opp_i32(f, s, std::plus<int32_t>());
    }

    std::vector<int32_t>* o_sub_i32(std::vector<int32_t>* f, std::vector<int32_t>* s){
        return o_opp_i32(f, s, std::minus<int32_t>());
    }
    
    std::vector<int32_t>* o_mul_i32(std::vector<int32_t>* f, std::vector<int32_t>* s){
        return o_opp_i32(f, s, std::multiplies<int32_t>());
    }

    std::vector<int32_t>* o_fdiv_i32(std::vector<int32_t>* f, std::vector<int32_t>* s){
        return o_opp_i32(f, s, std::divides<int32_t>());
    }
}


// V_OPPS
extern "C" {
    std::vector<int32_t>* v_add_i32(std::vector<int32_t>* f, std::vector<int32_t>* s, int32_t val){
        return v_opp_i32(f, s, std::plus<int32_t>(), val);
    }

    std::vector<int32_t>* v_sub_i32(std::vector<int32_t>* f, std::vector<int32_t>* s, int32_t val){
        return v_opp_i32(f, s, std::minus<int32_t>(), val);
    }
    
    std::vector<int32_t>* v_mul_i32(std::vector<int32_t>* f, std::vector<int32_t>* s, int32_t val){
        return v_opp_i32(f, s, std::multiplies<int32_t>(), val);
    }

    std::vector<int32_t>* v_fdiv_i32(std::vector<int32_t>* f, std::vector<int32_t>* s, int32_t val){
        return v_opp_i32(f, s, std::divides<int32_t>(), val);
    }
}