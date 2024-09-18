#include <Python.h>
#include <stdio.h>

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
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
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
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("[*] Python bytes info\n");
	printf("[*] Size of the Python Bytes = %zd\n", size);

	char *buffer = PyBytes_AsString(p);

	printf("[*] First %zd bytes: ", size < 10 ? size : 10);

	for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++)
	{
		printf("%02x ", (unsigned char)buffer[i]);
	}
	printf("\n");
}

