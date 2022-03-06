### Caching expensive computations

When displaying computationally intensive or otherwise extensive results it is sometime handy to cache intermediate (aka [memoize](https://en.wikipedia.org/wiki/Memoization)) results. These intermediate results can be complex computations, extensive database queries, etc. which are expensive to evaluate. Reflect allows to compute these results as less often as possible by providing a decorator which will cache previous values, recomputing them only when needed.

```load_module
tutorial.snippets.memoization
```

```read_module
tutorial.snippets.memoization
```

In this example we recompute `expensive_computation` only when `a` changes. This is because the cache status is inferred from the underlying observable objects the computation depends on.

We can also control when memoized methods need to update by passing a controller argument to `memoize` as shown below.

```load_module
tutorial.snippets.memoization_controlled
```

```read_module
tutorial.snippets.memoization_controlled
```

## Summary

- Reflect provides a memoization mechanism which will cache results based on `observable` dependencies
- One can control when cache recomputations occur using a controller object
