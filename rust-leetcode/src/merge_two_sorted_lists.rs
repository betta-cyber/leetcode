// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

use crate::ListNode;
use std::boxed::Box;

impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match  (list1, list2) {
            (Some(l), None) => return Some(l),
            (None, Some(r)) => return Some(r),
            (None, None) => return None,
            (Some(l), Some(r)) => {
              if l.val <= r.val {
                return Some(Box::new(ListNode{ next: Self::merge_two_lists(l.next, Some(r)), val: l.val }));
              } else {
                return Some(Box::new(ListNode{ next: Self::merge_two_lists(Some(l), r.next), val: r.val }));
              }
            },
        }
    }
}

pub struct Solution;

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::ListNode;
    use std::boxed::Box;

    #[test]
    fn test() {
        assert_eq!(Solution::merge_two_lists(
                Some(Box::new(ListNode::new(1))),
                Some(Box::new(ListNode::new(2)))
        ), Some(Box::new(ListNode{ val: 1, next: Some(Box::new(ListNode::new(2)))})));

        assert_eq!(Solution::merge_two_lists(
                None,
                None,
        ), None);
    }
}
