#include "lists.h"

/**
 * comp_lists - comp lists
 * @p1: p1
 * @p2: p2
 * Return: 1 if pal else 0
 */
int comp_lists(listint_t *p1, listint_t *p2)
{
	while (p1 && p2)
	{
		if (p1->n != p2->n)
			return (0);
		p1 = p1->next;
		p2 = p2->next;
	}
	return (1);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *next;
	int is_pal;

	slow = *head;
	fast = *head;
	prev = NULL;
	next = NULL;

	if (!*head || !(*head)->next)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast)
		slow = slow->next;

	is_pal = comp_lists(prev, slow);

	return (is_pal);
}
