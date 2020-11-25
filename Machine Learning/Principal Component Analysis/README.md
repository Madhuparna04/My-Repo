This Project contains implementation of Principal Component Analysis Algorithm from scratch in python.

The contributors to this project are - Madhuparna, Arpitha, Aniketh and Saurabh Agarwala.

This project uses two different algorithms to find the eigenvalues and eigenvectors which is an important step in the PCA algorithm.

1. Power Iteration Algorithm -

	a)	Power Iteration method finds the eigenvector corresponding to the largest(magnitude) eigenvalue of a matrix.

	b)  	From the largest eigenvector the eigenvalue can be calculated using  Rayleigh quotient.

	c)	By finding a matrix B with same eigenvalues as A except the largest eigenvalue of A being zero by using Wielandt’s Deflation the algorithm can be further used to find second largest, third largest and so on all the eigenvalues of a matrix.


2. QR - Decomposition

	Algorithm

	a) Use QR decomposition to find the QR values of a given matrix.

	b) Pass the normalized and covariance matrix of the given matrix to the QR algorithm to find its matrix of eigenvectors.

	c) Before calculating the eigenvectors, the matrix must be converted to Hessenberg form using Householder transformation.

	d) The QR algorithm iteratively reduces a matrix to its matrix of eigenvectors.

	e) Multiply the original matrix with this matrix of eigenvectors.

	f) Select two columns of this matrix as the Principal Components for the given matrix to reduce it to a dimension of 2.

The codes are available in jupyter notebook format and can be used with Google Colab.






