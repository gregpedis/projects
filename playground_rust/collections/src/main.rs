use std::collections::HashMap;

fn main() {
    let mut v = Vec::new();

    let mut vv = vec![1,2,3];

    let c = &vv[0];
    vv.push(42);

    v.push(42);

    let mut b = &vv[1];
    let mut a = vv[1];

    b = &31;
    a = 32;

    println!("Value: {}", a);
    println!("Value: {}", b);
    println!("Value: {}", vv[1]);
    vv[1] = 20;
    println!("Value: {}", vv[1]);

    let mut s = String::new();
    let mut a = "hello".to_string();
    a.push_str("cjeh");

    let res = s + &a;
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let s = format!("{s1}-{s2}-{s3}");

    let mut map = HashMap::new();
    map.insert("red", 42);
    map.insert("blue", 44);

    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);

    scores.entry(String::from("Yellow")).or_insert(50);
    scores.entry(String::from("Blue")).or_insert(50);

    println!("{:?}", scores);
 }
