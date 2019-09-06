use std::char::from_digit;

impl Solution {

    pub fn add_binary(a: String, b: String) -> String {
        let mut res: Vec<char> = Vec::with_capacity(usize::max(a.len(), b.len()) + 1);

        let mut a: Vec<char> = a.chars().collect();
        let mut b: Vec<char> = b.chars().collect();
        let mut carry = 0;

        while !(a.is_empty() && b.is_empty()) {
            let mut sum = a.pop().map_or(0, |ch| ch.to_digit(10).unwrap())
                + b.pop().map_or(0, |ch| ch.to_digit(10).unwrap()) + carry;
            if sum > 1 {
                sum = sum - 2;
                carry = 1;
            } else {
                carry = 0;
            }
            res.push(from_digit(sum, 10).unwrap());
        }

        if carry > 0 {
            res.push('1');
        }
        res.into_iter().rev().collect()
    }
}

pub struct Solution;

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test() {
        assert_eq!(Solution::add_binary("11".to_owned(), "1".to_owned()), "100");
        assert_eq!(Solution::add_binary("1010".to_owned(), "1011".to_owned()), "10101");
    }
}

