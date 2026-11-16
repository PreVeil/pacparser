fn main() {
    println!("cargo:rustc-link-search=native=./libs");
    println!("cargo:rustc-link-lib=static=pacparser");
    println!("cargo:rustc-link-lib=static=js");
}
