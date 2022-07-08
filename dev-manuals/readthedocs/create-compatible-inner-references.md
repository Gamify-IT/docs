# How to reference another section in the current document (compatibly)

ReadTheDocs needs explicit section marks to allow for referencing content on the same page.  
Services like GitHub can automatically create section marks based on titles.

## Tutorial based on an example

You want to link to the section under

```md
# Example
```

For _GitHub_, you don't have to do any additional work, you can reference it already using `[link text](#example)`.  
For _ReadTheDocs_, you need to adapt the heading as follows:

```md
(#example)=
# Example
```

Now both services link to the expected section, at the cost that GitHub will display the text `(#example)=` because it doesn't know what that is.
