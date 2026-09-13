void moveZeroes(vector<int>& nums) 
{
        int tracker = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if(nums[i] != 0)
            {
                nums[tracker] = nums[i];
                tracker++;
            }
        }

        for (tracker; tracker < nums.size(); tracker++)
        {
            nums[tracker] = 0;
        }
}
