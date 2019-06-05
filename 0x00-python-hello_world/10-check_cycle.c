#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a loop.
 * @list: the singly linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slowNode, *fastNode;

	slowNode = list;
	fastNode = list;
	while (slowNode && fastNode && fastNode->next)
	{
		if (slowNode == fastNode->next || slowNode == fastNode->next->next)
		return (1);
	slowNode = slowNode->next;
	fastNode = fastNode->next->next;
	}
	return (0);
}
