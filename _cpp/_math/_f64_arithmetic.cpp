#include <vector>
#include <functional>


std::vector<double>* v_opp_f64(std::vector<double>* f, std::vector<double>* s, std::function<double(double,double)> func, double val){
    std::vector<double>* rvec = new std::vector<double>;
    int sz1 = std::min(f->size(), s->size());
    int sz2 = std::max(f->size(), s->size());
    for (int i = 0; i < sz2; i++) {
        if (i < sz1) rvec->push_back(func(f->at(i),s->at(i)));
        else if (f->size() == sz1) rvec->push_back(func(val,s->at(i)));
        else if (s->size() == sz1) rvec->push_back(func(f->at(i),val));
    }
    
    return rvec;
}

std::vector<double>* z_opp_f64(std::vector<double>* f, std::vector<double>* s, std::function<double(double,double)> func){
    return v_opp_f64(f, s, func, 0LL);
}

std::vector<double>* o_opp_f64(std::vector<double>* f, std::vector<double>* s, std::function<double(double,double)> func){
    return v_opp_f64(f, s, func, 1LL);
}

// Z_OPPS
extern "C" {

    std::vector<double>* z_add_f64(std::vector<double>* f, std::vector<double>* s){
        return z_opp_f64(f, s, std::plus<double>());
    }

    std::vector<double>* z_sub_f64(std::vector<double>* f, std::vector<double>* s){
        return z_opp_f64(f, s, std::minus<double>());
    }
    
    std::vector<double>* z_mul_f64(std::vector<double>* f, std::vector<double>* s){
        return z_opp_f64(f, s, std::multiplies<double>());
    }

}

// O_OPPS
extern "C" {
    std::vector<double>* o_add_f64(std::vector<double>* f, std::vector<double>* s){
        return o_opp_f64(f, s, std::plus<double>());
    }

    std::vector<double>* o_sub_f64(std::vector<double>* f, std::vector<double>* s){
        return o_opp_f64(f, s, std::minus<double>());
    }
    
    std::vector<double>* o_mul_f64(std::vector<double>* f, std::vector<double>* s){
        return o_opp_f64(f, s, std::multiplies<double>());
    }

    std::vector<double>* o_div_f64(std::vector<double>* f, std::vector<double>* s){
        return o_opp_f64(f, s, std::divides<double>());
    }
}


// V_OPPS
extern "C" {
    std::vector<double>* v_add_f64(std::vector<double>* f, std::vector<double>* s, double val){
        return v_opp_f64(f, s, std::plus<double>(), val);
    }

    std::vector<double>* v_sub_f64(std::vector<double>* f, std::vector<double>* s, double val){
        return v_opp_f64(f, s, std::minus<double>(), val);
    }
    
    std::vector<double>* v_mul_f64(std::vector<double>* f, std::vector<double>* s, double val){
        return v_opp_f64(f, s, std::multiplies<double>(), val);
    }

    std::vector<double>* v_div_f64(std::vector<double>* f, std::vector<double>* s, double val){
        return v_opp_f64(f, s, std::divides<double>(), val);
    }
}