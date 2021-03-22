# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <complex.h>
# include <math.h>

void fft(int n,int m,double** Real,double** Imag){
	int i,j,k,n1,n2;
	double c,s,e,a,t1,t2; 
	j = 0; /* bit-reverse */
	n2 = n/2;
	/*
	 * Re-aranging of numbers in bit reversed order
	*/
	for (i=1; i < n - 1; i++){
		n1 = n2;
		while ( j >= n1 ){
			j = j - n1;
			n1 = n1/2;
	   }
		j = j + n1;		   
		if (i < j){
			t1 = (*Real)[i];
			(*Real)[i] = (*Real)[j];
			(*Real)[j] = t1;
			t1 = (*Imag)[i];
			(*Imag)[i] = (*Imag)[j];
			(*Imag)[j] = t1;
	   }
	}
										   										   
	n1 = 0;
	n2 = 1;
	// FFT										 
	for (i=0; i < m; i++){	
		n1 = n2;
		n2 = n2 + n2;
		e = -6.283185307179586/n2;
		a = 0.0;
												 
		for (j=0; j < n1; j++){
			c = cos(a);
			s = sin(a);
			a = a + e;
												
			for (k=j; k < n; k=k+n2){
				/*
				* Doing FFT by multiplying twiddle factors and adding them in each layer  
				* By using Butterfly simplification to reduce number of multiplications
				*/
				t1 = c * (*Real)[k+n1] - s * (*Imag)[k+n1];
				t2 = s * (*Real)[k+n1] + c * (*Imag)[k+n1];
				(*Real)[k+n1] = (*Real)[k] - t1;
				(*Imag)[k+n1] = (*Imag)[k] - t2;
				(*Real)[k] = (*Real)[k] + t1;
				(*Imag)[k] = (*Imag)[k] + t2;
			}
		}
	}
										  
	return;
}
void ifft(int n,int m,double** Real,double** Imag){
	int i,j,k,n1,n2;
	double c,s,e,a,t1,t2; 
	j = 0; /* bit-reverse */
	n2 = n/2;
	/*
	 * Re-aranging of numbers in bit reversed order
	*/
	for (i=1; i < n - 1; i++){
		n1 = n2;
		while ( j >= n1 ){
			j = j - n1;
			n1 = n1/2;
	   }
		j = j + n1;		   
		if (i < j){
			t1 = (*Real)[i];
			(*Real)[i] = (*Real)[j];
			(*Real)[j] = t1;
			t1 = (*Imag)[i];
			(*Imag)[i] = (*Imag)[j];
			(*Imag)[j] = t1;
	   }
	}
										   										   
	n1 = 0;
	n2 = 1;
	// FFT										 
	for (i=0; i < m; i++){	
		n1 = n2;
		n2 = n2 + n2;
		e = -6.283185307179586/n2;
		a = 0.0;
												 
		for (j=0; j < n1; j++){
			c = cos(a);
			s = -sin(a);
			a = a + e;
												
			for (k=j; k < n; k=k+n2){
				/*
				* Doing IFFT by multiplying twiddle factors and adding them in each layer  
				* By using Butterfly simplification to reduce number of multiplications
				*/
				t1 = c * (*Real)[k+n1] - s * (*Imag)[k+n1];
				t2 = s * (*Real)[k+n1] + c * (*Imag)[k+n1];
				(*Real)[k+n1] = (*Real)[k] - t1;
				(*Imag)[k+n1] = (*Imag)[k] - t2;
				(*Real)[k] = (*Real)[k] + t1;
				(*Imag)[k] = (*Imag)[k] + t2;
			}
		}
	}
										  
	return;
}

int main(){
	int n = (1<<20);
	FILE *fin, *fout1, *fout2;
	fin = fopen("../Data/x.dat","r");
	double* xr = (double*)malloc(n * sizeof(double));
	double* hr = (double*)malloc(n * sizeof(double));
	double* xi = (double*)malloc(n * sizeof(double));
	double* hi = (double*)malloc(n * sizeof(double));
	double a[] = {1,-2.52,2.56,-1.206,0.22013};
	double b[] = {0.00345,0.0138,0.020725,0.0138,0.00345};
	
	for(int i=0;i<n;i++){
        double val;
        fscanf(fin, "%lf", &val);
        xr[i] = val;
    }
    hr[0] = (b[0]/a[0]);
	hr[1] = (1/a[0])*(b[1]-a[1]*hr[0]);
	hr[2] = (1/a[0])*(b[2]-a[1]*hr[1]-a[2]*hr[0]);
	hr[3] = (1/a[0])*(b[3]-a[1]*hr[2]-a[2]*hr[1]-a[3]*hr[0]);
	hr[4] = (1/a[0])*(b[4]-a[1]*hr[3]-a[2]*hr[2]-a[3]*hr[1]
			-a[4]*hr[0]);
    for(int i=5;i<n;i++){
		hr[i] = (1/a[0])*(-a[1]*hr[i-1]-a[2]*hr[i-2]-a[3]*hr[i-3]-
				a[4]*hr[i-4]);
	}
	fft(n,20,&xr,&xi);
	fft(n,20,&hr,&hi);
	double* yr = (double*)malloc(n * sizeof(double));
	double* yi = (double*)malloc(n * sizeof(double));
	for(int i=0;i<n;i++){
		yr[i] = xr[i]*hr[i] - xi[i]*hi[i];
		yi[i] = xr[i]*hi[i] + xi[i]*hr[i];
	}
    fout1  = fopen("../Data/Ynfft.dat", "w");
    for(int i = 0; i < n; i++){
        fprintf(fout1, "%lf+%lfi \n", yr[i],yi[i]);//sqrt(yr[i]*yr[i]+yi[i]*yi[i]));
    }
    
    ifft(n,20,&yr,&yi);
    for(int i = 0; i < n; i++){
        yr[i] = yr[i]/n;
    }
    fout2  = fopen("../Data/ynfft.dat", "w");
    for(int i = 0; i < n; i++){
        fprintf(fout2, "%lf \n", yr[i]);
    }
    fclose(fin);
    fclose(fout1);
    fclose(fout2);
    return 0;
}


