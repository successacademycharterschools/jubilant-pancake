function editDistance(a, b) {
  // if either string is blank, return length of non-blank string
  // if strings are the same, return 0
  if(a.length === 0) return b.length;
  if(b.length === 0) return a.length;
  if(a === b) return 0;

  // create empty array for matrix
  let matrix = [];

  // increment along the first column of each row
  for(let i = 0; i <= b.length; i++){
    matrix[i] = [i];
  }

  // increment each column in the first row
  for(let j = 0; j <= a.length; j++){
    matrix[0][j] = j;
  }

  // Fill in the rest of the matrix
  for(i = 1; i <= b.length; i++){
    for(j = 1; j <= a.length; j++){
      if(b.charAt(i-1) == a.charAt(j-1)){
        // get diagonal value if characters are equal
        matrix[i][j] = matrix[i-1][j-1];
      } else {
        // else get minimum value from adjacent cells + 1
        matrix[i][j] = Math.min(matrix[i-1][j-1], // char substitution
                        matrix[i][j-1], // char insertion
                        matrix[i-1][j]) + 1; // char deletion
      }
    }
  }
  return matrix[b.length][a.length];
}

module.exports = { editDistance }
