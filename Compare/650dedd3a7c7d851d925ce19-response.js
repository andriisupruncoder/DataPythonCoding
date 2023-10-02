function solution(words, k) {
  let result = [];

  // Create a set to store all prefixes of a certain length
  for (let i = 1; i <= k; i++) {
    let prefixSet = new Set();

    for (let word of words) {
      if (word.length >= i) {
        prefixSet.add(word.substring(0, i));
      }
    }

    result.push(prefixSet.size);
  }

  return result;
}

let words = ['apple', 'app', 'apricot', 'stone'];
let k = 8;
console.log(solution(words, k)); // Expected output: [2, 2, 3, 3, 3, 1, 1, 0]
