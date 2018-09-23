#include<stdio.h>
#include<conio.h>
int main()
{   int h,m,h2,m2,tot_h_1,tot_h_2,ans,ans_hr,ans_min;
	
	scanf("%d  %d  \n %d   %d",&h,&m,&h2,&m2);
	tot_h_1=(h*60)+(m);
	tot_h_2=(h2*60)+(m2);
	ans=tot_h_1-tot_h_2;
	ans_hr=ans/60;
	ans_min=ans%60;
	printf("%d %d",ans_hr,ans_min);
	
	return 0;
	

}
