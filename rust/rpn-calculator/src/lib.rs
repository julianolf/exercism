use crate::CalculatorInput::*;

#[derive(Debug)]
pub enum CalculatorInput {
    Add,
    Subtract,
    Multiply,
    Divide,
    Value(i32),
}

pub fn evaluate(inputs: &[CalculatorInput]) -> Option<i32> {
    let mut output: Vec<i32> = Vec::new();

    for input in inputs.iter() {
        match input {
            Value(v) => output.push(*v),
            Add | Subtract | Multiply | Divide if output.len() < 2 => return None,
            Add => {
                let b = output.pop().unwrap();
                let a = output.pop().unwrap();
                output.push(a + b);
            }
            Subtract => {
                let b = output.pop().unwrap();
                let a = output.pop().unwrap();
                output.push(a - b);
            }
            Multiply => {
                let b = output.pop().unwrap();
                let a = output.pop().unwrap();
                output.push(a * b);
            }
            Divide => {
                let b = output.pop().unwrap();
                let a = output.pop().unwrap();
                output.push(a / b);
            }
        }
    }

    if output.len() == 1 {
        output.pop()
    } else {
        None
    }
}
