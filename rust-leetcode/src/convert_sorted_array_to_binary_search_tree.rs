use std::rc::Rc;
use std::cell::RefCell;
use crate::TreeNode;

impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {

        fn bst_helper(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if nums.is_empty() { return None }
            Some(Rc::new(RefCell::new(TreeNode{
                val: nums[nums.len() / 2],
                left: bst_helper(&nums[0..(nums.len()/2)]),
                right: bst_helper(&nums[(nums.len()/2+1)..]),
            })))
        }

        bst_helper(&nums[..])
    }
}

pub struct Solution;

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::btree;

    #[test]
    fn test() {
        assert_eq!(Solution::sorted_array_to_bst(vec![-10, -3, 0, 5, 9]), btree![0, -3, 9, -10, null, 5]);
    }
}
