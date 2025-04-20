use std::{collections::HashSet, io::stdin};

// Convert strings to pig latin. 
// The first consonant of each word is moved to the end of the word 
// and “ay” is added, 
// so “first” becomes “irst-fay.” 
// Words that start with a vowel have “hay” added to the end instead 
// (“apple” becomes “apple-hay”). 
// Keep in mind the details about UTF-8 encoding!

enum WordType {
    // s -> say
    ConsonantChar(String),
    // first -> irst-fay
    ConsonantWord(String),
    // apple -> apple-hay
    VowelWord(String),
}

fn main() {
    loop {
        let words = get_words();
        let transformed = pig_latin(&words);
        println!("{}", transformed);
    }
}

fn get_words() -> Vec<WordType> {
    println!("Give me a sentence");
    let mut input = String::new();
    stdin().read_line(&mut input).expect("Failed to read line");
    input
        .split_terminator([' ', ','])
        .map(|x| x.trim())
        .filter(|x| !x.is_empty())
        .map(classify_word)
        .collect()
}

fn classify_word(word: &str) -> WordType {
    let vowels: HashSet<char> = "aeiou".chars().collect();
    let first = word.chars().next().unwrap();

    if vowels.contains(&first) {
        WordType::VowelWord(word.to_string())
    } else {
        match word.len() {
            1 => WordType::ConsonantChar(word.to_string()),
            _ => WordType::ConsonantWord(word.to_string()),
        }
    }
}

fn pig_latin(words: &Vec<WordType>) -> String {
    words
        .iter()
        .map(|word| match word {
            WordType::VowelWord(x) => x.to_owned() + "-hay",
            WordType::ConsonantChar(x) => x.to_owned() + "ay",
            WordType::ConsonantWord(x) => {
                format!("{}-{}ay", x[1..].to_string(), x.chars().next().unwrap())
            }
        })
        .collect::<Vec<_>>()
        .join(" ")
}
