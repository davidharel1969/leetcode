void moveZeroes(int* nums, int numsSize) {
    int target=-1;
    int num_zeros=0;
    for (int i=0;i<numsSize;i++){
        if (nums[i]==0){
            num_zeros++;
            if (target==-1)
                target=i;
        
            continue;
        }
        if (target!=-1){
            nums[target]=nums[i];
            target++;
        }
    }
    for (int i=numsSize-num_zeros;i<numsSize;i++)
        nums[i]=0;
    
}