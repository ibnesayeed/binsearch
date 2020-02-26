# BinSearch

A Python module for binary search in sorted files.

## Objective

Given a sorted file, perform binary search on disk to find if a given lookup key is present in the file.
The file can have fielded data and matching is desired to be performed on a select few fields only.
It may also be desired to perform a prefix match where the lookup key is a prefix of one or more records in the file.
The search needs to be able to report no matches, all matches, the first match, or the last match.
In case a start and/or end byte position(s) is/are provided, the search should only be performed within that given range.

## Functions

```
find_first(fh, key, **kw) => None | FIRST_MATCHED_LINE
find_last(fh, key, **kw)  => None | LAST_MATCHED_LINE
find_all(fh, key, **kw)   => ITERATOR_OVER_ALL_MATCHED_LINES
```

## Parameters

* `fh` - File handle, open for binary read
* `key` - Bytes, search key
* `fields` - Int, number of fields in each line from the beginning to match against (Default: `None`)
* `matcher` - Function, to identify the portion of lines read for matching, overrides `fields` param (Default: `line.strip()`)
* `prefix` - Boolean, whether perform prefix match or exact (Default: `False`)
* `prefix_boundary` - Bytes, only consider prefix match if the following character is a boundary character (Default: `",/)'\".\s’"`)
* `start` - Int, beginning byte of the start the search boundary (Default: `0`)
* `end` - Int, end byte of the search boundary (Default: `fh.size()`)

## Use Cases

We can see it being useful in many places, but following are a few places where we do have the need:

* [IPWB](https://github.com/oduwsdl/ipwb) Replay Index Search
* [MementoMap](https://github.com/oduwsdl/MementoMap) Prefix Search
* A built-in CLI tool to perform binary search on files

## Considerations

* Should the caller provide a file path (and let the API deal with opening and closing the file) or an open file handle?
  * If the API handles file opening/closing then it will open and close files on each request.
  * If the caller provides a file handle then it can be reused, but the caller needs to write a couple extra lines.
* Should the API check for the file being sorted before performing lookup?
  * If the input file is not sorted then search function may behave in unexpected ways.
  * Checking for sorting has linear complexity that will require reading the whole file once, binding it to each search call will render the benefit of binary search useless.
  * Perhaps we can provide a separate helper function, in case the user wants to ensure it once before performing searches as a bootstrapping procedure.
* Should the API work for reverse sorted files too?
  * It is doable without any efficiency cost, but I do not see enough motivation to add more code complexity, unless there are compelling use cases.
* Should the `find_all()` function return `None` if no match found or an iterator which will terminate at the first iteration and will evaluate to `0` on length calculation?
  * Returning an empty iterator seems more sane approach, but the caller will need to iterate it at least once to see whether there was a match.
  * Returning `None` means the return value is polymorphic and call to the function cannot be used in a loop without first checking for `None` value.
* Should we use an existing implementation?
  * There are a few similar implementations in Python, but their license is not permissive and can not be used in projects with permissive licenses.
