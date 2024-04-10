g++ -fPIC -std=c++11 -shared -o ./_compiled/_vector_int32.so ./_cpp/_vector/_vector_int32.cpp -O3 -Wall
g++ -fPIC -std=c++11 -shared -o ./_compiled/_vector_int64.so ./_cpp/_vector/_vector_int64.cpp -O3 -Wall
g++ -fPIC -std=c++11 -shared -o ./_compiled/_arithmetic.so ./_cpp/_math/_i32_arithmetic.cpp ./_cpp/_math/_i64_arithmetic.cpp -O3 -Wall