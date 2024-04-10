#include <vector>
#include <functional>


std::vector<int64_t>* v_opp_i64(std::vector<int64_t>* f, std::vector<int64_t>* s, std::function<int64_t(int64_t,int64_t)> func, int64_t val){
    std::vector<int64_t>* rvec = new std::vector<int64_t>;
    int sz1 = std::min(f->size(), s->size());
    int sz2 = std::max(f->size(), s->size());
    for (int i = 0; i < sz2; i++) {
        if (i < sz1) rvec->push_back(func(f->at(i),s->at(i)));
        else if (f->size() == sz1) rvec->push_back(func(val,s->at(i)));
        else if (s->size() == sz1) rvec->push_back(func(f->at(i),val));
    }
    return rvec;
}

std::vector<int64_t>* z_opp_i64(std::vector<int64_t>* f, std::vector<int64_t>* s, std::function<int64_t(int64_t,int64_t)> func){
    return v_opp_i64(f, s, func, 0);
}

std::vector<int64_t>* o_opp_i64(std::vector<int64_t>* f, std::vector<int64_t>* s, std::function<int64_t(int64_t,int64_t)> func){
    return v_opp_i64(f, s, func, 1);
}

// Z_OPPS
extern "C" {

    std::vector<int64_t>* z_add_i64(std::vector<int64_t>* f, std::vector<int64_t>* s){
        return z_opp_i64(f, s, std::plus<int64_t>());
    }

    std::vector<int64_t>* z_sub_i64(std::vector<int64_t>* f, std::vector<int64_t>* s){
        return z_opp_i64(f, s, std::minus<int64_t>());
    }
    
    std::vector<int64_t>* z_mul_i64(std::vector<int64_t>* f, std::vector<int64_t>* s){
        return z_opp_i64(f, s, std::multiplies<int64_t>());
    }

    std::vector<int64_t>* z_fdiv_i64(std::vector<int64_t>* f, std::vector<int64_t>* s){
        return z_opp_i64(f, s, std::divides<int64_t>());
    }

}

// O_OPPS
extern "C" {
    std::vector<int64_t>* o_add_i64(std::vector<int64_t>* f, std::vector<int64_t>* s){
        return o_opp_i64(f, s, std::plus<int64_t>());
    }

    std::vector<int64_t>* o_sub_i64(std::vector<int64_t>* f, std::vector<int64_t>* s){
        return o_opp_i64(f, s, std::minus<int64_t>());
    }
    
    std::vector<int64_t>* o_mul_i64(std::vector<int64_t>* f, std::vector<int64_t>* s){
        return o_opp_i64(f, s, std::multiplies<int64_t>());
    }

    std::vector<int64_t>* o_fdiv_i64(std::vector<int64_t>* f, std::vector<int64_t>* s){
        return o_opp_i64(f, s, std::divides<int64_t>());
    }
}


// V_OPPS
extern "C" {
    std::vector<int64_t>* v_add_i64(std::vector<int64_t>* f, std::vector<int64_t>* s, int64_t val){
        return v_opp_i64(f, s, std::plus<int64_t>(), val);
    }

    std::vector<int64_t>* v_sub_i64(std::vector<int64_t>* f, std::vector<int64_t>* s, int64_t val){
        return v_opp_i64(f, s, std::minus<int64_t>(), val);
    }
    
    std::vector<int64_t>* v_mul_i64(std::vector<int64_t>* f, std::vector<int64_t>* s, int64_t val){
        return v_opp_i64(f, s, std::multiplies<int64_t>(), val);
    }

    std::vector<int64_t>* v_fdiv_i64(std::vector<int64_t>* f, std::vector<int64_t>* s, int64_t val){
        return v_opp_i64(f, s, std::divides<int64_t>(), val);
    }
}