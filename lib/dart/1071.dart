import 'dart:math';

class Solution {
  String gcdOfStrings(String str1, String str2) {
    int len1 = str1.length;
    int len2 = str2.length;
    bool isDivisor(int i) {
      if (len1 % i == true || len2 % i == true) {
        return false;
      }
      int f1 = len1 ~/ i;
      int f2 = len1 ~/ i;
      return (str1.substring(i))
    }

    for (int i = min(len1, len2); i > 0; i -= 1) {
      if (isDivisor(i) == true) {
        return str1.substring(0, i);
      }
      return "";
    }
  }
}

Solution sol = Solution();

void main() {
  sol.gcdOfStrings("ABCABC", "ABC");
}
