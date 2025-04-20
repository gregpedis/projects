fn main() {
    let mut s1 = String::from("string");
    doWork(&mut s1);
    println!("{}", s1);

    let s4 = &s1;
    let s3 = &s1;
    println!("{}{}", s3, s4);
    let s2 = &mut s1;


    let s4 = &mut s1;
    doWork(s4);
    let mut s3 = s4;

    let mut s1 = String::from("string");
    let s2 = &s1;
    let res = s1 == *s2;

    s1.clear();

    let ss = "hey";
    let sss = &ss[1..2];

    let mut xx = String::from("adq");
    first_word(&xx);
    first_word("hes");
}

fn doWork(s: &mut String) {
    s.push_str("string2");
}

fn doMove(mut s:String)
{
    s.push_str("string");
}

fn intWork(mut i:i32)
{
    let z = i+2;
    i = i+2;
}

fn first_word(s: &str) -> usize {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return i;
        }
    }

    s.len()
}

fn main2() {
    let mut my_string = String::from("hello world");
    let aa = &mut my_string;

    // `first_word` works on slices of `String`s, whether partial or whole
    // let word = first_word(&my_string[0..6]);
    // let word = first_word(&my_string[..]);
    // `first_word` also works on references to `String`s, which are equivalent
    // to whole slices of `String`s
    // let word = first_word(&my_string);
    let word = first_word(aa);

    let my_string_literal = "hello world";

    // `first_word` works on slices of string literals, whether partial or whole
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // Because string literals *are* string slices already,
    // this works too, without the slice syntax!
    let word = first_word(my_string_literal);
}