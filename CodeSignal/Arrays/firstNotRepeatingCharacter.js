function firstNotRepeatingCharacter(s) {
    let abc = Array(26).fill(-1);
    const max = 100001;
    let result = max, i;
    for(i = 0; i < s.length; i++) {
        let currentChar = s[i].charCodeAt(0) - 97;
        if(abc[currentChar] === -1) abc[currentChar] = i;
        else abc[currentChar] = -2;
    }

    for(i = 0; i < abc.length; i++) {
        console.log(result, abc[i], i);
        if(abc[i] !== -1 && abc[i] !== -2 && result > abc[i]) result = abc[i];
    }

    if(result === max) return '_';
    else return String.fromCharCode(s[result].charCodeAt(0));
}
