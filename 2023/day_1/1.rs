use std::fs;
use std::string;
fn main() {
    let mut tempstr = String::new();
    let mut lastnum: char;
    let mut firstnum: char;
    let mut finalnum = 0;
    let contents = fs::read_to_string("input1.txt")
        .expect("Should have been able to read file");
    let parts = contents.split("\n");
    for part in parts {
        for character in part.chars() {
            if character.is_numeric() {
                tempstr.push(character);
            };            
        };
        
        firstnum = tempstr.chars().nth(0);
        lastnum = tempstr.chars().nth((tempstr.len())-1);
    };
}
