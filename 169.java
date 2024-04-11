class Solution {
    public int majorityElement(int[] nums) 
    {
        Arrays.sort(nums); // sort array
        int n = nums.length;
        return nums[n/2]; // majority always middle element acc to definition 
           
    }
}
