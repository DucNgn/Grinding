function threeConsecutiveOdds(arr: number[]): boolean {
    return doCheck(arr, 0);
 };
 
 function doCheck(arr: number[], ctr: number): boolean {
     if (ctr == 3) {
         return true;
     } else if (arr.length == 0) {
         return false;
     } else {
        if(arr[0] % 2 != 0) {
             ctr++;
        } else {
            ctr = 0;
        }
        arr.shift();
        return doCheck(arr, ctr);
     }
 }
