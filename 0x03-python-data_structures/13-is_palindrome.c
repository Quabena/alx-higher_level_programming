#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the pointer of the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	int len, i;
	listint_t *temp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);

	temp = *head;
	middle = *head;

	for (len = 0; temp != NULL; len++)
		temp = temp->next;

	len = len / 2;

	for (i = 1; i < len; i++)
		middle = middle->next;

	if (len % 2 != 0 && len != 1)
	{
		middle = middle->next;
		len = len - 1;
	}

	reverse_list(&middle);
	i = compare_lists(*head, middle, len);

	return (i);
}

/**
* compare_lists - compare two lists
* @head: Pointer to the head node
* @middle: Pointer to the middle node
* @len: Length of the list
* Return: 1 if the same, else 0
*/

int compare_lists(listint_t *head, listint_t *middle, int len)
{
	int i;

	if (head == NULL || middle == NULL)
		return (1);

	for (i = 0; i < len; i++)
	{
		if (head->n != middle->n)
			return (0);

		head = head->next;
		middle = middle->next;
	}

	return (1);
}

/**
 * reverse_list - Reverses a singly linked list
 * @head: Pointer to the head of the list
 */

void reverse_list(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *prev;

	if (head == NULL || *head == NULL)
		return;

	prev = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

