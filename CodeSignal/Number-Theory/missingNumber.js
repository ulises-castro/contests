function missingNumber(arr) {
    const expectValue = arr.length;
    const sumArr = arr.reduce( (sum, currentValue ) => sum + currentValue );
    const total = expectValue * (expectValue + 1) / 2;
    return total - sumArr;
}