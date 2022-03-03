### Creating deep observables

#### Collections

So far we have created elements of app state by wrapping standard Python data inside `Observable` objects using the `make_observable` method. By default this makes collections observable but only at a shallow level. That is, changes to the collections themselves are observed but not the elements within them. This is sufficient in most situations but not when the app state needs to be observable at several levels. In these cases one can build nested observable data structures either by explicitly constructing them, or more elegantly by passing a depth argument to `make_observable`. The following example demonstrates how to create a deep observable.

```load_module
tutorial.deep_observable_collection
```

```read_module
tutorial.deep_observable_collection
```

In effect the `depth` argument controls the degree at which the data structure is made observable. In this example the resulting observable object will be of type `ObservableList[ObservableDict[ObservableValue]]`. Note that all changes made to `row_content_values` are applied to `actual_row_values`, which as [previously mentioned](internal:website.reflect.tutorial/observables.md) should only be accessed in "read only" mode.

#### Objects

Deep observability does not only apply to plain data containers (list, dict) but also also arbitrary Python objects. Below is the previous example rewritten using Python objects.

```load_module
tutorial.deep_observable_object
```

```read_module
tutorial.deep_observable_object
```

### Creating Mappings

You might have realized that in the previous example we recompute all the rows every time we add or change an element. This is not a real issue in this simple example but this might become impractical in more complex situations. You can easily solve this problem by defining a `Mapping` object to apply a transformation to the elements of a deep observable collection. The result will be an isomorphic lazily evaluated data structure. Here is the same example as above using a `Mapping`.

```load_module
tutorial.mapping
```

```read_module
tutorial.mapping
```

We added a `print` statement to demonstrate that we call `create_new_row` only once for each row. Users familiar with Excel will find a powerful counterpart to range formulas. Note that this powerful list protocol also supports a `move` method allowing to change the collection order without triggering any re-computations.

### Depth rules

Knowing the right depth value to use can be a bit confusing at the beginning. Here is a overview of how data structures are transformed by `make_observable`. Note that the default `depth` argument value is one.

| Depth | Scalar (str, int, etc) | Collection (dict, list)                                     |
| ----- | ---------------------- | ----------------------------------------------------------- |
| 0     | ObservableValue        | ObservableValue                                             |
| 1     | ObservableValue        | ObservableCollection                                        |
| 2     | ObservableValue        | ObservableCollection[ObservableValue]                       |
| 3     | ObservableValue        | ObservableCollection[ObservableCollection[ObservableValue]] |

## Summary

- Nested data structures can be made observable to the right depth through the `make_observable` depth argument
- `Mapping` efficiently transforms deep observable data structures into isomorphic observable data structures
