use std::{collections::HashMap, io::stdin};

// Given a list of integers,
// use a vector
// and return the median
// (when sorted, the value in the middle position)
// and mode
// (the value that occurs most often)

fn main() {
    loop {
        let input_result = get_numbers();
        match input_result {
            Ok(numbers) => do_work(numbers),
            Err(error) => println!("{}", error),
        }
    }
}

fn get_numbers() -> Result<Vec<i32>, String> {
    println!("Give me some numbers. E.g. 1 2 3");
    let mut input = String::new();
    stdin().read_line(&mut input).expect("Failed to read line");
    let res: Result<Vec<i32>, _> = input
        .split_whitespace()
        .map(|x| x.trim().parse::<i32>())
        .collect();

    match res {
        Ok(numbers) => Ok(numbers),
        Err(_) => Err("Some numbers could not be parsed".to_string()),
    }
}

fn do_work(ints: Vec<i32>) {
    let median = get_median(&ints);
    let mode = get_mode(&ints);
    println!("Median: {}", median);
    println!("Mode: {}", mode);
}

fn get_median(ints: &Vec<i32>) -> f32 {
    let mut sorted = ints.clone();
    sorted.sort();
    let length = sorted.len();
    if length % 2 == 0 {
        let left = sorted[length / 2];
        let right = sorted[(length - 1) / 2];
        (left + right) as f32 / 2 as f32
    } else {
        sorted[length / 2] as f32
    }
}

fn get_mode(ints: &Vec<i32>) -> i32 {
    let mut map = HashMap::new();
    for i in ints {
        let entry = map.entry(i).or_insert(0);
        *entry += 1;
    }

    let mut res = (&&0, &0);
    for kv in &map {
        if kv.1 > res.1 {
            res = kv;
        }
    }

    **res.0

    // // weird way
    //  **map
    //     .iter()
    //     .fold(
    //         (&&0, &0),
    //         |acc, (k, v)| if acc.1 < v { (k, v) } else { acc }
    //     )
    //     .0
}
