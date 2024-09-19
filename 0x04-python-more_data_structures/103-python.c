#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - Prints basic information about a Python list.
 * @p: The Python object to print.
 *
 * This function prints the size and allocated slots of a Python list.
 * It also iterates through the list to print the type of each element.
 * If the object is not a Python list, an error message is printed.
 */
void print_python_list(PyObject *p)
{
	int size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp-name;
		
		printf("Element %d: %s\n", i, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic information about
 * a Python bytes object.
 * @p: The Python object to print.
 *
 * This function prints the size of a Python bytes
 * object and up to the first
 * 10 bytes in hexadecimal format. If the object is
 * not a Python bytes object,
 * an error message is printed.
 */

void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp-name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);

	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);

		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

