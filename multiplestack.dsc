#include<stdio.h>
#define max 10
int top1,top2,arr[max],b1,b2;
void push();
void pop();
void display();
void main()
{
	int ch;
	top1=b1=-1;
	top2=b2=(max-1)/2;
	do
	{
		printf("\n1. Push\n2. Pop\n3. Display\n4. Exit\nChoice: ");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:push();
				break;
			case 2:pop();
				break;
			case 3:display();
				break;
			case 4:printf("Exiting from program\n");
				break;
			default:printf("Wrong Choice\n");
		}
	}
	while(ch!=4)                     ;
}

void push()
{
	int x,ch;
	printf("Enter a number ");
	scanf("%d",&x);
	printf("Press 1 to push in stack 1 or press 2 to push in stack 2\n");
	scanf("%d",&ch);
	if(ch==1)
	if(top1==b2)
		{
		printf("Stack overflow\n");
		return;
		}
	else
		arr[++top1]=x;
	if(ch==2)
	if(top2==max-1)
	{
		printf("Stack overflow\n");
		return;
	}
	else
		arr[++top2]=x;
}

void pop()
{
	int y,ch;
	printf("Press 1 to pop in stack 1 or press 2 to pop in stack 2\n");
	scanf("%d",&ch);
	if(ch==1)
	{
		if(top1==-1)
		{
			printf("Stack underflow\n");
			return;
		}
	y=arr[top1];
	arr[top1--]=0;
	}
	else
	{
		if(top2==b2)
		{
			printf("Stack underflow\n");
			return;
		}
	y=arr[top2];
	arr[top2--]=0;
	}
printf("Element has popped\n");
return;
}

void display()
{
	int i;
	if(top1==-1)
		printf("Stack 1 is empty\n");
	else
	{
		printf("The elements of stack 1 are :\n");
		for(i=0;i<=top1;i++)
			printf("%d\n",arr[i] );
	}
	if(top2==b2)
		printf("Stack 2 is empty\n");
	else
	{
		printf("The elements of stack 2 are :\n");
		for(i=b2+1;i<=top2;i++)
			printf("%d\n",arr[i] );
	}
return;
}
