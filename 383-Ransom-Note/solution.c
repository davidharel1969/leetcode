const int*count_occur(char *s){
    int *ans=malloc(sizeof(int)*256);
    memset(ans,0,sizeof(int)*256);
    while(*s)
        ans[*(s++)]++;
    return ans;
}

bool canConstruct(char* ransomNote, char* magazine) {
    int *magazin_counts=count_occur(magazine);
    int *ransom_counts=count_occur(ransomNote);
    for (int i=0;i<256;i++)
        if (ransom_counts[i]>magazin_counts[i])
            return false;
    return true;
    
}