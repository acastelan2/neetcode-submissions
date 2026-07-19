public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.Length > nums2.Length){
            (nums1, nums2) = (nums2, nums1);
        }

        int count = nums1.Length + nums2.Length;
        int half = (count + 1) / 2;

        int low = 0, high = nums1.Length;
        int left1 = 0, left2 = 0, right1 = 0, right2 = 0;

        while (low <= high){
            int mid1 = low + (high-low) / 2;
            int mid2 = half - mid1;

            left1 = mid1 > 0 ? nums1[mid1 - 1] : (int)-1e7;
            left2 = mid2 > 0 ? nums2[mid2 - 1] : (int)-1e7;
            right1 = mid1 < nums1.Length ? nums1[mid1] : (int)1e7;
            right2 = mid2 < nums2.Length ? nums2[mid2] : (int)1e7;

            if (left1 > right2){
                high = mid1 - 1;
                continue;
            }
            if (left2 > right1){
                low = mid1 + 1;
                continue;
            }
            break;
        }

        return (count % 2 == 0) ? (Math.Max(left1, left2) + Math.Min(right1, right2)) / 2.0 : Math.Max(left1, left2);  
    }
}
