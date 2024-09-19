#include <Python.h>

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
	Py_ssize_t size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

    /* Check if p is a valid Python list */
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %zd: %s\n", i, type);

		/* If the element is of type bytes, print its byte info */
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object.
 * @p: The Python object to print.
 *
 * This function prints the size of a Python bytes object and up to the first
 * 10 bytes in hexadecimal format. If the object is not a Python bytes object,
 * an error message is printed.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes;

	printf("[.] bytes object info\n");

	/* Check if p is a valid Python bytes object */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = ((PyVarObject *)p)->ob_size;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	/* Limit to the first 10 bytes */
	size = size > 10 ? 10 : size;
	printf("  first %zd bytes: ", size + 1);

	for (i = 0; i <= size; i++)
	{
		printf("%02hhx", (unsigned char)bytes->ob_sval[i]);
		if (i < size)
			printf(" ");
		else
			printf("\n");
	}
}

