use std::fmt::Debug;

fn main() {
    let mut rect = Rectangle {
        width: 42,
        height: 43,
    };
    println!("The rect area is {:#?}", rect.area());

    let added = rect.add(&rect);
    println!("The added rect area is {:#?}", added.area());

    let a = rect;

    let square = Rectangle::square(42);

    let mut s1 = String::from("");
    let s2 = s1;
    s1 = s2;
    // }
}

enum Thingies {
    One(i32) = 1,
    Two2{ value1: i32, value2: String} = 2,
}

enum Two {
    X = 1,
    Y = 2
}

struct Rectangle {
    width: i32,
    height: i32,
}

impl Rectangle {
    fn area(&self) -> i32 {
        self.height * self.width
    }

    fn add(&self, other: &Rectangle) -> Rectangle {
        Rectangle {
            width: self.width + other.width,
            height: self.height + other.height,
        }
    }

    fn square(size: i32) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}

impl Debug for Rectangle {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("Rectangle")
            .field("width", &self.width)
            .field("height", &self.height)
            .finish()
    }
}
