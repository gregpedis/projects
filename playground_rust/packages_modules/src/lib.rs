pub use crate::garden::banana::banana;
pub use garden::apple::apple;

pub use garden::{apple::apple as a, banana::banana as b};

mod garden;

pub mod stuff {
    pub struct Shit {
       pub x: i32,
    }
}

pub struct Shit2 {
    pub i: i32,
}

pub enum Thingies
{
    A,
    B(Shit2),
    C {x:i32},
    D(i32),
    E(Shit2,i32),
}

pub fn integral(function: fn(f32) -> f32, from: f32, to: f32, step: f32) -> f32 {
    let mut current = from;
    let mut total = 0.0;

    println!("Total numbers of steps to take:{}", (to - from) / step);

    while current < to {
        total += function(current);
        current += step;
    }

    return total * step;
}

pub mod grandad {
    pub mod dad {
        pub mod child1 {
            pub type c1 = i32;

            fn shit() {
                let a: super::child2::c2;
            }
        }
        mod child2 {
            pub type c2 = i32;

            fn a() {}
        }
    }

    pub mod mom {
        pub mod child3 {
            pub type c3 = i32;
        }
        pub mod child4 {
            pub type c4 = i32;
        }
    }
}

mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting;


mod shit{

pub fn eat_at_restaurant() {
    super::hosting::add_to_waitlist();
}
}

