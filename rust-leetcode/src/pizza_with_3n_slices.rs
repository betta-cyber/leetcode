impl Solution {
    // 1. simplify the ring to a flat array
    // 2. sub-array maximum sum problem
    // 简化为
    // 给一个长度为 3n 的环状序列，你可以在其中选择 n 个数，并且任意两个数不能相邻，求这 n 个数的最大值。

    pub fn max_size(slices: &[i32], k: usize) -> i32 {
        let n = slices.len();
        let mut dp = vec![vec![0; n]; k];
        for i in 0..k {
            for j in 0..n {
                if i == 0 { dp[i][j] = slices[j]; }
                else if j < i { dp[i][j] = 0; }
                else if let Some(max) = dp[i-1][0..j-1].iter().max() {
                    dp[i][j] = slices[j] + max;
                }
            }
        }

        *dp[k-1][0..n].iter().max().unwrap()
    }

    pub fn max_size_slices(slices: Vec<i32>) -> i32 {
        let n = slices.len();
        // 环状序列相较于普通序列，相当于添加了一个限制：普通序列中的第一个和最后一个数不能同时选。
        let m1 = Self::max_size(&slices[0..n-1], n / 3);
        let m2 = Self::max_size(&slices[1..n], n / 3);
        m1.max(m2)
    }

}


pub struct Solution;

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test() {
        assert_eq!(Solution::max_size_slices(vec![1,2,3,4,5,6]), 10);
    }
}

