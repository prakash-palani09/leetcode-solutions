class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int j = 0;
        int ans = 0;
        Set<Character> hsh = new HashSet<>();
        for(int i=0;i<n;i++){
            if(!hsh.contains(s.charAt(i))){
                hsh.add(s.charAt(i));
                ans = Math.max(ans,i-j+1);
            }
            else{
                while(hsh.contains(s.charAt(i))){
                    hsh.remove(s.charAt(j));
                    j++;
                }
                hsh.add(s.charAt(i));
            }
        }
        return ans;
        
    }
}