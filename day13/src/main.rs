use itertools::Itertools;
use std::collections::HashSet;

// fn main() { (|(a, b)| { println!("part 1: {}\npart 2:\n{}", a, b) })( (|(a, b): (Vec<[i64; 2]>, Vec<(usize, i64)>)| { (|f: &dyn Fn((usize, i64), Vec<[i64; 2]>) -> Vec<[i64; 2]>, p: &dyn Fn(Vec<[i64; 2]>) -> String | { (f(b[0].clone(), a.clone()).len(), p(b.into_iter().fold(a, |a, v| { f(v, a) }))) })(&|(axis, offset): (usize, i64), coords: Vec<[i64; 2]>| -> Vec<[i64; 2]> { coords.into_iter().filter(|i| i[axis] != offset).map(|i| i.into_iter().enumerate().map(|(index, i)| { if index == axis && i > offset { 2 * offset - i } else { i } }).collect::<Vec<_>>().as_slice().try_into().unwrap()).collect::<HashSet<_>>().into_iter().collect() }, &|v: Vec<[i64; 2]>| -> String { (0..=*v.iter().map(|[a, b]| b).max().unwrap()).map(|y| (0..=*v.iter().map(|[a, b]| a).max().unwrap()).map(|x| { if v.contains(&[x, y]) {'█'} else {' '} }).join("")).join("\n") }) })((|a: Vec<String>| { (a[0].split("\n").map(|i| i.split(",")).flatten().map(|i| i.parse::<i64>().unwrap()).tuples().map(|(a, b)| [a, b]).collect::<Vec<[i64; 2]>>(), a[1].split("\n").filter(|i| i.trim() != "").map(|i| i.strip_prefix("fold along").unwrap().trim()).map(|i| i.split("=")).flatten().tuples().map(|(a, b)| (if a == "x" {0} else {1}, b.parse::<i64>().unwrap())).collect::<Vec<_>>()) })(include_str!("../input.txt").split("\n\n").map(Into::into).collect()))); }


fn main() {
    (|(a, b)| {
        println!("part 1: {}\npart 2:\n{}", a, b)
    })( (|(a, b): (Vec<[i64; 2]>, Vec<(usize, i64)>)| {
        (|f: &dyn Fn((usize, i64), Vec<[i64; 2]>) -> Vec<[i64; 2]>, p: &dyn Fn(Vec<[i64; 2]>) -> String | {
            (f(b[0].clone(), a.clone()).len(), p(b.into_iter().fold(a, |a, v| {
                f(v, a)
            })))
        })(&|(axis, offset): (usize, i64), coords: Vec<[i64; 2]>| -> Vec<[i64; 2]> {
            coords.into_iter()
                .filter(|i| i[axis] != offset)
                .map(|i| i.into_iter().enumerate().map(|(index, i)| {
                    if index == axis && i > offset {
                        2 * offset - i
                    } else {
                        i
                    }
                }).collect::<Vec<_>>()
                    .as_slice()
                    .try_into()
                    .unwrap())
                .collect::<HashSet<_>>()
                .into_iter()
                .collect()
        }, &|v: Vec<[i64; 2]>| -> String {
            (0..=*v.iter().map(|[a, b]| b).max().unwrap()).map(|y| (0..=*v.iter().map(|[a, b]| a).max().unwrap()).map(|x| {
                if v.contains(&[x, y]) {'█'} else {' '}
            }).join("")).join("\n")
        })
    })((|a: Vec<String>| {
        (a[0].split("\n")
             .map(|i| i.split(","))
             .flatten()
             .map(|i| i.parse::<i64>().unwrap())
             .tuples()
             .map(|(a, b)| [a, b])
             .collect::<Vec<[i64; 2]>>(),
         a[1].split("\n")
             .filter(|i| i.trim() != "")
             .map(|i| i.strip_prefix("fold along").unwrap().trim())
             .map(|i| i.split("="))
             .flatten()
             .tuples()
             .map(|(a, b)| (if a == "x" {0} else {1}, b.parse::<i64>().unwrap()))
             .collect::<Vec<_>>()
        ) })(include_str!("../input.txt").split("\n\n").map(Into::into).collect())));
}
