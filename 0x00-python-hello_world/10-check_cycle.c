#include "lists.h"
/**
 * check_cycle - checks if the linked list is cyclick or not.
 * @list: poiter to list.
 * 
 * Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *slowPtr = list;
	listint_t *fastPtr = list;

	while (slowPtr != NULL &&
			fastPtr != NULL &&
			fastPtr->next != NULL)
	{
		slowPtr = slowPtr->next;
		fastPtr = fastPtr->next->next;
		if (slowPtr == fastPtr)
		{
			return (1);
		}
	}
	return (0);
}
