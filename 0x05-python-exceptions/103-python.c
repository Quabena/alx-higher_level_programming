#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	/* Check if the object is a list */
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	/* Get the size of the list */
	size = PyList_GET_SIZE(p);
	printf("[*] Size of the list: %zd\n", size);
	printf("[*] Allocated: %ld\n", ((PyListObject *)p)->allocated);

	/* Iterate through the list items */
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects.
 * @p: PyObject pointer to a Python bytes object
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	const char *bytes;

	/* Check if the object is a bytes */
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Get the size of the bytes object */
	size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);

	printf("[*] Size of the bytes: %zd\n", size);
	printf("[*] First %zd bytes: ", size < 10 ? size : 10);

	/* Print a maximum of 10 bytes */
	for (i = 0; i < (size < 10 ? size : 10); i++)
	{
		printf("%02x ", (unsigned char)bytes[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: PyObject pointer to a Python float object
 */

void print_python_float(PyObject *p)
{
	double value;

	/* Check if the object is a float */
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	/* Get the value of the float object */
	value = PyFloat_AsDouble(p);
	printf("[*] Value of the float: %f\n", value);
}
