import java.util.Scanner;
class fcfs{
public static void main(String args[])
{
   int bst[],process[],wt[],tat[],i,j,n,total=0,pos,temp=0;
   float wait_avg,TAT_avg;
   
   Scanner s=new Scanner(System.in);
   System.out.print("Enter number of process:");
   n=s.nextInt();
   process=new int[n];
   bst=new int[n];
   wt=new int[n];
   tat=new int[n];
   System.out.print("\nEnter a CPU time");
for(i=0;i<n;i++)
{
   System.out.print("\nProcess["+(i+1)+"]:");
   bst[i]=s.nextInt();
   process[i]=i+1;
}

System.out.print("********FCFS Scheduling**********************");
wt[0]=0;

for(i=1;i<n;i++)
{
  wt[i]=0;
  for(j=0;j<i;j++)
  {
     wt[i]+=bst[j];
     total+=wt[i];
  }
 } 
wait_avg=(float)total/n;

total=0;

System.out.print("**************************************************");
System.out.print("\nProcess \t\t|Burst time \t\t|Waiting Time \t\t|Turn time");
System.out.print("---------------------------------------------------");

for( i=0;i<n;i++)
{
   tat[i]=bst[i]+wt[i];
   total+=tat[i];
   System.out.println("\np"+process[i]+"\t\t|\t"+bst[i]+"\t\t|t"+wt[i]+"\t\t|t"+tat[i]);
   System.out.println("-----------------------------------------------------------");
}   
TAT_avg=(float)total/n;
System.out.println("\n\nAverage Waiting Time"+wait_avg);
System.out.println("\n\nAverage Turnaround  Time"+TAT_avg);
}
}

   

