#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer to listint_t.
 * @number: int number.
 *
 * Return: the address of the new node, or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur = *head;
	listint_t *new;
	listint_t *prev = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (cur != NULL)
	{
		cur = cur->next;
		if (new->n < cur->n)
		{
			new->next = cur;
			prev->next = new;
			return (new);
		}
		else if (cur->next == NULL)
		{
			cur->next = new;
			new->next = NULL;
			return (new);
		}
		prev = prev->next;
	}
	return (NULL);
}
