# How to convert all CRLF line endings to LF?

Unix: Use `find . -type f -name '*$EXTENSION' -print -exec sed -i 's/\r//' {} \;`, where `$EXTENSION` is the file type to replace in, i.e. `.md`.
