impl Solution {


    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let _res: Vec<i32>;

        fn do_plus(digits: Vec<i32>) -> Vec<i32> {
            let mut digits = digits;
            let mut a = digits.pop().map_or(0, |i32| i32);
            if a < 9 {
                a = a + 1;
                digits.push(a);
                return digits;
            } else {
               let mut cur: Vec<i32> = do_plus(digits);
                cur.push(0);
                return cur;
            }
        }

        _res = do_plus(digits);
        _res
    }
}

pub struct Solution;

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test() {
        assert_eq!(Solution::plus_one(vec![1, 2, 3]), vec![1, 2, 4]);
        assert_eq!(Solution::plus_one(vec![9]), vec![1, 0]);
    }
}
