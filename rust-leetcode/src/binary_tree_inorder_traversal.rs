use std::rc::Rc;
use std::cell::RefCell;
use crate::TreeNode;

impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {

        fn do_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
            let mut res :Vec<i32> = Vec::new();

            if let Some(root) = root.as_ref().map(|n| n.borrow()) {
                res.append(&mut do_traversal(root.left.clone()));
                res.push(root.val);
                res.append(&mut do_traversal(root.right.clone()));
            };
            return res;
        }

        let _res = do_traversal(root);
        _res
    }
}

pub struct Solution;

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::btree;

    #[test]
    fn test() {
        assert_eq!(Solution::inorder_traversal(btree![1, null, 2, 3]), vec![1, 3, 2]);
    }
}
