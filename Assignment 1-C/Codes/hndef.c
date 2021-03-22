# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <complex.h>
# include <math.h>

int main(){
	int n = (1<<20);
	FILE *fout;
	//fin = fopen("../Data/hndef.dat","r");
	//printf("%ld",sizeof(fin));
	double* h = (double*)malloc(n * sizeof(double));
	double a[] = {1,-2.52,2.56,-1.206,0.22013};
	double b[] = {0.00345,0.0138,0.020725,0.0138,0.00345};
	
    h[0] = (b[0]/a[0]);
	h[1] = (1/a[0])*(b[1]-a[1]*h[0]);
	h[2] = (1/a[0])*(b[2]-a[1]*h[1]-a[2]*h[0]);
	h[3] = (1/a[0])*(b[3]-a[1]*h[2]-a[2]*h[1]-a[3]*h[0]);
	h[4] = (1/a[0])*(b[4]-a[1]*h[3]-a[2]*h[2]-a[3]*h[1]
			-a[4]*h[0]);
    for(int i=5;i<n;i++){
		h[i] = (1/a[0])*(-a[1]*h[i-1]-a[2]*h[i-2]-a[3]*h[i-3]-
				a[4]*h[i-4]);
	}
    fout  = fopen("../Data/hndef.dat", "w");
    
    for(int i = 0; i < 100; i++){
        fprintf(fout, "%lf\n", h[i]);
    }
    fclose(fout);
    
    return 0;
}

