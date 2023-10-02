To solve this problem, we can start by generating all possible prefixes for each word in the given list. Then, for each length from 1 to k, we can collect all unique prefixes of that length from our generated list. Here's how you can achieve this using ES6:

```javascript
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
```

This function works by iterating over each length from 1 to k and then, for each word, it adds the prefix of the specified length to a set. The set inherently handles the uniqueness of the prefixes. The size of the set (which represents the count of unique prefixes) is then added to the result array.
