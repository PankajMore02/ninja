import java.util.Scanner;
class Fcfs {
public static void main(String args[]){ int
bst[],process[],wt[],tat[],i,j,n,total=0,pos,temp;
float wait_avg, TAT_avg;
Scanner s = new Scanner(System.in);
System.out.print("Enter number of process: "); 
n= s.nextInt();
process = new int[n];
bst = new int[n]; wt
= new int[n]; tat =
new int[n];
System.out.println("\nEnter CPU time:");
for(i=0;i<n;i++)
{
System.out.print("\nProcess["+(i+1)+"]: ");
bst[i] = s.nextInt();;
process[i]=i+1; //Process Number
}
System.out.println("\t\t\t**********FCFS Scheduling*********");
//First process has 0 waiting time
wt[0]=0;
//calculate waiting time
for(i=1;i<n;i++)
{ wt[i]=0;
for(j=0;j<i;j++)
wt[i]+=bst[j];
total+=wt[i];
}
//Calculating Average waiting time
wait_avg=(float)total/n;
total=0;
System.out.println("-----------------------------------------------------------------------");
System.out.println("\nProcess\t\t| Burst Time \t\t|Waiting Time\t\t|Turn Time");
System.out.println("-----------------------------------------------------------------------");
for(i=0;i<n;i++)
{
tat[i]=bst[i]+wt[i];
total+=tat[i];//Calculating TurnaroundTimetotal+=tat[i];
System.out.println("\np"+" "+process[i]+"\t|\t"+" "+bst[i]+"\t\t|\t"+" "+wt[i]+"\t\t|\t"+" "+tat[i]);
System.oiut.println("-----------------------------------------------------------------------");
}//Calculation of Average Turnaround Time
TAT_avg=(float)total/n;
System.out.println("\n\nAverage Waiting Time: "+wait_avg);
System.out.println("\nAverage Turnaround Time: "+TAT_avg);
}
}
