use std::collections::HashMap;
use std::io::stdin;

// Using a hash map and vectors,
// create a text interface to allow a user
// to add employee names to a department in a company.
// For example, “Add Sally to Engineering” or “Add Amir to Sales.”
// Then let the user retrieve a list of all people in a department
// or all people in the company by department, sorted alphabetically.

macro_rules! custom_println {
    ($format_string:expr $(, $arg:expr)*) => {
        println!("#####");
        println!($format_string $(, $arg)*);
    };
}

type Company = HashMap<String, Vec<String>>;

struct Add {
    department: String,
    employee: String,
}

enum Command {
    Add(Add),
    ListDepartment(String),
    ListAll,
}

fn main() {
    let mut company = Company::new();
    print_prompt();
    loop {
        custom_println!("Waiting...");
        let input = get_input();
        match parse_input(&input) {
            Some(command) => match command {
                Command::Add(data) => execute_add(&data, &mut company),
                Command::ListDepartment(department) => {
                    execute_list_department(&department, &company)
                }
                Command::ListAll => execute_list_all(&company),
            },
            None => println!("Something went wrong."),
        }
    }
}

fn print_prompt() {
    println!("Welcome to Corpa!");
    println!("You have the following options:");
    println!("  - Add [Employee] to [Department]");
    println!("  - List [Department]");
    println!("  - List");
}

fn get_input() -> String {
    let mut input = String::new();
    stdin()
        .read_line(&mut input)
        .expect("Something went wrong.");
    input
}

fn parse_input(data: &String) -> Option<Command> {
    let words = data.split_whitespace().collect::<Vec<&str>>();
    // let mut words = lower_case.split_whitespace();
    let verb = words.get(0); // add/list
    let arg1 = words.get(1); // employee/department
    let arg2 = words.get(3); // department
    match verb {
        Some(&"Add") => match (arg1, arg2) {
            (Some(employee), Some(department)) => Some(Command::Add(Add {
                employee: employee.to_string(),
                department: department.to_string(),
            })),
            (_, _) => None,
        },
        Some(&"List") => match arg1 {
            Some(department) => Some(Command::ListDepartment(department.to_string())),
            None => Some(Command::ListAll),
        },
        _ => None,
    }
}

fn execute_list_all(company: &Company) {
    println!("Listing all employees.");
    let mut keys = company.keys().clone().collect::<Vec<&String>>();
    keys.sort();
    for department in keys {
        execute_list_department(department, company);
    }
}

fn execute_list_department(department: &String, company: &Company) {
    println!("Listing employees for department: {}", department);
    let mut employees = company.get(department).unwrap().clone();
    employees.sort();

    for employee in employees {
        println!("{}", employee);
    }
}

fn execute_add(data: &Add, company: &mut Company) {
    let department = company
        .entry(data.department.to_string())
        .or_insert(Vec::new());
    department.push(data.employee.to_string());
    println!("Added {} to department {}!", data.employee, data.department);
}
