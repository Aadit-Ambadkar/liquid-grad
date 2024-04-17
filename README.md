Shared Object files compiled to another repository. This currently builds successfully (I think) and can be used as seen in `lgrad/_python/_tests/`

Run compile.sh to compile c++ files to `_compiled`. This links to a submodule which can be used to download the .so files from other devices.

Currently implements `Int32Vector` and `Int64Vector`. Also implements a `math` library for operating on these two.