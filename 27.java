class Solution 
{
    public int removeElement(int[] nums, int val) 
    {
        if(nums.length==0) return 0; // sanity check
        int index = 0;
        for(int i =0;i<nums.length;i++)
        {
            if(nums[i]!=val) // add element to result only if not equal to val
            {
            nums[index]=nums[i];
            index++;
            }

        }
        return index;
    }
}
