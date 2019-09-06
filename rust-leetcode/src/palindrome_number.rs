impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let s: String = x.to_string();

        // reverse string in rust
        if s == s.chars().rev().collect::<String>() {
            return true;
        }
        false
    }
}

pub struct Solution;

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test() {
        assert_eq!(Solution::is_palindrome(121), true);
        assert_eq!(Solution::is_palindrome(-121), false);
        assert_eq!(Solution::is_palindrome(10), false);
    }
}
