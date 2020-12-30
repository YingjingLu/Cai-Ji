public int jump(int[] nums) {
        int[] minjumps=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            for(int j=1;j<=nums[i];j++){
                if(i+j<nums.length){
                    if(minjumps[i+j]==0){
                        minjumps[i+j]=minjumps[i]+1;
                    }else if(minjumps[i+j]>minjumps[i]+1){
                        minjumps[i+j]=minjumps[i]+1;
                    }
                }
            }
        }
        return minjumps[minjumps.length-1];
    }