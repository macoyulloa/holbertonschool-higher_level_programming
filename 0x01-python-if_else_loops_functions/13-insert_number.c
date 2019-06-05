#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - insert a new node in a sorted list.
 * @head: linked list.
 * @number: integer, part of the new node.
 * Return: Address of the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *actual_node, *idx;

	idx = *head;
	if (head == NULL)
		return (NULL);
	while (idx->next->number)
		idx = idx->next
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = n;
	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	else if (idx == 0)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	actual_node = *head;
	while (idx - 1 > 0)
	{
		actual_node = actual_node->next;
		idx--;
		if (actual_node == NULL)
		{
			free(new_node);
			return (NULL);
		}
	}
	new_node->next = actual_node->next;
	actual_node->next = new_node;
	return (new_node);
}
