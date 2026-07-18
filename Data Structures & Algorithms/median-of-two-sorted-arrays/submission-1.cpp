class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }

        int count = nums1.size() + nums2.size();
        int half = (count + 1) / 2;

        int low = 0, high = nums1.size();
        int left1 = 0, left2 = 0, right1 = 0, right2 = 0;

        while (low <= high){
            int mid1 = low + (high-low) / 2;
            int mid2 = half - mid1;

            left1 = mid1 > 0 ? nums1[mid1 - 1] : -1e7;
            left2 = mid2 > 0 ? nums2[mid2 - 1] : -1e7;
            right1 = mid1 < nums1.size() ? nums1[mid1] : 1e7;
            right2 = mid2 < nums2.size() ? nums2[mid2] : 1e7;

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

        return (count % 2 == 0) ? (max(left1, left2) + min(right1, right2)) / 2.0 : max(left1, left2);    
    }
};
