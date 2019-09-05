impl Solution {
    pub fn sum_of_two_integers(a: i32, b: i32) -> i32 {
        a + b
    }
}

pub struct Solution;

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test() {
        assert_eq!(Solution::sum_of_two_integers(1, 2), 3);
    }
}
