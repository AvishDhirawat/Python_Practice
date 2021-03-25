//Author - Avish Dhirawat
//MetaCube Interview Ques
//Create a reverse function to reverse the given array(as argument) without using any additional array and return the reversed array.

#include<stdio.h>

int reverse(int arr[],int n)
{
  int temp;
for(int i=0; i<n/2;i++)
{
temp = arr[n-i-1];
arr[n-i-1] = arr[i];
arr[i] = temp;
}
return *arr;
}

int main()
{
  int arr[20],n;
  printf("Enter the size of Array : ");
  scanf("%d", &n);
  printf("Enter the Elements : \n");
  for(int i=0; i<n; i++)
  {
    scanf("%d", &arr[i]);
  }
  printf("Entered Elements : \n");
  //for (size_t i = 0; i < count; i++)
    /* code */
    for (int i=0; i<n;i++)
    {
      printf("%d\n", arr[i]);
    }
  *arr = reverse(arr, n);
  printf("Elements after reverse : \n");
    for (int i=0; i<n;i++)
    {
      printf("%d\n", arr[i]);
    }
}
