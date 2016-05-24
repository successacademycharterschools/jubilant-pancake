"use strict"

module.exports = {
	/**
	 * returns the minimum number of operations required to transform one string into another
	 * @param  {String} alpha first input string
	 * @param  {String} beta  second input string
	 * @return {Number}       minimum number of operations required to complete the transformation
	 */
	minimumEditDistance(alpha, beta, options) {
		// make sure neither string is null or undefined
		alpha = alpha || '';
		beta = beta || '';

		// if either is empty string, the others length is the minimum number of operations required
		if (!alpha) return beta.length;
		if (!beta) return alpha.length;

		if (options && options.caseSensitive===false){
			alpha = alpha.toLowerCase();
			beta = beta.toLowerCase();
		}
		
		// construct the matrix
		let matrix = new Array(alpha.length+1);
		for (let a=0; a<matrix.length; a++){
			matrix[a] = new Array(beta.length+1);
			if (a===0){
				for (let b=0; b<matrix[a].length; b++){
					matrix[a][b] = b;
				}
			}else{
				matrix[a][0] = a;
			}
		}

		// determine bottom right element's value in a given 2x2 window, and scan entire matrix
		for (let a = 0; a < alpha.length; a++) {
			const ca = alpha[a];
			for (let b = 0; b < beta.length; b++) {
				const cb = beta[b];
				if (ca == cb) {
					matrix[a + 1][b + 1] = matrix[a][b];
				} else {
					let min = matrix[a][b] > matrix[a][b + 1] ? matrix[a][b + 1] : matrix[a][b];
					min = matrix[a + 1][b] > min ? min : matrix[a + 1][b];
					matrix[a + 1][b + 1] = min + 1;
				}
			}
		}
		return matrix[alpha.length][beta.length];
	}

}