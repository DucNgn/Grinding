function findLucky(arr: number[]): number {
    let maxLucky = -1;
    let frequency = new Map<number, number>();
    for (let i = 0; i < arr.length; i++) {
        let num = arr[i];
        frequency.set(num, frequency.has(num) ? frequency.get(num) + 1 : 1);
    }
    frequency.forEach((value: number, key: number) => {
        if ((value == key) && (value > maxLucky)) {
            maxLucky = value;
        }
    });
    return maxLucky;
};

console.log(findLucky([2, 2, 4, 6]));