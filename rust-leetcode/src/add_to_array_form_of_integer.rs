impl Solution {
    pub fn add_to_array_form(a: Vec<i32>, k: i32) -> Vec<i32> {
        let _res: Vec<i32>;

        fn do_plus(digits: Vec<i32>, k: i32, flag: bool) -> Vec<i32> {
            let mut digits = digits;
            let a = digits.pop().map_or(0, |i32| i32);
            let b = k % 10;
            let v = k / 10;

            let mut flag = flag;

            let mut cur = a + b;
            if flag {
                cur += 1;
            }

            if cur >= 10 {
                cur = cur - 10;
                flag = true;
            } else {
                flag = false;
            }

            if v > 0 {
                let mut last: Vec<i32> = do_plus(digits, v, flag);
                last.push(cur);
                return last;
            } else {
                if flag == true {
                    let mut last: Vec<i32> = do_plus(digits, v, flag);
                    last.push(cur);
                    return last;
                }
                digits.push(cur);
                return digits;
            }
        }

        _res = do_plus(a, k, false);
        _res
    }
}

pub struct Solution;

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test() {
        assert_eq!(Solution::add_to_array_form(vec![1, 2, 0, 0], 34), vec![1, 2, 3, 4]);
        assert_eq!(Solution::add_to_array_form(vec![2, 1, 5], 806), vec![1, 0, 2, 1]);
        assert_eq!(Solution::add_to_array_form(vec![2, 7, 4], 181), vec![4, 5, 5]);
        assert_eq!(Solution::add_to_array_form(vec![9,9,9,9,9,9,9,9,9,9], 1), vec![1,0,0,0,0,0,0,0,0,0,0]);
    }
}
