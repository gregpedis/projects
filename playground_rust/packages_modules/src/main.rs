use packages_modules::*;

fn main() {
    let mut a = stuff::Shit { x: 3 };

    let shit = Thingies::A;
    let shit = Thingies::B(Shit2 { i: 42 });

    let shit = Thingies::C { x: 3 };
    let shit = Thingies::D(32);

    println!("Hello, world!");
    let a: banana;
    let b: apple;

    let b: b;
    let a: a;

    let closure = |x: f32| -> f32 { f32::powi(x, 2) };

    let res = integral(closure, -10.0, 11.0, 0.01);
    // let res = integral(closure, f32::NEG_INFINITY, f32::INFINITY, 0.01);
    println!("{}", res);
}