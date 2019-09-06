impl Solution {
    pub fn reverse(x: i32) -> i32 {

        // pub const fn overflowing_mul(self, rhs: u32) -> (u32, bool)
        // overflowing check return (u32, bool)
        // so we need assume a ret (0i32, false)

        let mut ret = (0i32, false);
        let mut x = x;

        while x != 0 {
            let n = x % 10;
            x = x / 10;
            ret = ret.0.overflowing_mul(10);
            if ret.1 {
                return 0;
            }
            ret = ret.0.overflowing_add(n);
            if ret.1 {
                return 0;
            }
        }
        ret.0
    }
}

pub struct Solution;

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test() {
        assert_eq!(Solution::reverse(123), 321);
        assert_eq!(Solution::reverse(-123), -321);
        assert_eq!(Solution::reverse(120), 21);
        assert_eq!(Solution::reverse(1534236469), 0);
    }
}

