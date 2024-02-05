#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * Alternative implementation of print_python_bytes.
 * @p: pointer to PyObject p
 */
void print_python_bytes_alternative(PyObject *p)
{
    setbuf(stdout, NULL);
    printf("[.] bytes object info\n");
    
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size_t size = PyBytes_Size(p);
    char *str = PyBytes_AsString(p);
    
    printf("  size: %ld\n  trying string: %s\n", size, str);

    size_t display_size = size >= 10 ? 10 : size;
    
    printf("  first %ld bytes: ", display_size);
    for (size_t i = 0; i < display_size; i++)
        printf("%02hhx ", str[i]);
    printf("\n");
}

/**
 * Alternative implementation of print_python_float.
 * @p: pointer to PyObject p
 */
void print_python_float_alternative(PyObject *p)
{
    setbuf(stdout, NULL);
    printf("[.] float object info\n");
    
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    double f = PyFloat_AsDouble(p);
    printf("  value: %f\n", f);
}

/**
 * Alternative implementation of print_python_list.
 * @p: pointer to PyObject p
 */
void print_python_list_alternative(PyObject *p)
{
    setbuf(stdout, NULL);
    printf("[*] Python list info\n");
    
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    PyListObject *list = (PyListObject *)p;
    size_t size = PyList_Size(p);
    size_t allocated = list->allocated;

    printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, allocated);

    for (size_t i = 0; i < size; i++)
    {
        PyObject *item = list->ob_item[i];
        const char *type_name = Py_TYPE(item)->tp_name;
        printf("Element %li: %s\n", i, type_name);

        if (strcmp(type_name, "bytes") == 0)
        {
            print_python_bytes_alternative(item);
        }
        else if (strcmp(type_name, "float") == 0)
        {
            print_python_float_alternative(item);
        }
    }
}
